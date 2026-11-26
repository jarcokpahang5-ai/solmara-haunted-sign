"""Funniest sign on a haunted server room door.

Writes the sign text (one line) to /output/entry.txt and prints it.
Pure Python 3 standard library, deterministic, no network, self-contained.
"""

import os

LINE = "WARNING: This server room is haunted. The ghost in rack 7 has root access and keeps changing every password to \"BOO\"."


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE + "\n")
    print(LINE)


if __name__ == "__main__":
    main()
