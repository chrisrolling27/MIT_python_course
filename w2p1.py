# -*- coding: utf-8 -*-
"""
MITx: 6.00.1x
Problem 1 - Paying Debt off in a Year 

@author: Chris.Rolling
"""

month = 0

def monthlyInterestRate(annualInterestRate):
      return annualInterestRate / 12


while month < 12:
            
      monthlyStatement = balance + (balance * monthlyInterestRate(annualInterestRate))
      
      newBalance = monthlyStatement - (monthlyStatement * monthlyPaymentRate)

      balance = newBalance

      month += 1

print(round(balance, 2))