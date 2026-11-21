"""Simple local JSON contact book."""
import json
from pathlib import Path
FILE=Path(__file__).with_name('contacts.json')
def load():
    try: return json.loads(FILE.read_text(encoding='utf-8')) if FILE.exists() else []
    except json.JSONDecodeError: print('Save file unreadable; starting fresh.'); return []
def save(items): FILE.write_text(json.dumps(items,indent=2),encoding='utf-8')
def main():
    items=load()
    while True:
        print('\nContacts: 1 Add | 2 Search | 3 List | 4 Delete | 0 Exit')
        choice=input('> ').strip()
        if choice=='1':
            name=input('Name: ').strip(); phone=input('Phone: ').strip()
            if name and phone: items.append({'name':name,'phone':phone}); save(items); print('Saved.')
            else: print('Both values are required.')
        elif choice=='2':
            q=input('Name search: ').lower(); matches=[x for x in items if q in x['name'].lower()]
            for x in matches: print(x['name'],x['phone'])
            if not matches: print('No matches.')
        elif choice=='3':
            for x in items: print(x['name'],x['phone'])
            if not items: print('No contacts yet.')
        elif choice=='4':
            name=input('Exact name: ').casefold(); new=[x for x in items if x['name'].casefold()!=name]
            if len(new)!=len(items): items=new; save(items); print('Removed.')
            else: print('Not found.')
        elif choice=='0': break
        else: print('Choose a menu option.')
if __name__=='__main__': main()
