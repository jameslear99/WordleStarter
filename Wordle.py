# File: Wordle.py

"""
This module is the starter file for the Wordle assignment.
BE SURE TO UPDATE THIS COMMENT WHEN YOU WRITE THE CODE.
"""

import random

from WordleDictionary import FIVE_LETTER_WORDS
from WordleGraphics import WordleGWindow, N_COLS, N_ROWS
from WordleGraphics import CORRECT_COLOR, PRESENT_COLOR, MISSING_COLOR

def wordle():
    secretWord = random.choice(FIVE_LETTER_WORDS)
    gw = WordleGWindow()
    
    def enter_action(s):
        currentRow = gw.get_current_row()
        
        if spellCheck(currentRow):
            user_word = getUserWord(currentRow)
            feedback = getFeedback(user_word, secretWord)
            
            gw.set_current_row(currentRow + 1)
            
            for col, status in enumerate(feedback):
                if status == 'C':  # Correct letter and position
                    gw.set_square_color(currentRow, col, CORRECT_COLOR)
                elif status == 'P':  # Correct letter, wrong position
                    gw.set_square_color(currentRow, col, PRESENT_COLOR)
                else:  # Incorrect letter
                    gw.set_square_color(currentRow, col, MISSING_COLOR)
                    
            
            if user_word == secretWord:
                gw.show_message("You win!")
                return
            
            # Is the game over?
            if currentRow == N_ROWS - 1:
                gw.show_message("Game Over!")
                return

    def getUserWord(currentRow):
        word = ""
        for col in range(N_COLS):
            word += gw.get_square_letter(currentRow, col)
        return word.lower()
        
    def spellCheck(currentRow):
        word = getUserWord(currentRow)
        if word in FIVE_LETTER_WORDS:
            return True
        else:
            gw.show_message("You fool! This is no word!")
            return False
            
    def getFeedback(user_word, secret_word):
        feedback = ['M'] * N_COLS
        for i in range(N_COLS):
            if user_word[i] == secret_word[i]:
                feedback[i] = 'C'
        for i in range(N_COLS):
            if feedback[i] == 'M' and user_word[i] in secret_word:
                feedback[i] = 'P'
        return feedback

    gw.add_enter_listener(enter_action)

if __name__ == "__main__":
    wordle()
