# Simple ATM
# Step 1: start with a balance
# Step 2: show menu
# Step 3: let the user deposit or withdraw

balance = 1000

while True:
    print("\n1. Check balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Exit")
    choice = input("Choose an option: ")

    if choice == '1':
        print("Your balance is:", balance)
    elif choice == '2':
        amount = float(input("Enter amount to deposit: "))
        balance = balance + amount
        print("Deposit successful.")
    elif choice == '3':
        amount = float(input("Enter amount to withdraw: "))
        if amount <= balance:
            balance = balance - amount
            print("Withdrawal successful.")
        else:
            print("Not enough money.")
    elif choice == '4':
        print("Goodbye!")
        break
    else:
        print("Invalid choice.")
