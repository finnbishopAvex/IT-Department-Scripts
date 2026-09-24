"""Move all PDF files from a source directory tree into a destination directory."""
import os
import shutil
import sys


def main():
    cwd = os.getcwd() 
    os.mkdir(os.path.join(cwd, "moved_pdfs"))
    destination = os.path.join(cwd, "moved_pdfs")

    moved = 0
    for root, _, files in os.walk(cwd):
        for name in files:
            if not name.lower().endswith(".pdf"):
                continue
            src = os.path.join(root, name)
            dst = os.path.join(destination, name)
            if os.path.exists(dst):
                print(f"Skipped (already exists): {dst}")
                continue
            shutil.move(src, dst)
            print(f"Moved: {name}")
            moved += 1

    print(f"Done. {moved} PDF(s) moved.")


if __name__ == "__main__":
    main()
