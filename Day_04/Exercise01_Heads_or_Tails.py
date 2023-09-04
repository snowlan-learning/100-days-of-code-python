# Import the Python standard library module 'random'
# This enables us to use various random number generation functions.
import random

# Generate a random integer between 1 and 2.
# In this case, 1 represents 'Heads' and 2 represents 'Tails'.
random_number = random.randint(1, 2)

# Check the value of the generated random number.
# If the random number is 1, print "Heads".
# Otherwise, print "Tails".
if random_number == 1:
    print("Heads")
else:
    print("Tails")