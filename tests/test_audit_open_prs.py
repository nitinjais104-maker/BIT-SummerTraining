import csv
import io
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

from scripts.audit_open_prs import (
    build_audit_rows,
    main,
    merge_existing_review,
    write_audit,
)


class AuditOpenPullRequestsTests(unittest.TestCase):
    def test_builds_a_review_row_for_a_valid_pull_request(self):
        pull_requests = [
            {
                "number": 396,
                "title": "Day 05 Assignment - Rahul",
                "user": {"login": "rahul"},
                "html_url": "https://github.com/example/repo/pull/396",
            }
        ]
        files = {
            396: ["assignments/day-05/submissions/batch-b/Rahul-Singh/solution.py"]
        }

        rows = build_audit_rows(pull_requests, files)

        self.assertEqual("day-05", rows[0]["day"])
        self.assertEqual("batch-b", rows[0]["batch"])
        self.assertEqual("Rahul-Singh", rows[0]["student"])
        self.assertEqual("valid", rows[0]["structure_status"])
        self.assertEqual("pending-review", rows[0]["completion_status"])
        self.assertEqual("review", rows[0]["action"])

    def test_records_actionable_structure_errors(self):
        pull_requests = [
            {
                "number": 385,
                "title": "Day 12 assignment",
                "user": {"login": "student"},
                "html_url": "https://github.com/example/repo/pull/385",
            }
        ]
        files = {
            385: [
                "assignments/day-12/submissions/batch-b/AnkitaSingh/solution .py"
            ]
        }

        rows = build_audit_rows(pull_requests, files)

        self.assertIn("Missing required files", rows[0]["structure_status"])
        self.assertIn("solution .py", rows[0]["structure_status"])

    def test_marks_only_the_newest_duplicate_for_review(self):
        pull_requests = [
            {
                "number": number,
                "title": f"Assignment {number}",
                "user": {"login": "student"},
                "html_url": f"https://github.com/example/repo/pull/{number}",
            }
            for number in (86, 85)
        ]
        path = "assignments/day-02/submissions/batch-a/Muskan-Verma/solution.py"
        files = {86: [path], 85: [path]}

        rows = build_audit_rows(pull_requests, files)
        rows_by_number = {row["pr_number"]: row for row in rows}

        self.assertEqual("review-newest", rows_by_number[86]["action"])
        self.assertEqual("superseded-by-#86", rows_by_number[85]["action"])
        self.assertEqual(
            "day-02/batch-a/Muskan-Verma", rows_by_number[86]["duplicate_group"]
        )

    def test_writes_csv_with_changed_files_and_review_columns(self):
        rows = build_audit_rows(
            [
                {
                    "number": 7,
                    "title": "Day 1",
                    "user": {"login": "student"},
                    "html_url": "https://github.com/example/repo/pull/7",
                }
            ],
            {7: ["assignments/day-01/submissions/batch-a/student/solution.py"]},
        )
        output = io.StringIO()

        write_audit(rows, output)

        parsed = list(csv.DictReader(io.StringIO(output.getvalue())))
        self.assertEqual("7", parsed[0]["pr_number"])
        self.assertIn("solution.py", parsed[0]["changed_files"])
        self.assertIn("completion_status", parsed[0])
        self.assertIn("review_notes", parsed[0])
        self.assertIn("action", parsed[0])

    def test_refresh_preserves_completed_manual_review(self):
        refreshed = build_audit_rows(
            [
                {
                    "number": 7,
                    "title": "Day 1",
                    "user": {"login": "student"},
                    "html_url": "https://github.com/example/repo/pull/7",
                }
            ],
            {7: ["assignments/day-01/submissions/batch-a/student/solution.py"]},
        )
        existing = [
            {
                "pr_number": "7",
                "completion_status": "complete",
                "review_notes": "All six questions answered.",
                "action": "merge",
            }
        ]

        rows = merge_existing_review(refreshed, existing)

        self.assertEqual("complete", rows[0]["completion_status"])
        self.assertEqual("All six questions answered.", rows[0]["review_notes"])
        self.assertEqual("merge", rows[0]["action"])

    def test_cli_fetches_open_prs_and_writes_the_live_audit(self):
        pull_requests = [
            {
                "number": 7,
                "title": "Day 1",
                "user": {"login": "student"},
                "html_url": "https://github.com/example/repo/pull/7",
            }
        ]
        files = [
            {
                "filename": "assignments/day-01/submissions/batch-a/student/solution.py"
            }
        ]
        with tempfile.TemporaryDirectory() as directory:
            output = Path(directory) / "open-prs.csv"
            with patch(
                "scripts.audit_open_prs._gh_api", side_effect=[pull_requests, files]
            ) as gh_api:
                exit_code = main(
                    ["--repo", "example/repo", "--output", str(output)]
                )

            self.assertEqual(0, exit_code)
            self.assertTrue(output.is_file())
            self.assertIn("pending-review", output.read_text(encoding="utf-8"))
            self.assertEqual(2, gh_api.call_count)


if __name__ == "__main__":
    unittest.main()
