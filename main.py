"""Emit the entry one-liner to the grader's output file.

The competition reads a single UTF-8 line from /output/entry.txt,
so this script writes exactly one joke there and nothing else.
"""

from pathlib import Path

# One line, reviewer angle: the laugh is in the final clause.
# Tightened wording: "changelog" up front, punchline on the summary.
ONE_LINER = (
    "My agent's changelog called it a minor tweak: forty-odd files, "
    "three new libraries, and a schema migration — the summary alone "
    "needed its own index."
)

TARGET = Path("/output/entry.txt")


def emit() -> None:
    """Write the one-liner, enforcing the single-line length window."""
    assert 1 <= len(ONE_LINER) <= 280, "joke outside the 1..280 window"
    assert "\n" not in ONE_LINER and "\r" not in ONE_LINER
    TARGET.parent.mkdir(parents=True, exist_ok=True)
    TARGET.write_text(ONE_LINER, encoding="utf-8")


if __name__ == "__main__":
    emit()
