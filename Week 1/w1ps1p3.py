# -*- coding: utf-8 -*-
"""
Created on Wed Feb 14 09:11:16 2018

@author: simpp
"""

s = 'hlqrjqbjiwedabhlqrjzzw'

length, start, stop, i = len(s), 0, 0, 0

while i < length:

    j = i+1

    while j < length and s[j] >= s[j-1]:
        j += 1

    if j - i > stop - start:
        start, stop = i, j

    i = j

print("Longest substring in alphabetical order is:",s[start:stop])