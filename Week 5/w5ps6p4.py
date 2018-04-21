# -*- coding: utf-8 -*-
"""
Created on Sun Mar 25 08:09:55 2018

@author: simpp
Week 5 Problem Set 6 Problem 3
Part of ps6.py.
"""


def decrypt_story():
    crypted_text = get_story_string()
    ciphertext = CiphertextMessage(crypted_text)
    return ciphertext.decrypt_message()

