# -*- coding: utf-8 -*-
"""
MITx: 6.00.1x
Problem 2 - Getting the User's Guess 

@author: Chris.Rolling
"""

def getGuessedWord(secret_word, letters_guessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    guessed_so_far = ""
    for c in secret_word:
        if c in letters_guessed:
            guessed_so_far += c
        else:
            guessed_so_far += " _ "
    return guessed_so_far