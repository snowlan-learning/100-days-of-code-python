# Sum all of the even numbers 

# Initialize the sum to 0
total = 0

# Iterate over numbers from 1 to 100
for n in range(1, 101):
    # Add 1 to the total
    if n == 1:
        total += n
    # Add even numbers to the total
    if n % 2 == 0:
        total += n

# Print the total sum of 1 and even numbers
print(total)