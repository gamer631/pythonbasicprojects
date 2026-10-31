# Rock, paper, scissors
# Step 1: ask the user for a choice
# Step 2: let the computer choose
# Step 3: compare choices and print result

import random

choices = ['rock', 'paper', 'scissors']

player = input("Enter rock, paper, or scissors: ").lower()
computer = random.choice(choices)

print("Computer chose:", computer)

if player == computer:
    print("It is a tie!")
elif (player == 'rock' and computer == 'scissors') or (player == 'paper' and computer == 'rock') or (player == 'scissors' and computer == 'paper'):
    print("You win!")
else:
    print("Computer wins!")
