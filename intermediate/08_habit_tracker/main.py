"""A small date-based habit tracker."""
import json
from pathlib import Path
from datetime import date
DATA = Path(__file__).with_name("habits.json")


def load() -> dict:
    if DATA.exists():
        try: return json.loads(DATA.read_text(encoding="utf-8"))
        except json.JSONDecodeError: print("Save file is unreadable; starting over.")
    return {}


def main() -> None:
    records = load()
    while True:
        print("\nHabit Tracker | 1 Check in | 2 History | 0 Exit")
        choice = input("Choice: ").strip()
        if choice == "1":
            habit = input("Habit name: ").strip()
            if not habit: print("Name can't be empty."); continue
            records.setdefault(habit, [])
            today = date.today().isoformat()
            if today in records[habit]: print("Already checked in today.")
            else:
                records[habit].append(today)
                records[habit].sort()
                DATA.write_text(json.dumps(records, indent=2), encoding="utf-8")
                print("Check-in saved. Good job showing up.")
        elif choice == "2":
            habit = input("Habit to view: ").strip()
            days = records.get(habit, [])
            print(f"{habit}: {len(days)} total check-ins")
            for day in days[-14:]: print("  " + day)
        elif choice == "0": break
        else: print("Choose one of the menu options.")


if __name__ == "__main__":
    main()
