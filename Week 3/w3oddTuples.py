# -*- coding: utf-8 -*-
"""
Created on Fri Feb 23 08:21:54 2018

@author: simpp
Write a procedure called oddTuples, which takes a tuple as input, and returns a new tuple as output, 
where every other element of the input tuple is copied, starting with the first one. 
So if test is the tuple ('I', 'am', 'a', 'test', 'tuple'), 
then evaluating oddTuples on this input would return the tuple ('I', 'a', 'tuple').
"""
testTuple = ('I', 'am', 'a', 'test', 'tuple')

def oddTuples(testTuple):
    words = ()
    if testTuple == ():
        return (words)
    else:
        for t in testTuple:
            words = words + testTuple[0::2]
            return (words)