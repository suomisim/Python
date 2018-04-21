# -*- coding: utf-8 -*-
"""
Created on Thu Mar  1 08:25:52 2018

@author: simpp
"""
secretWord = 'apple' 
lettersGuessed = ['e', 'i', 'k', 'p', 'r', 's']

def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    outputWord = []
    for char in secretWord:
        if char in lettersGuessed:
            outputWord.append(char)
        else:
            outputWord.append("_ ")
    return ''.join(outputWord)
        