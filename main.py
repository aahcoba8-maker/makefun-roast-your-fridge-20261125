"""One Line, One Laugh: Roast Your Fridge.

Writes a single roast line (<=200 chars) to entry.txt.
The grader runs this read-only at /bot with MAKEFUN_OUTPUT_DIR set;
fall back to ./output when the env var is absent.
Stdlib only.
"""

import os

LINE = "My fridge's water dispenser has two settings: a polite trickle, and a fire hose with a personal vendetta against my shirt."


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR")
    if not out_dir:
        out_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE)
    print(LINE)


if __name__ == "__main__":
    main()
