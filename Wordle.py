# File: Wordle.py

"""
This module is the starter file for the Wordle assignment.
BE SURE TO UPDATE THIS COMMENT WHEN YOU WRITE THE CODE.
"""

import random

from WordleDictionary import FIVE_LETTER_WORDS
from WordleGraphics import WordleGWindow, N_COLS, N_ROWS

def wordle():
    # secretWord = random.choice(FIVE_LETTER_WORDS)
    # gw = WordleGWindow()
    

    def enter_action(s):

         # gw.show_message("You have to implement this method.")
        currentRow= gw.get_current_row()

        if spellCheck(currentRow) == True:
            gw.set_current_row(currentRow + 1)

   

    gw = WordleGWindow()
    gw.add_enter_listener(enter_action)


#Spell check function
    def spellCheck(currentRow):
        
        word = ""
        #Grabs all the letters from each column and makes a word
        for col in range(0, N_COLS):
            word += gw.get_square_letter(currentRow, col)
        #Converts the word to lowercase to match the dictionary
        word = word.lower()        
        #Checks if the entered word is found inside the dictionary, then either moves to a new line, or displays error
        
        if word in FIVE_LETTER_WORDS:
            return True
            
        else:
            gw.show_message("You fool! This is no word!")
  

        
        



# Startup code

if __name__ == "__main__":
    wordle()
