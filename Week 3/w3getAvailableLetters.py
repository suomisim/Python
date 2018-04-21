# -*- coding: utf-8 -*-
"""
Created on Thu Mar  1 08:36:26 2018

@author: simpp
"""


lettersGuessed = ['e', 'i', 'k', 'p', 'r', 's']


def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    import string
    alphabet = string.ascii_lowercase
    
    for char in lettersGuessed:
        if char in alphabet:
            alphabet = alphabet.replace(char, "")   
    return alphabet