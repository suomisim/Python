# -*- coding: utf-8 -*-
"""
Created on Tue Feb 20 09:38:20 2018

@author: simpp
base: int or float.
exp: int >= 0 
returns: int or float, base^exp
"""

def recurPower(base, exp):
    if base == 1:
        return 1
    elif exp == 0:
        return 1
    else:
        return base*recurPower(base, exp - 1)