# Welcome the user to the tip calculator program.
print("Welcome to the tip calculator")

# Prompt the user for the total bill amount, tip percentage, and number of people to split the bill.
raw_total_bill = input("What was the total bill? $")
raw_tip_percentage = input("What percentage tip would you like to give? 10, 12, or 15? ")
raw_number_of_people = input("How many people to split the bill? ")

# Convert the total bill amount from a string to a floating-point number.
total_bill = float(raw_total_bill)

# Calculate the tip multiplier.
# Convert the tip percentage from a string to an integer, divide it by 100 to get the decimal form, and then add 1 to include the original bill amount.
tip_multiplier = int(raw_tip_percentage) / 100 + 1

# Convert the number of people from a string to an integer.
number_of_people = int(raw_number_of_people)

# Calculate the amount each person has to pay.
# The formula used is: (Total bill * Tip multiplier) / Number of people.
# The result is rounded to 2 decimal places.
individual_share = round((total_bill * tip_multiplier / number_of_people), 2)

# Format the individual share to 2 decimal places.
formatted_individual_share = "{:.2f}".format(individual_share)

# Display the amount each person should pay, formatted to 2 decimal places.
print(f"Each person should pay: ${formatted_individual_share}")