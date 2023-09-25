# File: Wordle.py

"""
This module is the starter file for the Wordle assignment.
BE SURE TO UPDATE THIS COMMENT WHEN YOU WRITE THE CODE.
"""

import random

from WordleDictionary import FIVE_LETTER_WORDS
from WordleGraphics import WordleGWindow, N_COLS, N_ROWS

secretWord = random.choice(FIVE_LETTER_WORDS).upper()
winCount = 0
guessCount = []

def wordle():
    

    def delete_action():
        
        gw.set_square_letter(1,5,"")

    def enter_action(s):
        global winCount
        global secretWord    
         # gw.show_message("You have to implement this method.")
        currentRow= gw.get_current_row()
        spellCheckResult = spellCheck(currentRow)

        if currentRow == N_ROWS - 1:
            gw.show_message("GAME OVER! YOU SUCK!")

        if spellCheckResult == True:
            correctCount = colorLetters(currentRow)
            gw.set_current_row(currentRow + 1)

            if correctCount == 5:
                winCount = winCount + 1
                guessCount.append(currentRow + 1)
                averageGuess = round((sum(guessCount)/len(guessCount)), 2)
                gw.show_message("You win! Games won: " + str(winCount) + " Average guesses: " + str(averageGuess))
                secretWord = random.choice(FIVE_LETTER_WORDS).upper()




        
                        


                
                


   

    gw = WordleGWindow()
    gw.add_enter_listener(enter_action)
    
    # gw.add_delete_listener(delete_action)

#Color Letter funciton
    def colorLetters(currentRow):
        correctCount = 0
        for col in range(0, N_COLS):
            if gw.get_square_letter(currentRow, col) == secretWord[col]:
                gw.set_square_color(currentRow,col,"#66BB66")
                gw.set_key_color(gw.get_square_letter(currentRow, col),"#66BB66")
                correctCount += 1
           
            elif gw.get_square_letter(currentRow,col) in secretWord:
                gw.set_key_color(gw.get_square_letter(currentRow, col),"#CCBB66")
                gw.set_square_color(currentRow,col,"#CCBB66") 

            elif gw.get_square_letter(currentRow,col) not in secretWord:
                gw.set_key_color(gw.get_square_letter(currentRow, col),"#999999")
                gw.set_square_color(currentRow,col,"#999999")
                
            else:
                pass

        return correctCount

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
            for col in range(0, N_COLS):
                gw.set_square_letter(currentRow,col, "")
            gw.set_current_row(currentRow)
            
            gw.show_message("You fool! This is no word!" + secretWord)
            
  


        



# Startup code

if __name__ == "__main__":
    wordle()
