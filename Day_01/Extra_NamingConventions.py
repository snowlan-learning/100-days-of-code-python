# Python Naming and Style Conventions

# ---- Descriptive Names ----
# Good Practice
username = "JohnDoe"
# Bad Practice
u = "JohnDoe"

# ---- Lowercase ----
# Use lowercase for simple variables
age = 21

# ---- Underscores for Multiple Words ----
# Use underscores to separate words (snake_case)
first_name = "John"

# ---- Case Sensitivity ----
# Variable names are case-sensitive
# These are different variables
Age = 21
age = 22

# ---- Constants ----
# Use all uppercase for constants, separating words with underscores
PI = 3.14159
MAX_SIZE = 100

# ---- Class Names ----
# Use CamelCase for class names
class UserProfile:
    pass

# ---- Avoid Single-letter Names ----
# Use single-letter names only in very short blocks where meaning is clear
# Acceptable:
for i in range(10):
    print(i)

# ---- Avoid using built-in names ----
# Don't use names that are built-in to Python
# Bad
list = [1, 2, 3]
# Good
my_list = [1, 2, 3]

# ---- Type Hints ----
# As of Python 3.5+, you can use type hints
from typing import List

def add_elements(elements: List[int]) -> int:
    return sum(elements)

# ---- Private Variables ----
# Prefix with an underscore for "private" variables intended for internal use
_hidden_var = 42

# By adhering to these best practices, you'll make your code more
# understandable and maintainable, both for yourself and for others.