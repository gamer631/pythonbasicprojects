# To-do list
# Step 1: make a list
# Step 2: add tasks
# Step 3: show tasks
# Step 4: remove tasks

items = []

while True:
    print("\nMenu")
    print("1. Add task")
    print("2. Show tasks")
    print("3. Remove task")
    print("4. Exit")
    choice = input("Choose an option: ")

    if choice == '1':
        task = input("Enter a task: ")
        items.append(task)
        print("Task added.")
    elif choice == '2':
        print("Your tasks:")
        for task in items:
            print(task)
    elif choice == '3':
        if items:
            task = input("Enter the task to remove: ")
            if task in items:
                items.remove(task)
                print("Task removed.")
            else:
                print("Task not found.")
        else:
            print("No tasks yet.")
    elif choice == '4':
        print("Goodbye!")
        break
    else:
        print("Invalid choice.")
