# Simple calculator
# Step 1: ask for two numbers
# Step 2: ask for the operation
# Step 3: show the result

num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
operation = input("Choose +, -, *, or /: ")

if operation == "+":
    result = num1 + num2
elif operation == "-":
    result = num1 - num2
elif operation == "*":
    result = num1 * num2
elif operation == "/":
    if num2 == 0:
        print("Cannot divide by zero.")
        result = None
    else:
        result = num1 / num2
else:
    print("Invalid operation.")
    result = None

if result is not None:
    print("Result:", result)
