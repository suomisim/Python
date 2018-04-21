# -*- coding: utf-8 -*-
"""
Created on Sat Mar 10 07:31:59 2018

@author: simpp
"""

WORDLIST_FILENAME = "words.txt"
word = 'rapture'
hand = {'r': 1, 'a': 3, 'p': 2, 'e': 1, 't': 1, 'u': 1}

inFile = open(WORDLIST_FILENAME, 'r')
# wordList: list of strings
wordList = []
for line in inFile:
    wordList.append(line.strip().lower())




def isValidWord(word, hand, wordList):
    """
    Returns True if word is in the wordList and is entirely
    composed of letters in the hand. Otherwise, returns False.

    Does not mutate hand or wordList.
   
    word: string
    hand: dictionary (string -> int)
    wordList: list of lowercase strings
    """
    isInWordList = True
    isInHand = True
    isAllInHand = True
    
    updatedHand = hand.copy()
    for char in word:
        if char in updatedHand.keys():
            updatedHand[char] = updatedHand[char] - 1
        else:
            isInHand = False
    for value in updatedHand.values():
        if value < 0:
            isAllInHand = False
    if word in wordList:
        isInWordList = True
    else:
        isInWordList = False
    if isInHand == True and isAllInHand == True and isInWordList == True:
        return True
    else:
        return False
    
    
    
#    isIt = False
#    if word in wordList:
#        for char in word:
#            if char in hand.keys():
#                isIt = True
#            else:
#                isIt = False
#    return isIt
    
    
