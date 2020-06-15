# -*- coding: utf-8 -*-
"""
MITx: 6.00.1x
Problem 1 - Paying Debt off in a Year 

@author: Chris.Rolling
"""

def monthlyInterestRate(annualInterestRate):
      return annualInterestRate / 12


def calculateFinalBalance(paymentAmount, balance):
      month = 0
      
      while month < 12:
            
            monthlyStatement = balance + (balance * monthlyInterestRate(annualInterestRate))
      
            newBalance = monthlyStatement - paymentAmount

            balance = newBalance

            month += 1
            
      return balance

def calculateLowestPayment(balance):
      testPaymentAmount = 10
      while True:
            ##print(testPaymentAmount)
            remainingBalance = calculateFinalBalance(testPaymentAmount, balance)
      
            if remainingBalance <=  30:
                  print("Lowest payment: " + str(testPaymentAmount))
                  break
            else: 
                  testPaymentAmount += 10 
                  ##print(remainingBalance)
calculateLowestPayment(balance)

