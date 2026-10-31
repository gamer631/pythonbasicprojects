# Expense tracker
# Step 1: create an empty list
# Step 2: add items with prices
# Step 3: show total cost

expenses = []

while True:
    print("\n1. Add expense")
    print("2. Show total")
    print("3. Exit")
    choice = input("Choose an option: ")

    if choice == '1':
        item = input("Enter item name: ")
        price = float(input("Enter price: "))
        expenses.append((item, price))
        print("Expense added.")
    elif choice == '2':
        total = 0
        for item, price in expenses:
            total += price
        print("Total expenses:", total)
    elif choice == '3':
        print("Goodbye!")
        break
    else:
        print("Invalid choice.")
