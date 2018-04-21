# -*- coding: utf-8 -*-
"""
Created on Sat Mar 10 08:18:08 2018

@author: simpp
"""
hand = {'r': 1, 'a': 3, 'p': 2, 'e': 1, 't': 1, 'u': 1}

def calculateHandlen(hand):
    """ 
    Returns the length (number of letters) in the current hand.
    
    hand: dictionary (string int)
    returns: integer
    """
    result = 0
    for value in hand.keys():
        result = result + hand.get(value)
    return result
    