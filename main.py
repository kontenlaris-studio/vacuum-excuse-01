"""The Robot Vacuum's Best Excuse entry: the sock attacked first."""

import os

JOKE = (
    "The sock was not an accident. It wore the rug like a disguise and "
    "charged at me. I ate it in self-defense, and I would do it again."
)


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(JOKE + "\n")
    print(f"wrote {path} ({len(JOKE)} characters)")


if __name__ == "__main__":
    main()
