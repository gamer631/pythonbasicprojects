# Quiz game
# Step 1: make questions and answers
# Step 2: ask each question
# Step 3: count the score

score = 0

print("Welcome to the quiz!")

answer1 = input("What is 2 + 2? ")
if answer1 == '4':
    print("Correct!")
    score += 1
else:
    print("Wrong. The answer is 4.")

answer2 = input("What is the capital of France? ").lower()
if answer2 == 'paris':
    print("Correct!")
    score += 1
else:
    print("Wrong. The answer is Paris.")

answer3 = input("Which animal says moo? ").lower()
if answer3 == 'cow':
    print("Correct!")
    score += 1
else:
    print("Wrong. The answer is cow.")

print("Your score is:", score)
