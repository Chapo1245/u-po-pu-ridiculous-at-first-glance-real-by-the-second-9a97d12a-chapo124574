#!/usr/bin/env python3
"""Write one bizarre-but-real startup pitch to /output/entry.txt.

The pitch: pothole naming rights. Furious drivers pay to name the crater
that ate their tyre; the city spends the fee filling it. The joke funds
its own punchline, which is why the business logic holds.
"""

import os

ENTRY = (
    "We sell naming rights to potholes: furious drivers pay $49 to name "
    "the crater that ate their tyre, and the city uses the fee to finally "
    "fill it."
)


def main() -> None:
    # The gate allows 1 to 200 characters; keep the entry one sentence.
    assert 1 <= len(ENTRY) <= 200, len(ENTRY)
    assert ENTRY.count(".") == 1 and ENTRY.endswith(".")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="\n") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
