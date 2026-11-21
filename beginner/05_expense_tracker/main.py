"""Record and summarize expenses in JSON."""
import json
from pathlib import Path
from datetime import date
FILE=Path(__file__).with_name('expenses.json')
def load():
    try: return json.loads(FILE.read_text(encoding='utf-8')) if FILE.exists() else []
    except json.JSONDecodeError: print('Data file was invalid; starting empty.'); return []
def main():
    rows=load()
    while True:
        print('\nExpense Tracker: 1 Add | 2 Summary | 3 List | 0 Exit')
        choice=input('> ').strip()
        if choice=='1':
            category=input('Category: ').strip() or 'Other'; note=input('Note: ').strip()
            try: amount=float(input('Amount (NPR): '))
            except ValueError: print('Amount must be numeric.'); continue
            if amount<=0: print('Amount must be positive.'); continue
            rows.append({'date':date.today().isoformat(),'category':category,'note':note,'amount':amount})
            FILE.write_text(json.dumps(rows,indent=2),encoding='utf-8'); print('Recorded.')
        elif choice=='2':
            totals={}
            for item in rows: totals[item['category']]=totals.get(item['category'],0)+item['amount']
            for name,total in sorted(totals.items()): print(f'{name}: NPR {total:.2f}')
            print(f'Overall: NPR {sum(x["amount"] for x in rows):.2f}')
        elif choice=='3':
            for x in rows: print(f'{x["date"]} | {x["category"]} | {x["amount"]:.2f} | {x["note"]}')
            if not rows: print('No expenses saved.')
        elif choice=='0': break
        else: print('Select a menu number.')
if __name__=='__main__': main()
