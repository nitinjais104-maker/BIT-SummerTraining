#!/usr/bin/env python3
"""Create a correctly located assignment submission folder."""

import argparse
import re
import sys
from pathlib import Path
from typing import Optional, Sequence, Tuple


STUDENT_NAME_PATTERN = re.compile(r"^[A-Za-z0-9][A-Za-z0-9_-]*$")
ADDITIONAL_FILES = {
    7: ("sales_data.csv",),
    10: (
        "monthly_sales_line.png",
        "students_by_course_bar.png",
        "course_enrollment_pie.png",
        "study_hours_scatter.png",
        "course_growth.png",
    ),
    11: (
        "course_count.png",
        "average_marks_bar.png",
        "study_hours_marks_scatter.png",
        "marks_boxplot.png",
        "marks_histogram.png",
        "student_correlation_heatmap.png",
    ),
}


def additional_required_files(day: int) -> Tuple[str, ...]:
    return ADDITIONAL_FILES.get(day, ())


def create_submission(root: Path, day: int, batch: str, name: str) -> Path:
    if day not in range(1, 15):
        raise ValueError("Day must be between 1 and 14.")
    if batch not in {"a", "b"}:
        raise ValueError("Batch must be 'a' or 'b'.")
    if STUDENT_NAME_PATTERN.fullmatch(name) is None:
        raise ValueError(
            "Student name must be one folder using only letters, numbers, '-' or '_'."
        )

    folder = (
        root
        / "assignments"
        / f"day-{day:02d}"
        / "submissions"
        / f"batch-{batch}"
        / name
    )
    folder.mkdir(parents=True, exist_ok=False)
    solution = folder / "solution.py"
    solution.write_text(
        f'"""Day {day:02d} assignment by {name}."""\n\n'
        "# Answer every question from questions.md below.\n",
        encoding="utf-8",
    )
    return solution


def main(argv: Optional[Sequence[str]] = None) -> int:
    parser = argparse.ArgumentParser(
        description="Create the correct folder and solution.py for one assignment."
    )
    parser.add_argument("--day", required=True, type=int, help="Assignment day (1-14).")
    parser.add_argument(
        "--batch", required=True, choices=("a", "b"), help="Student batch."
    )
    parser.add_argument("--name", required=True, help="Student folder name.")
    args = parser.parse_args(argv)

    try:
        solution = create_submission(Path.cwd(), args.day, args.batch, args.name)
    except (FileExistsError, ValueError) as error:
        print(f"Error: {error}", file=sys.stderr)
        return 1

    print(f"Created {solution}")
    remaining = additional_required_files(args.day)
    if remaining:
        print("You must also add these required files in the same folder:")
        for filename in remaining:
            print(f"- {filename}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
