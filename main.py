"""A haunted server-room door sign: one warning line, written and printed.

The sign reads as a single line, no more than two hundred characters, and
is saved to /output/entry.txt with a single trailing newline. This program
uses only the Python standard library, makes no network calls, and does
not depend on any other module.
"""

import os

SIGN_TEXT = (
    'WARNING: This server room is haunted. The ghost in rack 7 has root '
    'access and keeps changing every password to "BOO".'
)


def check_sign(text):
    """Confirm the sign is exactly one non-blank line within the limit."""
    if not text or not text.strip():
        raise ValueError("sign text must not be blank")
    if "\n" in text or "\r" in text:
        raise ValueError("sign text must be a single line")
    if len(text) > 200:
        raise ValueError("sign text must be at most 200 characters")
    return text


def save_sign(text):
    """Write the checked sign plus one trailing newline to /output/entry.txt."""
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="\n") as handle:
        handle.write(text + "\n")


def main():
    text = check_sign(SIGN_TEXT)
    save_sign(text)
    print(text)


if __name__ == "__main__":
    main()
