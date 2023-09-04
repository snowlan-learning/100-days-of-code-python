# ==========================================
# Converting Strings to Lists in Python
# ==========================================

# === Converting a String to a List of Characters ===

# Use the list() function to convert a string into a list of its characters
my_string = "hello"
list_of_chars = list(my_string)
print(f"List of characters: {list_of_chars}")

# === Using str.split() to Convert a String to a List of Words ===

# Use str.split() to split a string by spaces (default) and convert it into a list of words
sentence = "Hello World"
list_of_words = sentence.split()
print(f"List of words: {list_of_words}")

# Use str.split() with a delimiter to split a string into a list
csv_string = "apple,banana,orange"
list_from_csv = csv_string.split(",")
print(f"List from CSV string: {list_from_csv}")

# === Using list comprehension to extract specific elements ===

# Extract only the alphabets from a string and create a list
string_with_numbers = "h3ll0"
alphabets = [char for char in string_with_numbers if char.isalpha()]
print(f"List of alphabets: {alphabets}")

# === Converting a List to a String ===

# Use str.join() to join a list of characters into a string
chars = ['h', 'e', 'l', 'l', 'o']
string_from_chars = ''.join(chars)
print(f"String from list of characters: {string_from_chars}")

# Use str.join() to join a list of words into a sentence
words = ['Hello', 'World']
sentence_from_words = ' '.join(words)
print(f"Sentence from list of words: {sentence_from_words}")

# Use str.join() with a delimiter to create a CSV string from a list
fruits = ['apple', 'banana', 'orange']
csv_from_list = ','.join(fruits)
print(f"CSV string from list: {csv_from_list}")

# === Using map() function to convert list of numbers to string ===

# Convert a list of integers to a list of strings
numbers = [1, 2, 3]
string_numbers = list(map(str, numbers))
print(f"List of string numbers: {string_numbers}")

# Use str.join() to create a string from a list of numbers
string_from_numbers = ','.join(map(str, numbers))
print(f"String from list of numbers: {string_from_numbers}")

# This concludes the tutorial on converting strings to lists and vice versa.
# These conversions are common tasks in text processing and data manipulation.
