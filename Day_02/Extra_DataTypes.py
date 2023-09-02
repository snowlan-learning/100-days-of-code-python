# Python Data Types Explained

# -------------------------
# String Data Type (str)
# -------------------------

# Strings are sequences of characters enclosed in quotes.
# Python supports both single and double quotes.

# Accessing a character by index (Index starts from 0)
print("Character at index 4 of 'Hello':", "Hello"[4])  # Output will be 'o'

# String concatenation
print("Concatenation of '123' and '345':", "123" + "345")  # Output will be '123345'

# Advanced String Operations
# Converting string to uppercase
text = "hello"
print("Uppercase of 'hello':", text.upper())  # Output: 'HELLO'

# -------------------------
# Integer Data Type (int)
# -------------------------

# Integers are whole numbers, both positive and negative.

# Basic arithmetic operation (Addition)
print("Addition of 123 and 345:", 123 + 345)  # Output will be 468

# Subtracting a negative from a positive
print("Subtraction of -345 from 123:", 123 - (-345))  # Output will be 468

# Large Integers
# Python can handle integers of arbitrary size, limited only by available memory.
# Underscores can be used for readability
print("Large integer with underscores:", 123_456_789)  # Output will be 123456789

# -------------------------
# Floating-Point Data Type (float)
# -------------------------

# Floating-point numbers are real numbers that contain a decimal point.

# A float number
print("A float number:", 3.14159)  # Output will be 3.14159

# Arithmetic operations with float numbers
print("Addition of 4.2 and 2.3:", 4.2 + 2.3)  # Output will be 6.5

# Scientific Notation
# Python also supports scientific notation for floats
print("Scientific notation of 3.14e2:", 3.14e2)  # Output will be 314.0

# -------------------------
# Boolean Data Type (bool)
# -------------------------

# Booleans represent one of two values: True or False.

# A simple Boolean
print("A simple Boolean:", True)  # Output will be True

# Logical operations with Booleans
print("Logical AND between True and False:", True and False)  # Output will be False

# Usage in conditional statements
is_raining = True
if is_raining:
    print("Take an umbrella!")  # Output will be 'Take an umbrella!'
