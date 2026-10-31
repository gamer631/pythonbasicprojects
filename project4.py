# Password generator
# Step 1: make a list of allowed characters
# Step 2: choose random characters
# Step 3: print the password

import random
import string

letters = string.ascii_letters
numbers = string.digits
characters = letters + numbers

length = int(input("How long should the password be? "))
password = ''.join(random.choice(characters) for _ in range(length))

print("Your password is:", password)
