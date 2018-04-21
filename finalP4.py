# -*- coding: utf-8 -*-
"""
Created on Sat Mar 31 08:19:57 2018

@author: simpp
Write a Python function that creates and returns a list of prime numbers between 2 
and N, inclusive, sorted in increasing order. 
A prime number is a number that is divisible only by 1 and itself. 
This function takes in an integer and returns a list of integers.
"""


def primes_list(N):
    '''
    N: an integer
    Returns a list of prime numbers
    '''
    primes = []
    if N == 2:
        primes.append(2)
    else:
        for num in range(2,N):
            prime = True
            for i in range(2,num):
                if (num%i==0):
                    prime = False
            if prime:
                primes.append(num)
    return primes