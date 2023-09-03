# Program to determine whether a given year is a leap year.
# Leap years have 366 days with an extra day in February.
# For an in-depth explanation of why leap years exist, see:
# https://www.youtube.com/watch?v=xX96xng7sAE

# Leap Year Criteria:
# - Must be divisible by 4
# - Must not be divisible by 100, unless it's also divisible by 400

# Examples:
# - 2000 is a leap year because it meets all criteria (divisible by 4, 100, and 400)
# - 2100 is not a leap year because it's divisible by 100 but not by 400

# Collect the year to check from the user and convert to an integer
year = int(input("Which year do you want to check? "))

# Calculate and determine if the given year is a leap year
# Apply the criteria for identifying leap years
if year % 4 != 0:
    print("Not leap year.")
elif year % 100 != 0:
    print("Leap year.")
elif year % 400 == 0:
    print("Leap year.")
else:
    print("Not leap year.")