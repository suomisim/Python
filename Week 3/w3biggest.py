# -*- coding: utf-8 -*-
"""
Created on Wed Feb 28 08:07:15 2018

@author: simpp
"""

aDict = { 'a': ['aardvark'], 'b': ['baboon'], 'c': ['coati']}

aDict['d'] = ['donkey']
aDict['d'].append('dog')
aDict['d'].append('dingo')

def biggest(aDict):
    '''
    aDict: A dictionary, where all the values are lists.

    returns: The key with the largest number of values associated with it
    '''
    if len(aDict) == 0:
        return None
    else:
        big = max(aDict.keys())
    return big