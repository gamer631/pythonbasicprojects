"""A tiny JSON-backed contact book."""
import json
from pathlib import Path


DATA_FILE = Path(__file__).with_name("contacts.json")


def load_contacts() -> list[dict[str, str]]:
    if not DATA_FILE.exists():
        return []
    try:
        return json.loads(DATA_FILE.read_text(encoding="utf-8"))
    except json.JSONDecodeError:
        print("Contact file is damaged; starting with an empty list.")
        return []


def save_contacts(contacts: list[dict[str, str]]) -> None:
    DATA_FILE.write_text(json.dumps(contacts, indent=2), encoding="utf-8")


def main() -> None:
    contacts = load_contacts()
    while True:
        print("\nContact Book | 1 Add | 2 Search | 3 List | 4 Delete | 0 Exit")
        choice = input("Choose: ").strip()
        if choice == "1":
            name = input("Name: ").strip()
            phone = input("Phone: ").strip()
            if name and phone:
                contacts.append({"name": name, "phone": phone})
                save_contacts(contacts)
                print("Saved.")
            else:
                print("Both fields are required.")
        elif choice == "2":
            term = input("Search name: ").strip().casefold()
            found = [c for c in contacts if term in c["name"].casefold()]
            for c in found: print(f"{c['name']} — {c['phone']}")
            if not found: print("No matches.")
        elif choice == "3":
            for c in contacts: print(f"{c['name']} — {c['phone']}")
            if not contacts: print("No contacts yet.")
        elif choice == "4":
            name = input("Exact name to delete: ").strip().casefold()
            old_count = len(contacts)
            contacts = [c for c in contacts if c["name"].casefold() != name]
            if len(contacts) != old_count:
                save_contacts(contacts); print("Deleted.")
            else: print("No contact with that name.")
        elif choice == "0":
            break
        else:
            print("Please choose one of the listed options.")


if __name__ == "__main__":
    main()
