# -*- coding: utf-8 -*-
"""
Created on Fri Mar  9 08:44:35 2018

@author: simpp
"""

hand = {'a':1, 'q':1, 'l':2, 'm':1, 'u':1, 'i':1}
word = "quail"

def updateHand(hand, word):
    """
    Assumes that 'hand' has all the letters in word.
    In other words, this assumes that however many times
    a letter appears in 'word', 'hand' has at least as
    many of that letter in it. 

    Updates the hand: uses up the letters in the given word
    and returns the new hand, without those letters in it.

    Has no side effects: does not modify hand.

    word: string
    hand: dictionary (string -> int)    
    returns: dictionary (string -> int)
    """
    updatedHand = hand.copy()
    for char in word:
        if char in updatedHand.keys() and updatedHand.get(char) == 1:
            del updatedHand[char]
        elif char in updatedHand.keys() and updatedHand.get(char) > 1:
            updatedHand[char] = updatedHand[char] - 1
    return updatedHand
    