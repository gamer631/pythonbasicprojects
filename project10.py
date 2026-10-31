# Hangman game
# Step 1: choose a word
# Step 2: show blanks
# Step 3: ask for letters until the word is guessed

word = 'python'
letters = set(word)
guessed = set()

print("Guess the word. It has 6 letters.")

while letters - guessed:
    for letter in word:
        if letter in guessed:
            print(letter, end=' ')
        else:
            print('_', end=' ')
    print()

    guess = input("Enter a letter: ").lower()
    guessed.add(guess)

    if guess not in word:
        print("Wrong letter.")

print("You win! The word is python.")
