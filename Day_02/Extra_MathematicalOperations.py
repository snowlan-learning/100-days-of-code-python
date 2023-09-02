# Python Mathematical Operations Explained

# ------------------------------
# Basic Arithmetic Operations
# ------------------------------

# Addition
addition_result = 5 + 3
print(f"Addition: 5 + 3 = {addition_result}")

# Subtraction
subtraction_result = 10 - 4
print(f"Subtraction: 10 - 4 = {subtraction_result}")

# Multiplication
multiplication_result = 6 * 7
print(f"Multiplication: 6 * 7 = {multiplication_result}")

# Division (Float)
division_result = 8 / 3
print(f"Division (Float): 8 / 3 = {division_result}")

# Division (Integer)
integer_division_result = 8 // 3
print(f"Division (Integer): 8 // 3 = {integer_division_result}")

# Remainder
remainder_result = 10 % 3
print(f"Remainder: 10 % 3 = {remainder_result}")

# Exponentiation
exponentiation_result = 2 ** 3
print(f"Exponentiation: 2 ** 3 = {exponentiation_result}")

# ------------------------------
# Advanced Mathematical Functions
# ------------------------------

# Python's math library offers more advanced mathematical functions.
# You need to import the math library to access these functions.

import math

# Square Root
square_root_result = math.sqrt(16)
print(f"Square Root: sqrt(16) = {square_root_result}")

# Factorial
factorial_result = math.factorial(5)
print(f"Factorial: 5! = {factorial_result}")

# Logarithm (Natural Log)
natural_log_result = math.log(2.71)
print(f"Natural Log: log(2.71) = {natural_log_result}")

# Logarithm (Base 10)
base_10_log_result = math.log10(100)
print(f"Base 10 Log: log10(100) = {base_10_log_result}")

# Trigonometry (Sine, Cosine, Tangent)
sine_result = math.sin(math.pi / 2)
cosine_result = math.cos(0)
tangent_result = math.tan(math.pi / 4)
print(f"Sine: sin(pi/2) = {sine_result}")
print(f"Cosine: cos(0) = {cosine_result}")
print(f"Tangent: tan(pi/4) = {tangent_result}")

# ------------------------------
# Rounding Numbers
# ------------------------------

# Rounding to Nearest Integer
round_result = round(2.6)
print(f"Rounded to nearest integer: round(2.6) = {round_result}")

# Rounding Up
ceil_result = math.ceil(2.1)
print(f"Rounded up: ceil(2.1) = {ceil_result}")

# Rounding Down
floor_result = math.floor(2.9)
print(f"Rounded down: floor(2.9) = {floor_result}")

