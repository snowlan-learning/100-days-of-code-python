# Password Generator Project

# Importing required libraries
import random

# Defining possible letters for the password
letters = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n',
    'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
    'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N',
    'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'
]

# Defining possible numbers for the password
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

# Defining possible symbols for the password
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

# Welcoming user to the password generator
print("Welcome to the PyPassword Generator!")

# Getting user input for number of letters, symbols and numbers
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

# Eazy Level - Order not randomised:
# e.g. 4 letter, 2 symbol, 2 number = JduE&!91

# Hard Level - Order of characters randomised:
# e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P

# Creating an empty list to hold characters of the password
password_list = []

# Generating random letters based on user's preference
for n in range(0, nr_letters):
    random_letter_index = random.randint(0, len(letters) -1)
    password_list += [letters[random_letter_index]]

# Generating random symbols based on user's preference
for n in range(0, nr_symbols):
    random_symbol_index = random.randint(0, len(symbols) -1)
    password_list += [symbols[random_symbol_index]]

# Generating random numbers based on user's preference
for n in range(0, nr_numbers):
    random_number_index = random.randint(0, len(numbers) -1)
    password_list += [numbers[random_number_index]]

# Randomly shuffling the characters to make the password unpredictable
random.shuffle(password_list)

# Converting the shuffled list to a string to form the password
password = ''.join(password_list)

# Displaying the generated password
print(password)