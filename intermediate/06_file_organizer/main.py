"""Organize a directory by file extension, with a preview before moving."""
import argparse
import shutil
from pathlib import Path



def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("folder", type=Path, help="folder to organize")
    args = parser.parse_args()
    root = args.folder.expanduser().resolve()
    if not root.is_dir():
        parser.error("the path must be an existing directory")
    moves = []
    for item in root.iterdir():
        if item.is_file():
            category = item.suffix.lower().lstrip(".") or "no_extension"
            destination = root / category
            target = destination / item.name
            if target.exists():
                print(f"Skipping collision: {target}")
                continue
            moves.append((item, target))
    if not moves:
        print("Nothing to organize.")
        return
    print("Preview:")
    for source, target in moves: print(f"{source.name} -> {target.parent.name}/{target.name}")
    if input(f"Move {len(moves)} files? Type YES to proceed: ") != "YES":
        print("No changes made."); return
    for source, target in moves:
        target.parent.mkdir(exist_ok=True)
        shutil.move(str(source), str(target))
    print("Done.")


if __name__ == "__main__":
    main()
