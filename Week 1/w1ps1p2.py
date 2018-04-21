# -*- coding: utf-8 -*-
"""
Created on Wed Feb 14 09:11:16 2018

@author: simpp
"""

s = 'kbobboboobobbbobobrbobszbo'
sana = 'bob'
count = 0
for x in range(len(s) - len(sana) + 1):
    if s[x:x+len(sana)] == sana:
            count += 1
print("Number of times bob occurs is: ", count)