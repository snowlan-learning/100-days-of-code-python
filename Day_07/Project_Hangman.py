import random
import os
from hangman_words import word_list
from hangman_art import logo, stages

# Choose a random word from the provided word list for the game.
chosen_word = random.choice(word_list)

# Initialize player lives.
lives = 6  

# Display the game's logo when the game starts.
print(logo)

# Debugging hint - display the solution. Should be disabled for actual gameplay.
print(f'Pssst, the solution is {chosen_word}.')

# Initialize a list to represent the player's progress in guessing the word. 
# Underscores represent un-guessed letters.
display = [ "_" for letter in chosen_word ]

# Display the initial hidden word to the player.
print(display)

# Main game loop. Continues while the word isn't fully guessed and player has lives.
while "_" in display and lives > 0:

    # Prompt the player for their letter guess.
    guess = input("Guess a letter: ").lower()
    
    # Clear the terminal for a cleaner display. 
    os.system('clear')  # Note: This works for Linux/macOS. Use 'cls' for Windows.

    # Inform player if they've already guessed this letter.
    if guess in display:
        print(f"You have already entered the letter: {guess}")

    # Update the display list with correctly guessed letters.
    for index, letter in enumerate(chosen_word): 
        if letter == guess:
            display[index] = letter

    # Decrease the player's lives if the guessed letter isn't in the word.
    if guess not in chosen_word:
        lives -= 1
        
    # If all lives are lost, end the game and display a game over message.
    if lives == 0:
        print("Game Over")

    # Show the player's current progress in guessing the word.
    print(display)
    
    # Display the hangman drawing corresponding to the player's remaining lives.
    print(stages[lives])

# If loop ends and there are no more underscores in the display, the player has won.
if "_" not in display:
    print("You Win")
