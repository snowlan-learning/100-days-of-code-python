# Python f-strings Explained

# f-strings provide a concise and convenient way to embed Python expressions
# inside string literals for formatting.

# ------------------------------
# Basic Usage of f-strings
# ------------------------------

name = "John"
age = 30

# Using f-string to embed variables within strings.
greeting = f"Hello, my name is {name} and I am {age} years old."
print(f"Basic Usage: {greeting}")

# ------------------------------
# Expressions within f-strings
# ------------------------------

# You can perform operations inside the curly braces.
price = 20
tax = 0.1
total_price = f"The total price with tax is {price * (1 + tax)}."
print(f"Expressions: {total_price}")

# ------------------------------
# Formatting Floats in f-strings
# ------------------------------

# You can format float numbers to control decimal places.
pi = 3.141592653589793
formatted_pi = f"Pi rounded to 2 decimal places: {pi:.2f}"
print(f"Formatting Floats: {formatted_pi}")

# ------------------------------
# Dynamic Expressions
# ------------------------------

# Dynamic expressions can also be used within f-strings.
x, y = 5, 10
result = f"The sum of {x} and {y} is {x + y}."
print(f"Dynamic Expressions: {result}")

# ------------------------------
# Padding and Alignment
# ------------------------------

# You can pad and align text using f-strings.
name = "John"
print(f"Padding and Alignment: |{name:<10}|{name:^10}|{name:>10}|")

# '<' aligns the text to the left.
# '^' centers the text.
# '>' aligns the text to the right.

# ------------------------------
# Escaping Braces
# ------------------------------

# To include literal curly braces in the string, you can escape them by doubling them.
print(f"Escaping Braces: {{Hello}} {name}")

# ------------------------------

