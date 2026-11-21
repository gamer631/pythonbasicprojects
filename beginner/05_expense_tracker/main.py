"""Record expenses and summarize totals by category."""
import json
from pathlib import Path
from datetime import date

DATA_FILE = Path(__file__).with_name("expenses.json")


def read_data() -> list[dict]:
    if DATA_FILE.exists():
        try: return json.loads(DATA_FILE.read_text(encoding="utf-8"))
        except json.JSONDecodeError: print("Couldn't read saved expenses; using a fresh list.")
    return []



def main() -> None:
    expenses = read_data()
    while True:
        print("\nExpenses | 1 Add | 2 Summary | 3 List | 0 Quit")
        choice = input("Select: ").strip()
        if choice == "1":
            category = input("Category: ").strip() or "Other"
            note = input("Note: ").strip()
            try: amount = float(input("Amount (NPR): "))
            except ValueError: print("Enter an amount as a number."); continue
            if amount <= 0: print("Amount must be greater than zero."); continue
            expenses.append({"date": date.today().isoformat(), "category": category, "note": note, "amount": amount})
            DATA_FILE.write_text(json.dumps(expenses, indent=2), encoding="utf-8")
            print("Expense saved.")
        elif choice == "2":
            totals = {}
            for item in expenses: totals[item["category"]] = totals.get(item["category"], 0) + item["amount"]
            print("\nSpending by category:")
            for category, total in sorted(totals.items()): print(f"{category}: NPR {total:.2f}")
            print(f"Total: NPR {sum(i['amount'] for i in expenses):.2f}")
        elif choice == "3":
            for item in expenses: print(f"{item['date']} | {item['category']} | NPR {item['amount']:.2f} | {item['note']}")
            if not expenses: print("Nothing recorded yet.")
        elif choice == "0": break
        else: print("Pick 0, 1, 2, or 3.")


if __name__ == "__main__":
    main()
