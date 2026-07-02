#!/usr/bin/env python3
"""Validate the files changed by an assignment pull request."""

import argparse
import re
import sys
from pathlib import Path
from typing import Iterable, List, Optional, Sequence


PATH_PATTERN = re.compile(
    r"^assignments/day-(?P<day>0[1-9]|1[0-4])/submissions/"
    r"(?P<batch>batch-[ab])/(?P<student>[A-Za-z0-9][A-Za-z0-9_-]*)/"
    r"(?P<filename>[^/]+)$"
)

SPECIAL_REQUIRED_FILES = {
    7: {"solution.py", "sales_data.csv"},
    10: {
        "solution.py",
        "monthly_sales_line.png",
        "students_by_course_bar.png",
        "course_enrollment_pie.png",
        "study_hours_scatter.png",
        "course_growth.png",
    },
    11: {
        "solution.py",
        "course_count.png",
        "average_marks_bar.png",
        "study_hours_marks_scatter.png",
        "marks_boxplot.png",
        "marks_histogram.png",
        "student_correlation_heatmap.png",
    },
}


def validate_paths(paths: Iterable[str]) -> List[str]:
    submitted = list(paths)
    if not submitted:
        return ["No changed files were provided."]

    errors = []
    duplicates = sorted({path for path in submitted if submitted.count(path) > 1})
    if duplicates:
        errors.append(f"Duplicate changed path: {', '.join(duplicates)}")

    matches = []
    invalid_paths = []
    for path in submitted:
        match = PATH_PATTERN.fullmatch(path)
        if match is None:
            invalid_paths.append(path)
        else:
            matches.append(match)
    if invalid_paths:
        errors.append(
            "Invalid submission paths (only assignment files are allowed): "
            + ", ".join(sorted(invalid_paths))
        )
        return errors

    days = {match.group("day") for match in matches}
    batches = {match.group("batch") for match in matches}
    students = {match.group("student") for match in matches}
    if len(days) != 1:
        errors.append("A pull request must contain exactly one assignment day.")
    if len(batches) != 1:
        errors.append("A pull request must contain exactly one batch.")
    if len(students) != 1:
        errors.append("A pull request must contain exactly one student folder.")
    if len(days) != 1 or len(batches) != 1 or len(students) != 1:
        return errors

    day = int(matches[0].group("day"))
    required_files = SPECIAL_REQUIRED_FILES.get(day, {"solution.py"})
    filenames = {match.group("filename") for match in matches}
    missing_files = sorted(required_files - filenames)
    unexpected_files = sorted(filenames - required_files)
    if missing_files:
        errors.append(f"Missing required files: {', '.join(missing_files)}")
    if unexpected_files:
        errors.append(f"Unexpected files: {', '.join(unexpected_files)}")

    return errors


def main(argv: Optional[Sequence[str]] = None) -> int:
    parser = argparse.ArgumentParser(
        description="Validate changed files in an assignment pull request."
    )
    parser.add_argument(
        "--paths-file",
        required=True,
        type=Path,
        help="Text file containing one changed repository path per line.",
    )
    args = parser.parse_args(argv)

    paths = [
        path
        for path in args.paths_file.read_text(encoding="utf-8").splitlines()
        if path
    ]
    errors = validate_paths(paths)
    if errors:
        for error in errors:
            print(f"::error::{error}", file=sys.stderr)
        return 1

    print("Assignment structure is valid.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
