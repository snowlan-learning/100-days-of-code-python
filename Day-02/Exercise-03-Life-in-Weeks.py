# This program calculates the time left (in days, weeks, and months) 
# if a person lives up to 90 years old. It uses basic arithmetic operations 
# and f-strings for output formatting.

# Note: The following assumptions are made in this program:
# - There are 365 days in a year.
# - There are 52 weeks in a year.
# - There are 12 months in a year.

# Get the user's current age as input.
# Note: The input is received as a string and needs to be converted to an integer.
age = input("What is your current age? ")

# Convert the age from string to integer and calculate the years until 90.
years_until_90 = 90 - int(age)

# Calculate the number of months left until 90 years old.
months_until_90 = years_until_90 * 12

# Calculate the number of weeks left until 90 years old.
weeks_until_90 = years_until_90 * 52

# Calculate the number of days left until 90 years old.
days_until_90 = years_until_90 * 365

# Display the calculated time left in days, weeks, and months using f-strings.
print(f"You have {days_until_90} days, {weeks_until_90} weeks, and {months_until_90} months left.")