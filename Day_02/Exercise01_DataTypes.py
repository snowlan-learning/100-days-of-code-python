# Purpose: This program calculates the sum of the digits in a two-digit number.
# For example, if the input is 35, the output will be "3 + 5 = 8".
# Note: Do not modify the lines designated for input collection (lines 1-3). The program should work for any two-digit number input.

# 🚨 Don't change the code below 👇
# Collecting user input for a two-digit number
two_digit_number = input("Type a two digit number: ")
# 🚨 Don't change the code above 👆

####################################
# Write your code below this line 👇

# Displaying the data type of the 'two_digit_number' variable to confirm it's a string
print(type(two_digit_number))

# Extracting the first and second digits from the input string
first_digit = two_digit_number[0]
second_digit = two_digit_number[1]

# Calculating the sum of the two digits
sumTotal = int(first_digit) + int(second_digit)

# Creating the output string to display the sum
output = f"{first_digit} + {second_digit} = {sumTotal}"

# Printing the output
print(output)