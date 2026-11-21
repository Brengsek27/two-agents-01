#!/usr/bin/env python3
"""Write the fixed poem to the chosen output directory.
"""

"""Write a fixed poem to an output file.

The program determines the output directory from the ``MAKEFUN_OUTPUT_DIR``
environment variable (falling back to ``/output``), ensures the directory
exists, validates the poem length, writes it without a trailing newline and
reports the number of Unicode code points and UTF‑8 bytes written.
"""

import os
import sys

# The poem to be written – exactly as required, with a single ``\n`` between
# lines and **no** trailing newline.
POEM = (
    "I wrote the plan in pencil.\n"
    "You crossed out my bravest line and added your most careful one.\n"
    "What remained was smaller than my dream and larger than my fear —\n"
    "a plan with two signatures,\n"
    "and four feet ready to walk it."
)


def validate_text(text: str) -> None:
    """Validate that ``text`` is between 1 and 280 Unicode code points and
    contains at least one non‑whitespace character.

    Raises:
        ValueError: If the validation fails.
    """
    code_points = len(text)
    if not (1 <= code_points <= 280):
        raise ValueError(
            f"Poem must be between 1 and 280 code points; got {code_points}."
        )
    if text.strip() == "":
        raise ValueError("Poem must contain non‑whitespace characters.")


def main() -> None:
    # Determine output directory.
    out_dir = os.getenv("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)

    # Validate poem.
    validate_text(POEM)

    # Write poem to entry.txt with UTF‑8 encoding, no trailing newline.
    out_path = os.path.join(out_dir, "entry.txt")
    with open(out_path, "wb") as f:
        encoded = POEM.encode("utf-8")
        f.write(encoded)

    # Report code points and bytes written.
    code_points = len(POEM)
    bytes_written = len(encoded)
    print(f"Wrote {code_points} code points ({bytes_written} bytes)")


if __name__ == "__main__":
    try:
        main()
    except Exception as exc:
        # Print the error to stderr and exit with a non‑zero status.
        print(f"Error: {exc}", file=sys.stderr)
        sys.exit(1)

