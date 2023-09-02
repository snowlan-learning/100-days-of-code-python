# Display a welcome message to introduce the Band Name Generator program.
print("Welcome to the Band Generator.")

# Prompt the user to enter the name of the city where they grew up.
# The '\n' ensures that the user's input starts on a new line.
user_city = input("What is the name of the city you grew up in? \n")

# Prompt the user to enter the name of their first pet.
# The '\n' ensures that the user's input starts on a new line.
user_pet = input("What is the name of your first pet? \n")

# Generate a suggested band name by combining the user's city and pet name.
# Display the generated band name to the user.
print("Your band name could be " + user_city + " " + user_pet )