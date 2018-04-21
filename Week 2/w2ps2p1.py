# -*- coding: utf-8 -*-
"""
Created on Thu Feb 22 08:50:35 2018

@author: simpp
	      # Test Case 1:

	      
	      # Result Your Code Should Generate Below:
	      Remaining balance: 31.38
                    
          # To make sure you are doing calculation correctly, this is the 
          # remaining balance you should be getting at each month for this example
            Month 1 Remaining balance: 40.99
            Month 2 Remaining balance: 40.01
            Month 3 Remaining balance: 39.05
            Month 4 Remaining balance: 38.11
            Month 5 Remaining balance: 37.2
            Month 6 Remaining balance: 36.3
            Month 7 Remaining balance: 35.43
            Month 8 Remaining balance: 34.58
            Month 9 Remaining balance: 33.75
            Month 10 Remaining balance: 32.94
            Month 11 Remaining balance: 32.15
            Month 12 Remaining balance: 31.38
            
    A summary of the required math is found below:

    Monthly interest rate= (Annual interest rate) / 12.0
    Minimum monthly payment = (Minimum monthly payment rate) x (Previous balance)
    Monthly unpaid balance = (Previous balance) - (Minimum monthly payment)
    Updated balance each month = (Monthly unpaid balance) + (Monthly interest rate x Monthly unpaid balance)

"""
balance = 42
annualInterestRate = 0.2
monthlyPaymentRate = 0.04
month = 1

while month < 13:
    minPayment = (monthlyPaymentRate * balance)
    balance = balance - minPayment
    balance = balance * (1 + (annualInterestRate/12))
#   print("Month " + str(month) + " Remaining balance:", (round(balance, 2)))
    month = month +1
print("Remaining balance:", (round(balance, 2)))