# -*- coding: utf-8 -*-
"""
Created on Sat Mar 31 08:33:11 2018

@author: simpp
 You are given a dictionary aDict that maps integer keys to integer values. Write a Python function that returns a list of keys in aDict that map to dictionary values that appear exactly once in aDict.

    This function takes in a dictionary and returns a list.
    Return the list of keys in increasing order.
    If aDict does not contain any values appearing exactly once, return an empty list.
    If aDict is empty, return an empty list.

"""


aDict = {1: 1, 3: 2, 6: 0, 7: 0, 8: 4, 10: 0}

def uniqueValues(aDict):
    uniques = {}
    for i in aDict.values():
        uniques.setdefault(i,0)
        uniques[i] += 1   
    return sorted(k for k, v in aDict.items() if uniques[v] == 1)