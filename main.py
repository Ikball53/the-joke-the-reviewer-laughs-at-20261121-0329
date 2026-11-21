"""Emit the competition one-liner to the sandbox output slot.

The grader reads exactly one UTF-8 line from /output/entry.txt, so this
script keeps a single constant, makes sure the folder exists, and writes
the bytes with no extra decoration.
"""

from pathlib import Path

# One line, reviewer angle: the laugh is in the last clause.
LINE = "Reviewing my AI agent is easy: every bug arrives with a passing test proving it was intended behavior all along."


def emit() -> None:
    # Stay inside the 1..280 code-point window the rules demand.
    assert 1 <= len(LINE) <= 280 and "\n" not in LINE
    target = Path("/output/entry.txt")
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(LINE, encoding="utf-8")


if __name__ == "__main__":
    emit()
