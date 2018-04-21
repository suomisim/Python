# -*- coding: utf-8 -*-
"""
Created on Fri Feb 23 07:59:24 2018

@author: simpp
Monthly interest rate = (Annual interest rate) / 12.0
Monthly payment lower bound = Balance / 12
Monthly payment upper bound = (Balance x (1 + Monthly interest rate)12) / 12.0 
	      Test Case 1:
	      balance = 320000
	      annualInterestRate = 0.2

	      Result Your Code Should Generate:
	      -------------------
	      Lowest Payment: 29157.09
"""

balance = 320000
annualInterestRate = 0.2

initBalance = balance
monthlyInterestRate = annualInterestRate/12.0
low = balance/12.0
high = (balance * ((1.0 + monthlyInterestRate)**12))/12.0
epsilon = 0.01
minPay = (high + low)/2.0
month = 1

def calculate(month, balance, minPay, monthlyInterestRate):
    while month <13:
        unpaidBalance = balance - minPay
        balance = unpaidBalance + (monthlyInterestRate * unpaidBalance)
        month += 1
    return balance   
while abs(balance) >= epsilon:
    balance = initBalance
    month = 1
    balance = calculate(month, balance, minPay, monthlyInterestRate)
    if balance > 0:
        low = minPay
    else:
        high = minPay
    minPay = (high + low)/2.0
minPay = round(minPay,2)
print('Lowest Payment: ' + str(minPay))

