# -*- coding: utf-8 -*-
"""
Created on Wed Feb 21 08:40:01 2018

@author: simpp
char: a single character
aStr: an alphabetized string
    
returns: True if char is in aStr; False otherwise
"""

def isIn(char, aStr):
    
    if not aStr or type(aStr) != str:
        return False
    middlechar = aStr[len(aStr)//2]
    if char == middlechar:
        return True
    elif char != middlechar and len(aStr) == 1:
        return False
    elif char <  middlechar:
        return isIn(char, aStr[: len(aStr)//2])
    else:
        return isIn(char, aStr[len(aStr)//2:])