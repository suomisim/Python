# -*- coding: utf-8 -*-
"""
Created on Sat Mar 31 08:16:47 2018

@author: simpp
"""

def sum_digits(s):
    """ assumes s a string
        Returns an int that is the sum of all of the digits in s.
          If there are no digits in s it raises a ValueError exception. """
    sum = 0
    for i in s:
        try:
            sum += int(i)
        except ValueError:
            pass
    return sum