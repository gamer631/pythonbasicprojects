"""Summarize level counts and frequent messages in a log file."""
import argparse
import re
from collections import Counter
from pathlib import Path
LEVEL_RE = re.compile(r"\b(DEBUG|INFO|WARNING|ERROR|CRITICAL)\b", re.IGNORECASE)



def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("logfile", type=Path)
    args = parser.parse_args()
    try: lines = args.logfile.read_text(encoding="utf-8", errors="replace").splitlines()
    except OSError as exc: parser.error(str(exc))
    levels = Counter()
    error_lines = []
    for line in lines:
        match = LEVEL_RE.search(line)
        if match:
            level = match.group(1).upper()
            levels[level] += 1
            if level in {"ERROR", "CRITICAL"}: error_lines.append(line)
    print(f"File: {args.logfile} | Lines: {len(lines)}")
    print("Level counts:")
    for level in ("DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"):
        print(f"  {level:<8} {levels[level]}")
    print("\nErrors and critical events:")
    for line in error_lines[:20]: print("  " + line)
    if len(error_lines) > 20: print(f"  ... {len(error_lines) - 20} more")


if __name__ == "__main__":
    main()
