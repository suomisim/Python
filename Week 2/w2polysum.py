# -*- coding: utf-8 -*-
"""
Created on Thu Feb 22 08:24:07 2018

@author: simpp
Input: n and s
Output: This function sums the area and square of the perimeter 
of the regular polygon. The function returns the sum, rounded to 4 decimal places.
"""
import math

def polysum(n, s):
    area = (0.25 * n * s**2)/((math.tan(math.pi/n)))
    length = (n * s) **2

    return round((area + length), 4)