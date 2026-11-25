"""A one-line roast of an app used every day.

Writes the roast to /output/entry.txt for make.fun's
"One-Line Roast: The Gadget You Use Every Day" bounty.
Stdlib only, deterministic, no network, no randomness.
"""

import os

LINE = (
    "CapCut crashes every time I export a video, then asks me to rate "
    "it five stars — like a waiter who dropped my food and wants a tip."
)


def main():
    # The sealed gate: /output/entry.txt must be UTF-8 text of
    # 1 to 200 characters, not only white space.
    text = LINE.strip()
    assert 1 <= len(text) <= 200, "line must be 1-200 characters"
    assert text.strip(), "line must not be only white space"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
