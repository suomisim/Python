# -*- coding: utf-8 -*-
"""
Created on Wed Feb 21 08:45:49 2018

@author: simpp
"""

def middleChar(aStr):
    middle = "0"
    if(len(aStr) % 2 == 0):
        middle = aStr[(int(len(aStr) / 2) - 1 )] + aStr[(int(len(aStr) / 2))]
    else:
        middle = aStr[(int(len(aStr)/2))]
    return middle    
    