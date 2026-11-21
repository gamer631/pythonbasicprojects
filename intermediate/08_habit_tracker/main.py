"""Track habit check-ins with dates in a JSON file."""
import json
from pathlib import Path
from datetime import date
FILE=Path(__file__).with_name('habit_data.json')
def load():
    try: return json.loads(FILE.read_text(encoding='utf-8')) if FILE.exists() else {}
    except json.JSONDecodeError: print('Save data is corrupt; starting fresh.'); return {}
def main():
    habits=load()
    while True:
        print('\nHabit tracker: 1 Check-in | 2 History | 0 Exit')
        choice=input('> ').strip()
        if choice=='1':
            name=input('Habit: ').strip()
            if not name: print('Enter a habit name.'); continue
            dates=habits.setdefault(name,[]); today=date.today().isoformat()
            if today in dates: print('Already checked today.')
            else: dates.append(today); dates.sort(); FILE.write_text(json.dumps(habits,indent=2),encoding='utf-8'); print('Saved check-in!')
        elif choice=='2':
            name=input('Habit name: '); dates=habits.get(name,[])
            print(f'{len(dates)} total check-ins')
            for day in dates[-14:]: print(day)
        elif choice=='0': break
        else: print('Choose a valid menu item.')
if __name__=='__main__': main()
