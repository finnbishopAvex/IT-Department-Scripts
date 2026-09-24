"""Move all PDF files from a source directory tree into a destination directory."""
import argparse
import os
import shutil
import sys


def main():
    parser = argparse.ArgumentParser(
        description="Recursively move all .pdf files from SOURCE (and its subfolders) into DESTINATION.")
    parser.add_argument("-s", "--source", required=True, help="base directory to search for PDFs")
    parser.add_argument("-d", "--destination", required=True, help="directory to move PDFs into")
    args = parser.parse_args()

    for label, path in (("Source", args.source), ("Destination", args.destination)):
        if not os.path.isdir(path):
            sys.exit(f"Error: {label} directory does not exist: {path}")

    moved = 0
    for root, _, files in os.walk(args.source):
        for name in files:
            if not name.lower().endswith(".pdf"):
                continue
            src = os.path.join(root, name)
            dst = os.path.join(args.destination, name)
            if os.path.exists(dst):
                print(f"Skipped (already exists): {dst}")
                continue
            shutil.move(src, dst)
            print(f"Moved: {src} -> {dst}")
            moved += 1

    print(f"Done. {moved} PDF(s) moved.")


if __name__ == "__main__":
    main()
