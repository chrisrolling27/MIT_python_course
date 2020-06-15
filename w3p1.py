# -*- coding: utf-8 -*-
"""
MITx: 6.00.1x
Problem 1 - Is the Word Guessed 

@author: Chris.Rolling
"""

def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    for l in secretWord: 
          if l not in lettersGuessed:
                return False
    return True 