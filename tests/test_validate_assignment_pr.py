import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

from scripts.validate_assignment_pr import validate_paths


class ValidateAssignmentPullRequestTests(unittest.TestCase):
    def test_accepts_one_solution_for_an_ordinary_day(self):
        for path in (
            "assignments/day-01/submissions/batch-a/student_one/solution.py",
            "assignments/day-14/submissions/batch-b/Student-Two/solution.py",
        ):
            with self.subTest(path=path):
                self.assertEqual([], validate_paths([path]))

    def test_accepts_day_7_solution_and_csv(self):
        errors = validate_paths(
            [
                "assignments/day-07/submissions/batch-a/rahul/solution.py",
                "assignments/day-07/submissions/batch-a/rahul/sales_data.csv",
            ]
        )

        self.assertEqual([], errors)

    def test_accepts_day_10_solution_and_five_charts(self):
        folder = "assignments/day-10/submissions/batch-b/rahul"
        errors = validate_paths(
            [
                f"{folder}/solution.py",
                f"{folder}/monthly_sales_line.png",
                f"{folder}/students_by_course_bar.png",
                f"{folder}/course_enrollment_pie.png",
                f"{folder}/study_hours_scatter.png",
                f"{folder}/course_growth.png",
            ]
        )

        self.assertEqual([], errors)

    def test_accepts_day_11_solution_and_six_charts(self):
        folder = "assignments/day-11/submissions/batch-a/rahul"
        errors = validate_paths(
            [
                f"{folder}/solution.py",
                f"{folder}/course_count.png",
                f"{folder}/average_marks_bar.png",
                f"{folder}/study_hours_marks_scatter.png",
                f"{folder}/marks_boxplot.png",
                f"{folder}/marks_histogram.png",
                f"{folder}/student_correlation_heatmap.png",
            ]
        )

        self.assertEqual([], errors)

    def test_rejects_an_empty_pull_request(self):
        self.assertEqual(["No changed files were provided."], validate_paths([]))

    def test_rejects_files_outside_assignment_submissions(self):
        errors = validate_paths(
            [
                "assignments/day-05/submissions/batch-a/rahul/solution.py",
                "CONTRIBUTING.md",
            ]
        )

        self.assertIn("CONTRIBUTING.md", "\n".join(errors))

    def test_rejects_multiple_days_batches_or_students(self):
        cases = (
            (
                [
                    "assignments/day-01/submissions/batch-a/rahul/solution.py",
                    "assignments/day-02/submissions/batch-a/rahul/solution.py",
                ],
                "one assignment day",
            ),
            (
                [
                    "assignments/day-01/submissions/batch-a/rahul/solution.py",
                    "assignments/day-01/submissions/batch-b/rahul/solution.py",
                ],
                "one batch",
            ),
            (
                [
                    "assignments/day-01/submissions/batch-a/rahul/solution.py",
                    "assignments/day-01/submissions/batch-a/priya/solution.py",
                ],
                "one student folder",
            ),
        )

        for paths, expected_message in cases:
            with self.subTest(paths=paths):
                self.assertIn(expected_message, "\n".join(validate_paths(paths)))

    def test_rejects_missing_and_unexpected_files(self):
        errors = validate_paths(
            ["assignments/day-07/submissions/batch-a/rahul/solution .py"]
        )
        message = "\n".join(errors)

        self.assertIn("Missing required files: sales_data.csv, solution.py", message)
        self.assertIn("Unexpected files: solution .py", message)

    def test_rejects_student_folder_with_spaces(self):
        errors = validate_paths(
            ["assignments/day-05/submissions/batch-a/Rahul Singh/solution.py"]
        )

        self.assertIn("Rahul Singh", "\n".join(errors))

    def test_rejects_duplicate_changed_paths(self):
        path = "assignments/day-05/submissions/batch-a/rahul/solution.py"

        self.assertIn("Duplicate changed path", "\n".join(validate_paths([path, path])))

    def test_cli_returns_success_for_valid_paths(self):
        result = self._run_cli(
            "assignments/day-05/submissions/batch-b/Rahul-Singh/solution.py\n"
        )

        self.assertEqual(0, result.returncode)
        self.assertIn("Assignment structure is valid.", result.stdout)

    def test_cli_returns_failure_and_preserves_filename_spaces(self):
        result = self._run_cli(
            "assignments/day-12/submissions/batch-b/AnkitaSingh/solution .py\n"
        )

        self.assertEqual(1, result.returncode)
        self.assertIn("solution .py", result.stderr)

    @staticmethod
    def _run_cli(contents):
        script = Path(__file__).parents[1] / "scripts" / "validate_assignment_pr.py"
        with tempfile.TemporaryDirectory() as directory:
            paths_file = Path(directory) / "changed-files.txt"
            paths_file.write_text(contents, encoding="utf-8")
            return subprocess.run(
                [sys.executable, str(script), "--paths-file", str(paths_file)],
                check=False,
                capture_output=True,
                text=True,
            )


if __name__ == "__main__":
    unittest.main()
