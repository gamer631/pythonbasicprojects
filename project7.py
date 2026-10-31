# Dice roller
# Step 1: roll a random number
# Step 2: print it
# Step 3: repeat if the user wants

import random

again = 'y'
while again == 'y':
    number = random.randint(1, 6)
    print("You rolled:", number)
    again = input("Roll again? (y/n): ").lower()

print("Thanks for playing!")
