# Number guessing game
# Step 1: choose a random number
# Step 2: ask the user to guess
# Step 3: give hints until the user wins

import random

secret_number = random.randint(1, 10)
print("I am thinking of a number between 1 and 10.")

for attempt in range(1, 4):
    guess = int(input("Guess the number: "))
    if guess == secret_number:
        print("You win!")
        break
    elif guess < secret_number:
        print("Too low. Try again.")
    else:
        print("Too high. Try again.")

print("The number was:", secret_number)
