# Python Pizza Order Program
# This program calculates the final bill for a pizza order based on the user's selection of size, pepperoni, and extra cheese.

# Pricing Guide:
# - Small Pizza: $15
# - Medium Pizza: $20
# - Large Pizza: $25
# - Pepperoni for Small Pizza: Additional $2
# - Pepperoni for Medium or Large Pizza: Additional $3
# - Extra cheese for any size: Additional $1

# Display welcome message and gather user preferences
print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")

# Initialize the bill amount to 0
bill = 0 

# Calculate the cost based on the size of the pizza
if size == "S":
    bill += 15  # Small pizza cost
    if add_pepperoni == "Y":
        bill += 2  # Add pepperoni cost for small pizza
elif size == "M":
    bill += 20  # Medium pizza cost
    if add_pepperoni == "Y":
        bill += 3  # Add pepperoni cost for medium pizza
elif size == "L":
    bill += 25  # Large pizza cost
    if add_pepperoni == "Y":
        bill += 3  # Add pepperoni cost for large pizza
else:
    print("You did not choose a valid size!")  # Invalid size selection

# Calculate the cost for extra cheese, if requested
if extra_cheese == "Y":
    bill += 1  # Add extra cheese cost

# Display the final bill amount
print(f"Your final bill is: ${bill}.")