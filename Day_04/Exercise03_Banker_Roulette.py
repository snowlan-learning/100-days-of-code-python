# Import Python's built-in 'random' module for random number generation
import random

# Gather a comma-separated string of names from the user
names_string = input("Give me everybody's names, separated by a comma. ")

# Convert the comma-separated string into a list of names
# Each name becomes a separate element in the list
names = names_string.split(", ")

# Do not modify the code above this line

# Generate a random index to pick a name from the 'names' list
# The index is between 0 and the length of the list minus 1 (inclusive)
random_index = random.randint(0, (len(names) - 1))

# Use the random index to pick a name from the 'names' list and announce who will buy the meal
print(f"{names[random_index]} is going to buy the meal today!")