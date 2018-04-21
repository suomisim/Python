# -*- coding: utf-8 -*-
"""
Created on Sun Mar  4 10:47:33 2018

@author: simpp
"""


list_of_numbers = [0, 2, 4]
index = 0

def fancy_divide(list_of_numbers, index):
   denom = list_of_numbers[index]
   return [simple_divide(item, denom) for item in list_of_numbers]


def simple_divide(item, denom):
    try:
        return item / denom
    except ZeroDivisionError:
        return 0
    