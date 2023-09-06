# Loops with Lists in Python

# Initializing a list of integers
numbers = [1, 2, 3, 4, 5]

# Using a for loop to iterate through each element in the list
print("Using for loop to iterate through each element:")
for num in numbers:
    print(num)

# Using a for loop with the enumerate function to get index and value
print("\nUsing for loop with enumerate to get index and value:")
for index, num in enumerate(numbers):
    print(f"Index: {index}, Value: {num}")

# Using a while loop to iterate through the list
print("\nUsing while loop to iterate:")
index = 0
while index < len(numbers):
    print(numbers[index])
    index += 1

# Looping through a list of strings
words = ["apple", "banana", "cherry"]
print("\nLooping through a list of strings:")
for word in words:
    print(word.upper())  # Convert each word to uppercase

# Nested lists and nested loops
nested_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print("\nLooping through a nested list:")
for sublist in nested_list:
    for num in sublist:
        print(num)

# Using list comprehensions to create a new list
squared_numbers = [num ** 2 for num in numbers]
print("\nUsing list comprehension to create a new list of squared numbers:")
print(squared_numbers)

# Using list comprehensions with conditions
even_squared_numbers = [num ** 2 for num in numbers if num % 2 == 0]
print("\nUsing list comprehension with conditions to get squares of even numbers:")
print(even_squared_numbers)

# Modifying the original list using a loop
print("\nModifying the original list to square each element:")
for i in range(len(numbers)):
    numbers[i] = numbers[i] ** 2
print(numbers)
