#!/usr/bin/env python3
"""Build a refreshable CSV audit of open assignment pull requests."""

import argparse
import csv
import json
import subprocess
import sys
from collections import defaultdict
from pathlib import Path
from typing import (
    Dict,
    Iterable,
    List,
    Mapping,
    Optional,
    Sequence,
    TextIO,
    Tuple,
)

try:
    from scripts.validate_assignment_pr import PATH_PATTERN, validate_paths
except ModuleNotFoundError:  # Support direct execution from the scripts folder.
    from validate_assignment_pr import PATH_PATTERN, validate_paths


AUDIT_FIELDS = (
    "pr_number",
    "title",
    "author",
    "url",
    "day",
    "batch",
    "student",
    "changed_files",
    "duplicate_group",
    "structure_status",
    "completion_status",
    "review_notes",
    "action",
)


def _identity(paths: Iterable[str]) -> Optional[Tuple[str, str, str]]:
    matches = [PATH_PATTERN.fullmatch(path) for path in paths]
    if not matches or any(match is None for match in matches):
        return None
    identities = {
        (match.group("day"), match.group("batch"), match.group("student"))
        for match in matches
    }
    if len(identities) != 1:
        return None
    day, batch, student = identities.pop()
    return f"day-{day}", batch, student


def build_audit_rows(
    pull_requests: Iterable[Mapping[str, object]],
    files_by_number: Mapping[int, List[str]],
) -> List[Dict[str, object]]:
    rows = []
    groups = defaultdict(list)

    for pull_request in pull_requests:
        number = int(pull_request["number"])
        paths = files_by_number.get(number, [])
        identity = _identity(paths)
        errors = validate_paths(paths)
        row = {
            "pr_number": number,
            "title": pull_request.get("title", ""),
            "author": (pull_request.get("user") or {}).get("login", ""),
            "url": pull_request.get("html_url", ""),
            "day": identity[0] if identity else "",
            "batch": identity[1] if identity else "",
            "student": identity[2] if identity else "",
            "changed_files": " | ".join(paths),
            "duplicate_group": "/".join(identity) if identity else "",
            "structure_status": "valid" if not errors else "; ".join(errors),
            "completion_status": "pending-review",
            "review_notes": "",
            "action": "review",
        }
        rows.append(row)
        if identity:
            groups[identity].append(row)

    for group_rows in groups.values():
        if len(group_rows) < 2:
            continue
        newest_number = max(int(row["pr_number"]) for row in group_rows)
        for row in group_rows:
            if int(row["pr_number"]) == newest_number:
                row["action"] = "review-newest"
            else:
                row["action"] = f"superseded-by-#{newest_number}"

    return sorted(rows, key=lambda row: int(row["pr_number"]), reverse=True)


def merge_existing_review(
    refreshed_rows: List[Dict[str, object]],
    existing_rows: Iterable[Mapping[str, object]],
) -> List[Dict[str, object]]:
    existing_by_number = {
        int(row["pr_number"]): row for row in existing_rows if row.get("pr_number")
    }
    for row in refreshed_rows:
        existing = existing_by_number.get(int(row["pr_number"]))
        if not existing:
            continue
        completion = str(existing.get("completion_status", ""))
        notes = str(existing.get("review_notes", ""))
        if completion and completion != "pending-review":
            row["completion_status"] = completion
            row["review_notes"] = notes
            row["action"] = existing.get("action", row["action"])
    return refreshed_rows


def write_audit(rows: Iterable[Mapping[str, object]], output: TextIO) -> None:
    writer = csv.DictWriter(output, fieldnames=AUDIT_FIELDS)
    writer.writeheader()
    writer.writerows(rows)


def _gh_api(endpoint: str) -> List[dict]:
    result = subprocess.run(
        ["gh", "api", "--paginate", "--slurp", endpoint],
        check=False,
        capture_output=True,
        text=True,
    )
    if result.returncode:
        raise RuntimeError(result.stderr.strip() or "GitHub API request failed.")

    pages = json.loads(result.stdout)
    if pages and all(isinstance(page, list) for page in pages):
        return [item for page in pages for item in page]
    return pages


def main(argv: Optional[Sequence[str]] = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo", required=True, help="GitHub repository as owner/name.")
    parser.add_argument(
        "--output", required=True, type=Path, help="Destination CSV audit file."
    )
    args = parser.parse_args(argv)

    try:
        pull_requests = _gh_api(
            f"repos/{args.repo}/pulls?state=open&per_page=100"
        )
        files_by_number = {}
        for pull_request in pull_requests:
            number = int(pull_request["number"])
            file_records = _gh_api(
                f"repos/{args.repo}/pulls/{number}/files?per_page=100"
            )
            files_by_number[number] = [
                str(file_record["filename"]) for file_record in file_records
            ]
    except (KeyError, RuntimeError, TypeError, ValueError, json.JSONDecodeError) as error:
        print(f"Error: {error}", file=sys.stderr)
        return 1

    existing_rows = []
    if args.output.exists():
        with args.output.open(encoding="utf-8", newline="") as existing_file:
            existing_rows = list(csv.DictReader(existing_file))

    rows = merge_existing_review(
        build_audit_rows(pull_requests, files_by_number), existing_rows
    )
    args.output.parent.mkdir(parents=True, exist_ok=True)
    with args.output.open("w", encoding="utf-8", newline="") as output:
        write_audit(rows, output)
    print(f"Wrote {len(rows)} open pull requests to {args.output}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
