"""Small task list with priority and local JSON storage."""
import json
from pathlib import Path
from datetime import date
FILE=Path(__file__).with_name('tasks.json')
def load():
    try: return json.loads(FILE.read_text(encoding='utf-8')) if FILE.exists() else []
    except json.JSONDecodeError: print('Task file is damaged; starting empty.'); return []
def save(tasks): FILE.write_text(json.dumps(tasks,indent=2),encoding='utf-8')
def main():
    tasks=load()
    while True:
        print('\nTasks: 1 Add | 2 List | 3 Done | 4 Remove | 0 Exit')
        choice=input('> ').strip()
        if choice=='1':
            title=input('Task: ').strip(); priority=input('Priority (low/medium/high): ').strip().lower() or 'medium'; due=input('Due date (YYYY-MM-DD or blank): ').strip()
            if not title: print('Task name is required.'); continue
            if priority not in ('low','medium','high'): print('Priority must be low, medium, or high.'); continue
            if due:
                try: date.fromisoformat(due)
                except ValueError: print('Date format should be YYYY-MM-DD.'); continue
            tasks.append({'title':title,'priority':priority,'due':due,'done':False}); save(tasks); print('Added.')
        elif choice=='2':
            if not tasks: print('Nothing on your list.')
            for i,t in enumerate(tasks,1): print(f'{i}. {"[x]" if t["done"] else "[ ]"} {t["title"]} — {t["priority"]} — {t["due"] or "no due date"}')
        elif choice in ('3','4'):
            try: idx=int(input('Task number: '))-1
            except ValueError: print('Enter a number.'); continue
            if not 0<=idx<len(tasks): print('No task at that number.'); continue
            if choice=='3': tasks[idx]['done']=True; save(tasks); print('Marked done.')
            else: tasks.pop(idx); save(tasks); print('Removed.')
        elif choice=='0': break
        else: print('Choose a menu item.')
if __name__=='__main__': main()
