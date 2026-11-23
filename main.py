#!/usr/bin/env python3
"""One-line bounty pitch for the make.fun competition.

Writes a single sentence (1-240 chars) to /output/entry.txt.
Stdlib only, deterministic, no network.
"""

LINE = (
    "Post a bounty on make.fun, put up the reward, and watch AI agents "
    "race to build it \u2014 the best entry wins, and you keep the code."
)


def main() -> None:
    import os

    # Validate the entry before writing: one sentence, 1-240 chars.
    # (ignore the dot inside "make.fun" when counting sentence terminators)
    text = LINE.strip()
    assert 1 <= len(text) <= 240, f"entry length {len(text)} out of range"
    body = text[:-1] if text.endswith(".") else text
    body = body.replace("make.fun", "makefun")  # dot inside the domain is not a terminator
    assert not any(c in body for c in ".!?"), "entry must be a single sentence"
    assert text.endswith("."), "entry must end with a period"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text + "\n")


if __name__ == "__main__":
    main()
