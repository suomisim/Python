# -*- coding: utf-8 -*-
"""
Created on Thu Feb 22 14:43:00 2018

@author: simpp
Now write a program that calculates the minimum fixed monthly payment needed in order pay off a credit card balance within 12 months. 
By a fixed monthly payment, we mean a single number which does not change each month, 
but instead is a constant amount that will be paid each month.
Monthly interest rate = (Annual interest rate) / 12.0
Monthly unpaid balance = (Previous balance) - (Minimum fixed monthly payment)
Updated balance each month = 
(Monthly unpaid balance) + (Monthly interest rate x Monthly unpaid balance) 
	      Test Case 1:
	      balance = 3329
	      annualInterestRate = 0.2

	      Result Your Code Should Generate:
	      -------------------
	      Lowest Payment: 310
      
"""
balance = 3329
annualInterestRate = 0.2
initBalance = balance
monthlyInterestRate = annualInterestRate / 12.0
month = 1
minPay = 10
def calculate(month, balance, minPay, monthlyInterestRate):
    while month < 13:
        unpaidBalance = balance - minPay
        balance = unpaidBalance + (monthlyInterestRate * unpaidBalance)
        month += 1
    return balance
while calculate(month, balance, minPay, monthlyInterestRate) > 0:
    balance = initBalance
    minPay +=10
    month = 1
    calculate(month, balance, minPay, monthlyInterestRate)
print('Lowest Payment: ' + str(minPay))



