# Rollercoaster Ticket Program
# Display a welcome message to introduce the program
print("Welcome to the rollercoaster!")

# Collect user's height and age; convert inputs to integers
height = int(input("What is your height in cm? "))
age = int(input("What is your age? "))
bill = 0  # Initialize bill amount

# Check if the user meets the height requirement (at least 120 cm)
if height >= 120:
    # User is eligible to ride the rollercoaster
    print("You can ride the rollercoaster!")

    # Determine the ticket price based on age groups
    if age <= 12:
        print("Child ticket is $5.")
        bill = 5  # Cost for children
    elif age <= 18:
        print("Teen ticket is $7.")
        bill = 7  # Cost for teens
    elif age >= 45 and age <= 55:
        print("Ticketrs is free")
    else:
        print("Adult ticket is $12.")
        bill = 12  # Cost for adults

    # Ask user if they want a photo taken during the ride
    wants_photo = input("Do you want a photo taken? Y or N. ")

    if wants_photo == "Y":
        # Add the photo cost to the bill
        bill += 3

    # Display the total cost for the user
    print(f"Your final bill is ${bill}")

else:
    # User is not tall enough to ride; provide a polite refusal message
    print("Sorry, you need to grow taller before you can ride!")
