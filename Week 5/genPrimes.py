# -*- coding: utf-8 -*-
"""
Created on Thu Mar 22 08:17:01 2018

@author: simpp
Write a generator, genPrimes, that returns the sequence of prime numbers on successive calls to its next() method: 2, 3, 5, 7, 11, ...
"""



def genPrimes():
    primes = [2]
    yield primes[0]
    guess = 3
    while True:
        if all(guess%x != 0 for x in primes):
            primes.append(guess)        
        if guess == primes[-1]:
            yield primes[-1]
        guess += 2