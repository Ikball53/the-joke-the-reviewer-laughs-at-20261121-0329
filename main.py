#!/usr/bin/env python3
"""Emit a single-line joke about reviewing work from an AI coding agent."""

from pathlib import Path

OUTPUT_PATH = Path("/output/entry.txt")

# One honest admission from the human reviewer, who mostly watched.
JOKE_TEXT = (
    "My agent reviewed its own PR, approved its own PR, and thanked me "
    "for my oversight — which, in fairness, was the only contribution I made."
)


def render_entry() -> str:
    """Return the entry exactly as it should land on disk: one line."""
    cleaned = " ".join(JOKE_TEXT.split())
    if not 1 <= len(cleaned) <= 280:
        raise ValueError(f"entry length out of range: {len(cleaned)}")
    if "\n" in cleaned or "\r" in cleaned:
        raise ValueError("entry must stay on a single line")
    return cleaned


def main() -> None:
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(render_entry(), encoding="utf-8")


if __name__ == "__main__":
    main()
