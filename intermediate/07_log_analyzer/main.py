"""Count log levels in a text file and print error lines."""
import argparse, re
from collections import Counter
from pathlib import Path
PATTERN=re.compile(r'\b(DEBUG|INFO|WARNING|ERROR|CRITICAL)\b',re.I)
def main():
    parser=argparse.ArgumentParser(description=__doc__); parser.add_argument('logfile',type=Path); args=parser.parse_args()
    try: lines=args.logfile.read_text(encoding='utf-8',errors='replace').splitlines()
    except OSError as exc: parser.error(str(exc))
    counts=Counter(); errors=[]
    for line in lines:
        match=PATTERN.search(line)
        if match:
            level=match.group().upper(); counts[level]+=1
            if level in ('ERROR','CRITICAL'): errors.append(line)
    print(f'Lines scanned: {len(lines)}')
    for level in ('DEBUG','INFO','WARNING','ERROR','CRITICAL'): print(f'{level:8} {counts[level]}')
    print('\nError details:')
    for line in errors[:15]: print(line)
    if len(errors)>15: print(f'... and {len(errors)-15} more')
if __name__=='__main__': main()
