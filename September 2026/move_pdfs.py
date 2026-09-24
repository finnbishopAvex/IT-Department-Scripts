"""Move all PDF files from a source directory tree into a destination directory."""
import os
import shutil

def main():
    cwd = os.getcwd() 
    destination = os.path.dirname(os.path.abspath(__file__))
    os.makedirs(destination, exist_ok=True)

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
