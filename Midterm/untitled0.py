# -*- coding: utf-8 -*-
"""
Created on Sun Mar  4 10:47:33 2018

@author: simpp
"""
def fancy_divide(list_of_numbers, index):
   denom = list_of_numbers[index]
   return [simple_divide(item, denom) for item in list_of_numbers]


def simple_divide(item, denom):
   return item / denom
    