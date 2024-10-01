########################################
# Name: Cody Pagone
# Collaborators (if any): Jack Crone
# GenAI Transcript (if any):
# Estimated time spent (hr): 5.5
# Description of any added extensions:
########################################

from WordleGraphics import WordleGWindow, N_ROWS, N_COLS, CORRECT_COLOR, PRESENT_COLOR, MISSING_COLOR, UNKNOWN_COLOR
import random
from english import ENGLISH_WORDS, is_english_word  # Assuming this is a valid import

# Function to randomly select a word from ENGLISH_WORDS
def get_random_word():
    return random.choice([word for word in ENGLISH_WORDS if len(word) == 5])

# Function to visually update the grid and show messages
def check_wordle_guess(input_word: str, correct_word: str, gw):
    current_row = gw.get_current_row()
    
    # Loop over each letter in the input word and update the grid
    for i, letter in enumerate(input_word):
        gw.set_square_letter(current_row, i, letter.upper())  # Set the letter in the grid

        # Check if the letter is correct
        if letter.lower() == correct_word[i].lower():
            gw.set_square_color(current_row, i, "#66BB66")  # Green for correct letters
        elif letter.lower() in correct_word.lower():
            gw.set_square_color(current_row, i, "#CCBB66")  # Yellow for present but misplaced letters
        else:
            gw.set_square_color(current_row, i, "#999999")  # Gray for missing letters
    
    # Check if the entire word is correct
    if input_word.lower() == correct_word.lower():
        gw.show_message("Congratulations! You guessed the word!")
        return True
    else:
        gw.show_message("Try again.")
        return False

# Function to handle input and process it
def handle_enter(gw, correct_word):
    current_row = gw.get_current_row()
    
    try:
        # Assuming gw.word_from_row() is a custom method you wrote for extracting words from the grid
        input_word = word_from_row(gw, current_row)  # Get the input word from the current row
    except AttributeError:
        gw.show_message("Error: Unable to retrieve word from row.")
        return

    # Check if the guess is valid
    if len(input_word) != 5:
        gw.show_message("Please enter a 5-letter word.")
        return
    
    # Check the guess and update the grid
    success = check_wordle_guess(input_word, correct_word, gw)

    # Move to the next row if guess is wrong
    if not success:
        if current_row < 5:  # Move to the next row if not at the last row
            gw.set_current_row(current_row + 1)
        else:
            gw.show_message("Game over!")
    
    # If the guess is correct
    if success:
        gw.show_message("Congratulations! You've won!")

# Utility function to get word from a row (implement this if it doesn't exist in your class)
def word_from_row(gw, row):
    word = ""
    for col in range(5):  # Assuming a 5-letter word
        letter = gw.get_square_letter(row, col)
        word += letter
    return word

# Main game setup
def start_wordle_game():
    # Initialize the Wordle window
    gw = WordleGWindow()  # Ensure this exists in your WordleGraphics file
    
    correct_word = get_random_word()  # Get the random word
    gw.set_current_row(0)  # Set the initial row to start typing
    
    # Attach the 'Enter' key listener to process the input and check the guess
    gw.add_enter_listener(lambda: handle_enter(gw, correct_word))
    
    # Start the game window (if this is necessary for your framework)
    gw.run()  # Assuming there's a run method to launch the GUI loop

# Start the game
start_wordle_game()

