"""One-line office joke entry for make.fun.

Writes the entry text to /output/entry.txt.
"""

import os

ENTRY = "Our printer has one job and refuses to do it, so HR gave it a promotion."


def main():
    if not 1 <= len(ENTRY) <= 200:
        raise ValueError("entry must be 1-200 characters")
    if not ENTRY.strip():
        raise ValueError("entry must not be only whitespace")
    if ENTRY != ENTRY.strip():
        raise ValueError("entry must not start or end with whitespace")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
