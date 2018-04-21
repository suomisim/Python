# -*- coding: utf-8 -*-
"""
Created on Sun Feb 25 09:19:49 2018

@author: simpp
"""

def applyEachTo(L, x):
    result = []
    for i in range(len(L)):
        result.append(L[i](x))
    return result

def square(a):
    return a*a

def halve(a):
    return a/2

def inc(a):
    return a+1