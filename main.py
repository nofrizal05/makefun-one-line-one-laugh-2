#!/usr/bin/env python3
"""One Line, One Laugh — make.fun entry (u-deysumbrella-one-line-one-laugh-e0cdcda9).

Writes a single original funny line to /output/entry.txt.
Standard library only. The joke: a smart fridge that diets-shames you
in front of the other appliances — the laugh lands on the last phrase.
"""

import os

LINE = (
    "I told my smart fridge I'm on a diet. "
    "It now judges my midnight snacks out loud, "
    "in front of the other appliances."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
