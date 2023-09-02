# Python Type Errors, Type Checking & Type Conversion Explained

# ------------------------------
# Type Errors
# ------------------------------

# Type errors occur when an operation is performed on an inappropriate data type.

# For example, you can't concatenate a string and an integer
try:
    print("String" + 123)  # Will raise a TypeError
except TypeError as e:
    print(f"TypeError: {e}")

# ------------------------------
# Type Checking
# ------------------------------

# It's good practice to check the type of variables before performing operations on them.
# This can help to avoid TypeErrors.

# Checking if a variable is an integer
x = 10
if isinstance(x, int):
    print(f"{x} is an integer")

# Checking if a variable is a string
y = "Hello"
if type(y) == str:
    print(f"'{y}' is a string")

# ------------------------------
# Type Conversion
# ------------------------------

# Type conversion is the process of converting one data type to another.

# Integer to String
int_to_str = str(123)
print(f"Integer to string: {int_to_str} (Type: {type(int_to_str)})")

# String to Integer
str_to_int = int("123")
print(f"String to integer: {str_to_int} (Type: {type(str_to_int)})")

# Float to Integer (Note: This truncates the decimal part)
float_to_int = int(123.456)
print(f"Float to integer: {float_to_int} (Type: {type(float_to_int)})")

# Integer to Float
int_to_float = float(123)
print(f"Integer to float: {int_to_float} (Type: {type(int_to_float)})")

# Boolean to String
bool_to_str = str(True)
print(f"Boolean to string: {bool_to_str} (Type: {type(bool_to_str)})")

# ------------------------------
# Explicit Type Conversion in Operations
# ------------------------------

# Sometimes you may need to explicitly convert types to perform certain operations.

# Adding an integer to a float by converting integer to float
result = 123 + float("456.789")
print(f"Explicit Type Conversion Result: {result}")

# Note: Explicit type conversion can also be a source of errors, so use it carefully.
try:
    invalid_conversion = int("123abc")
except ValueError as e:
    print(f"ValueError in type conversion: {e}")

