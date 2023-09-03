# Python PEMDAS Order of Operations Explained

# PEMDAS stands for Parentheses, Exponents, Multiplication and Division,
# and Addition and Subtraction. This rule sets the standard order of
# operations in mathematics, which is also followed in Python.

# ------------------------------
# Parentheses
# ------------------------------

# Parentheses have the highest priority and can be used to force an expression
# to evaluate in the order you want.

parentheses_result = (3 + 2) * 4  # 5 * 4 = 20
print(f"Using Parentheses: (3 + 2) * 4 = {parentheses_result}")

# ------------------------------
# Exponents
# ------------------------------

# Exponents are the next priority.

exponents_result = 2 ** 3  # 2 * 2 * 2 = 8
print(f"Exponents: 2 ** 3 = {exponents_result}")

# ------------------------------
# Multiplication and Division
# ------------------------------

# Multiplication and division are of equal priority and are performed from left to right.

mult_div_result = 8 * 2 / 4  # (8 * 2) / 4 = 16 / 4 = 4
print(f"Multiplication and Division: 8 * 2 / 4 = {mult_div_result}")

# ------------------------------
# Addition and Subtraction
# ------------------------------

# Finally, addition and subtraction are of the lowest priority and are also
# performed from left to right.

add_sub_result = 3 + 4 - 2  # 3 + 4 = 7, 7 - 2 = 5
print(f"Addition and Subtraction: 3 + 4 - 2 = {add_sub_result}")

# ------------------------------
# Complete PEMDAS Example
# ------------------------------

# Putting it all together
complete_pemdas_result = (2 + 3) * 4 ** 2 / 2 - 1  # ((5) * 16) / 2 - 1 = 80 / 2 - 1 = 40 - 1 = 39
print(f"Complete PEMDAS Example: (2 + 3) * 4 ** 2 / 2 - 1 = {complete_pemdas_result}")



