"""Print a grade report table. Usage: python -m gradebook.cli scores.csv"""
import sys

from rich.console import Console
from rich.table import Table

from gradebook.core import parse_line, average, grade


def main() -> None:
    path = sys.argv[1] if len(sys.argv) > 1 else "scores.csv"
    with open(path) as f:
        rows = [parse_line(line) for line in f if line.strip()]

    table = Table(title="Grade Report")
    table.add_column("Name")
    table.add_column("Score")
    table.add_column("Grade")
    for name, score in rows:
        table.add_row(name, str(score), grade(score))

    console = Console()
    console.print(table)
    console.print(f"Class average: {average([s for _, s in rows]):.1f}")


if __name__ == "__main__":
    main()
