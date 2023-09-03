# This program calculates the "Love Compatibility" score between two people based on the characters in their names.
# The algorithm involves four steps:
# 1. Prompt the user to enter the names of the two individuals.
# 2. Calculate the occurrences of each letter in the words "TRUE" and "LOVE" within the concatenated names.
# 3. Concatenate the counts to form a two-digit score.
# 4. Display a compatibility message based on the generated score.

# Display a welcome message to greet the user.
print("Welcome to the Love Calculator!")

# Prompt the user to enter their name and the name of the other individual.
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")

# Convert the names to lowercase and concatenate them to facilitate counting.
combined_name = name1.lower() + name2.lower()

# Count the occurrences of each letter in the word "TRUE" within the combined names.
true_count = combined_name.count("t") + combined_name.count("r") + combined_name.count("u") + combined_name.count("e")

# Count the occurrences of each letter in the word "LOVE" within the combined names.
love_count = combined_name.count("l") + combined_name.count("o") + combined_name.count("v") + combined_name.count("e")

# Concatenate the two counts to form a two-digit love score.
score = int(str(true_count) + str(love_count))

# Generate and display a message indicating compatibility based on the calculated score.
if score < 10 or score > 90:
    print(f"Your score is {score}, you go together like coke and mentos.")
elif score >= 40 and score <= 50: 
    print(f"Your score is {score}, you are alright together.")
else:
    print(f"Your score is {score}.")