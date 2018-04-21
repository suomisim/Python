# -*- coding: utf-8 -*-
"""
Created on Tue Feb 20 09:17:37 2018

@author: simpp
base: int or float.
exp: int >= 0
returns: int or float, base^exp
"""
def iterPower(base, exp):
    def iin(base, exp):
        return 1 if exp <= 0 else \
               base * iin(base, exp-1)
    return iin(base, exp)

