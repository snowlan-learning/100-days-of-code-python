# ================================
# Working with Lists in Python
# ================================

# === Creating Lists ===

# Creating an empty list
empty_list = []
print(f"Empty list: {empty_list}")

# Creating a list with integers
integer_list = [1, 2, 3, 4, 5]
print(f"Integer list: {integer_list}")

# Creating a list with mixed data types
mixed_list = [1, "hello", 3.14, True]
print(f"Mixed list: {mixed_list}")

# === Accessing Elements ===

# Accessing an element by its index
first_element = integer_list[0]
print(f"First element: {first_element}")

# Accessing the last element
last_element = integer_list[-1]
print(f"Last element: {last_element}")

# === Slicing Lists ===

# Get a slice from index 1 to 3 (3 is exclusive)
sublist = integer_list[1:3]
print(f"Sublist (1 to 3): {sublist}")

# Get all elements from index 2 onwards
sublist = integer_list[2:]
print(f"Sublist (from index 2): {sublist}")

# === Modifying Lists ===

# Changing an element by index
integer_list[0] = 100
print(f"Modified list: {integer_list}")

# Adding an element at the end
integer_list.append(6)
print(f"Appended list: {integer_list}")

# Adding multiple elements at the end
integer_list.extend([7, 8, 9])
print(f"Extended list: {integer_list}")

# Inserting an element at a specific index
integer_list.insert(0, 0)
print(f"List after insertion: {integer_list}")

# === Removing Elements ===

# Remove an element by value (only the first occurrence)
integer_list.remove(100)
print(f"List after removing 100: {integer_list}")

# Remove an element by index
del integer_list[0]
print(f"List after removing the first element: {integer_list}")

# Pop the last element
popped_element = integer_list.pop()
print(f"Popped element: {popped_element}")
print(f"List after pop: {integer_list}")

# === List Operations ===

# Concatenation
new_list = integer_list + [10, 11, 12]
print(f"Concatenated list: {new_list}")

# Repeating elements
repeated_list = [1, 2] * 3
print(f"Repeated list: {repeated_list}")

# === Useful List Methods ===

# Finding the index of an element
index_of_three = integer_list.index(3)
print(f"Index of 3: {index_of_three}")

# Count occurrences of an element
count_of_three = integer_list.count(3)
print(f"Count of 3: {count_of_three}")

# Sorting a list
integer_list.sort()
print(f"Sorted list: {integer_list}")

# Reversing a list
integer_list.reverse()
print(f"Reversed list: {integer_list}")

# === List Comprehension ===

# Create a list of squares from 0 to 9
squares = [x ** 2 for x in range(10)]
print(f"Squares: {squares}")

# Create a list of odd numbers from 0 to 9
odd_numbers = [x for x in range(10) if x % 2 != 0]
print(f"Odd numbers: {odd_numbers}")

# This concludes the basics of lists in Python.
# Lists are versatile and offer a wide range of methods for manipulation.
