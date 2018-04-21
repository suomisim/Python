# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
Input x: int or float
Returns x to the power of 4
"""

def fourthPower(x):
    def square(x):
        y = x*x
        return y
    return square(square(x))