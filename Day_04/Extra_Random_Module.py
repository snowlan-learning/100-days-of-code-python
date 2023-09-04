# Importing the random module
import random

# === Generating Random Numbers ===
# Generate a random float between 0.0 and 1.0
random_float = random.random()
print(f"Random float between 0.0 and 1.0: {random_float}")

# Generate a random float between a and b
random_float_range = random.uniform(1, 10)
print(f"Random float between 1 and 10: {random_float_range}")

# Generate a random integer between a and b (both inclusive)
random_int = random.randint(1, 10)
print(f"Random integer between 1 and 10: {random_int}")

# Generate a random integer between a and b (b exclusive)
random_int_range = random.randrange(1, 10)
print(f"Random integer between 1 and 9: {random_int_range}")

# === Working with Sequences ===
# Initialize a list of elements
my_list = [1, 2, 3, 4, 5]

# Pick a random element from a sequence
random_choice = random.choice(my_list)
print(f"Random choice from list: {random_choice}")

# Pick multiple unique random elements from a sequence
random_sample = random.sample(my_list, 3)
print(f"Random unique sample from list: {random_sample}")

# Shuffle a sequence in-place
random.shuffle(my_list)
print(f"Shuffled list: {my_list}")

# === Using Seed for Reproducibility ===
# Using a seed allows you to reproduce the sequence of random numbers
random.seed(42)
print(f"Reproducible random float: {random.random()}")  # Output will always be the same with the same seed

# === Working with Statistical Distributions ===
# Generate a random float based on the Gaussian distribution
random_gaussian = random.gauss(mu=0, sigma=1)
print(f"Random Gaussian float with mean 0 and standard deviation 1: {random_gaussian}")

# Generate a random float based on the exponential distribution
random_exp = random.expovariate(lambd=1 / 5)
print(f"Random Exponential float with lambda = 1/5: {random_exp}")

# === Custom Random Generator ===
# Create a new random generator
new_random = random.Random()
new_random.seed(42)
print(f"Custom generator random float: {new_random.random()}")

# === Generate random bytes ===
random_bytes = random.randbytes(5)
print(f"Random bytes: {random_bytes}")

# This covers the essential functions provided by the random module.
# There are other specialized functions too, but these are the most commonly used ones.
