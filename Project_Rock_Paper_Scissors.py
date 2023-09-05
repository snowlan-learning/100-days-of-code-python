# ASCII art for the game options: Rock, Paper, Scissors
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

# Import the random module for generating computer's choice
import random

# Prompt the player for their choice
player_chose = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))

# Display the player's choice using ASCII art
print("\nPlayer chose:\n")
if player_chose == 0:
    print(rock)
elif player_chose == 1:
    print(paper)
elif player_chose == 2:
    print(scissors)
else:
    print("You did not pick a valid choice!")

# Generate the computer's choice randomly and display it using ASCII art
print("\nComputer chose:\n")
computer_chose = random.randint(0, 2)
if computer_chose == 0:
    print(rock)
elif computer_chose == 1:
    print(paper)
elif computer_chose == 2:
    print(scissors)
else:
    print("Computer did not pick a valid choice!")  # This should never happen

# Define result lists for the game based on the player's choices
list_of_results_1 = ["Draw", "Lose", "Win"]  # Results when player chooses Rock
list_of_results_2 = ["Win", "Draw", "Lose"]  # Results when player chooses Paper
list_of_results_3 = ["Lose", "Win", "Draw"]  # Results when player chooses Scissors

# Map the result lists into a single list for easier indexing
results_map = [list_of_results_1, list_of_results_2, list_of_results_3]

# Use double indexing to find the game result and print it
print(results_map[player_chose][computer_chose])


