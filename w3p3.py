# -*- coding: utf-8 -*-
"""
MITx: 6.00.1x
Problem 3 - Printing Out all Available Letters 

@author: Chris.Rolling
"""

def getAvailableLetters(letters_guessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    available = ""
    for letter in string.ascii_lowercase:
        if letter not in letters_guessed:
            available += letter
    return available