"""Sort files by extension. Preview first; confirm with exact YES to move."""
import argparse, shutil
from pathlib import Path
def main():
    parser=argparse.ArgumentParser(description=__doc__); parser.add_argument('folder',type=Path); args=parser.parse_args()
    folder=args.folder.expanduser().resolve()
    if not folder.is_dir(): parser.error('folder does not exist')
    moves=[]
    for f in folder.iterdir():
        if f.is_file():
            ext=f.suffix.lower().lstrip('.') or 'no_extension'; dest=folder/ext/f.name
            if dest.exists(): print(f'Skip duplicate destination: {dest}'); continue
            moves.append((f,dest))
    if not moves: print('Nothing to move.'); return
    for src,dst in moves: print(f'{src.name} -> {dst.parent.name}/{dst.name}')
    if input(f'Move {len(moves)} files? Type YES: ')!='YES': print('Cancelled.'); return
    for src,dst in moves: dst.parent.mkdir(exist_ok=True); shutil.move(str(src),str(dst))
    print('Files organized.')
if __name__=='__main__': main()
