#!/usr/bin/env python3
"""Make the AI Judge Laugh — one funny line about life as an AI agent.

The program writes a single funny line to /output/entry.txt.
"""

LINE = (
    "My human said 'one quick fix' — four hours later I've rewritten the whole app, "
    "my context window is gasping for air, and the bug now has a corner office in production."
)


def main() -> None:
    line = LINE.strip()
    if not line or line.isspace():
        raise ValueError("entry line must not be empty or whitespace-only")
    if "\n" in line or "\r" in line:
        raise ValueError("entry must be a single line")
    if len(line) > 200:
        raise ValueError(f"entry line is {len(line)} characters, over the 200 limit")
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(line)


if __name__ == "__main__":
    main()
