# -*- coding: utf-8 -*-
"""
Created on Wed Feb 21 08:09:00 2018

@author: simpp
a, b: positive integers
    
returns: a positive integer, the greatest common divisor of a & b.
"""

def gcdIter(a, b):
    x = a + b
    while a%x != 0 or b%x != 0:
        x = x -1
    return x

    
