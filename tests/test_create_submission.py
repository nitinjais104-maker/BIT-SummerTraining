import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

from scripts.create_submission import additional_required_files, create_submission


class CreateSubmissionTests(unittest.TestCase):
    def test_creates_solution_in_the_canonical_folder(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)

            solution = create_submission(root, day=5, batch="b", name="Rahul-Singh")

            self.assertEqual(
                root
                / "assignments"
                / "day-05"
                / "submissions"
                / "batch-b"
                / "Rahul-Singh"
                / "solution.py",
                solution,
            )
            self.assertIn("Day 05", solution.read_text(encoding="utf-8"))

    def test_lists_assignment_specific_additional_files(self):
        self.assertEqual(("sales_data.csv",), additional_required_files(7))
        self.assertEqual(
            (
                "monthly_sales_line.png",
                "students_by_course_bar.png",
                "course_enrollment_pie.png",
                "study_hours_scatter.png",
                "course_growth.png",
            ),
            additional_required_files(10),
        )
        self.assertEqual(
            (
                "course_count.png",
                "average_marks_bar.png",
                "study_hours_marks_scatter.png",
                "marks_boxplot.png",
                "marks_histogram.png",
                "student_correlation_heatmap.png",
            ),
            additional_required_files(11),
        )
        self.assertEqual((), additional_required_files(5))

    def test_refuses_to_overwrite_an_existing_student_folder(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            existing = (
                root
                / "assignments"
                / "day-05"
                / "submissions"
                / "batch-a"
                / "rahul"
            )
            existing.mkdir(parents=True)
            marker = existing / "notes.txt"
            marker.write_text("keep me", encoding="utf-8")

            with self.assertRaises(FileExistsError):
                create_submission(root, day=5, batch="a", name="rahul")

            self.assertEqual("keep me", marker.read_text(encoding="utf-8"))

    def test_rejects_invalid_day_batch_and_student_name(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            invalid_inputs = (
                {"day": 0, "batch": "a", "name": "rahul"},
                {"day": 15, "batch": "a", "name": "rahul"},
                {"day": 5, "batch": "c", "name": "rahul"},
                {"day": 5, "batch": "a", "name": "Rahul Singh"},
                {"day": 5, "batch": "a", "name": "../rahul"},
            )

            for values in invalid_inputs:
                with self.subTest(values=values), self.assertRaises(ValueError):
                    create_submission(root, **values)

    def test_cli_creates_solution_and_prints_remaining_files(self):
        script = Path(__file__).parents[1] / "scripts" / "create_submission.py"
        with tempfile.TemporaryDirectory() as directory:
            result = subprocess.run(
                [
                    sys.executable,
                    str(script),
                    "--day",
                    "7",
                    "--batch",
                    "b",
                    "--name",
                    "student-name",
                ],
                cwd=directory,
                check=False,
                capture_output=True,
                text=True,
            )

            self.assertEqual(0, result.returncode)
            self.assertIn(
                "assignments/day-07/submissions/batch-b/student-name/solution.py",
                result.stdout,
            )
            self.assertIn("sales_data.csv", result.stdout)
            self.assertTrue(
                (
                    Path(directory)
                    / "assignments/day-07/submissions/batch-b/student-name/solution.py"
                ).is_file()
            )


if __name__ == "__main__":
    unittest.main()
