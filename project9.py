# Temperature converter
# Step 1: ask the user for a temperature
# Step 2: ask the unit
# Step 3: convert and print result

value = float(input("Enter a temperature value: "))
unit = input("Enter C for Celsius or F for Fahrenheit: ").upper()

if unit == 'C':
    result = (value * 9 / 5) + 32
    print("Temperature in Fahrenheit:", result)
elif unit == 'F':
    result = (value - 32) * 5 / 9
    print("Temperature in Celsius:", result)
else:
    print("Invalid unit.")
