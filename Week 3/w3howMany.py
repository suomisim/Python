# -*- coding: utf-8 -*-
"""
Created on Tue Feb 27 07:57:57 2018

@author: simpp

"""

aDict = { 'a': ['aardvark'], 'b': ['baboon'], 'c': ['coati']}

aDict['d'] = ['donkey']
aDict['d'].append('dog')
aDict['d'].append('dingo')

def how_many(aDict):
    result = 0
    for value in aDict.values():
        # Since all the values of aDict are lists, aDict.values() will 
        #  be a list of lists
        result += len(value)
    return result