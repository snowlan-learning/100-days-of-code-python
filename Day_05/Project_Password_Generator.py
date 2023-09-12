# Password Generator Project
import random

# Lists containing characters for generating the password
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

# Introduction and user input for password customization
print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input("How many symbols would you like?\n"))
nr_numbers = int(input("How many numbers would you like?\n"))

# Generating specified number of letters, symbols, and numbers for the password
list_of_letters = [random.choice(letters) for _ in range(nr_letters)]
list_of_symbols = [random.choice(symbols) for _ in range(nr_symbols)]
list_of_numbers = [random.choice(numbers) for _ in range(nr_numbers)]

# Merging lists and shuffling to create a randomized password
password_list = list_of_letters + list_of_symbols + list_of_numbers
random.shuffle(password_list)

# Converting the list into a string
password = ''.join(password_list)

print(password)
