# Program Purpose: To calculate and display the number of characters in a user-provided name.
# The program leverages Python's built-in input() function for data collection and len() function for calculation.

# Step 1: Gather the User's Name
# Use the input() function to display a prompt "What is your name?" and collect the user's input.
# Store the user's input in a variable called 'name'.
name = input("What is your name? ")

# Step 2: Compute the Length of the Name
# Utilize the len() function to measure the number of characters in the 'name' string.
# len() returns an integer representing the length of the string.

# Step 3: Output the Result
# Employ the print() function to display the calculated length of the user's name.
print(len(name))

# Alternative One-Liner Solution
# The same functionality can be achieved in a single line by nesting the input() and len() functions within the print() function.
print(len(input("What is your name? ")))