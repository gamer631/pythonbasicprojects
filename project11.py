# BMI calculator
# Step 1: ask for weight
# Step 2: ask for height
# Step 3: calculate BMI and print result

weight = float(input("Enter your weight in kilograms: "))
height = float(input("Enter your height in meters: "))

bmi = weight / (height * height)
print("Your BMI is:", bmi)

if bmi < 18.5:
    print("You are underweight.")
elif bmi < 25:
    print("You are healthy.")
elif bmi < 30:
    print("You are overweight.")
else:
    print("You are obese.")
