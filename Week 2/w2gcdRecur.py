# -*- coding: utf-8 -*-
"""
Created on Wed Feb 21 08:22:21 2018

@author: simpp
a, b: positive integers
    
returns: a positive integer, the greatest common divisor of a & b.
"""

def gcdRecur(a, b):
    if b == 0:
        return a
    else:
        return gcdRecur(b, a % b)

