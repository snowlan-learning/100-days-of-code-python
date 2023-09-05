# Instructions:
# The purpose of this program is to place an "X" at a specific location on a 3x3 map.
# The initial map is represented as a nested list with each sublist representing a row. Each element is a "⬜️".

# Note:
# To visualize the map more clearly, the print statement formats it as a 3x3 square grid.

# ---------------- Do not modify the code below this line -----------------
row1 = ["⬜️", "⬜️", "⬜️"]
row2 = ["⬜️", "⬜️", "⬜️"]
row3 = ["⬜️", "⬜️", "⬜️"]
map = [row1, row2, row3]

# Display the initial map
print(f"{row1}\n{row2}\n{row3}")

# Collect user input to place the "X"
position = input("Where do you want to put the treasure? (Format: XY, where X is the row and Y is the column): ")
# ---------------- Do not modify the code above this line -----------------

# Convert the input string into a list of its characters
list_position = list(position)

# Extract the row and column numbers from the input, and convert them to integers
horizontal_digit = int(list_position[0])
vertical_digit = int(list_position[1])

# Update the corresponding position in the map with an "X"
map[vertical_digit - 1][horizontal_digit - 1] = "X"


# ---------------- Do not modify the code below this line -----------------
# Display the map after placing the "X"
print(f"{row1}\n{row2}\n{row3}")
