# Program to Determine if a Number is Odd or Even
# This program prompts the user for a number and then determines
# if it's an odd or even number based on whether it's divisible by 2 without a remainder.

# Note on Even Numbers:
# An even number can be evenly divided by 2 without leaving a remainder.
# Example: 86 is even because 86 ÷ 2 = 43 with no remainder.

# Note on Odd Numbers:
# An odd number leaves a remainder when divided by 2.
# Example: 59 is odd because 59 ÷ 2 = 29.5 (i.e., there's a remainder).

# Prompt user for a number to check.
# Note: Input returns a string, so it's converted to an integer for arithmetic operations.
number = int(input("Which number do you want to check? "))

# Use the modulus operator (%) to find the remainder when the number is divided by 2.
# If the remainder is 0, the number is even. Otherwise, it's odd.
if number % 2 == 0:
    print(f"{number} is an Even number")
else:
    print(f"{number} is an Odd number")