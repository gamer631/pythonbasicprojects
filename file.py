# This is a simple Python project that demonstrates basic functionality
# The project is making use of basic variables,loops, and functions , datatypes, to preform a simple task.
# This script is designed to take a list of numbers and return the sum of all even numbers in that list.
def sum_even_numbers(numbers): #defining a function that takes a list of numbers as input
    total = 0 # This variable is used to store the sum of even numbers
    for n in numbers: # for n in numbers: # iterating through each number in the list
        if n % 2 == 0: # checking if the number is even
            total += n # This total variable is used to accumulate the sum of even numbers
    return total # return the total sum of even numbers
print(sum_even_numbers([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])) # calling the function and printing the result