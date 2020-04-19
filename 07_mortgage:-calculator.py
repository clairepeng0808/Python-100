#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr  9 18:04:17 2020

@author: clairepeng

Mortgage Calculator - Calculate the monthly payments of a f
ixed term mortgage over given Nth terms at a given interest rate. 
Also figure out how long it will take the user to pay back the loan. 
For added complexity, add an option for users to select the 
compounding interval (Monthly, Weekly, Daily, Continually).
"""


print('Welcome to mortgage Calculator!')

def enter_terms():
    while True:
        try:
            terms = int(input('Enter the morgage term(in years): '))
            
            if terms >= 50:
                print('Sorry, the term should be under 50 years.')

            
            elif terms <= 0:
                    print('The term should be a positive integer.')
                    continue
            else:
                 
                return terms
                break
        
        except ValueError:
            print('Please enter an integer.')

def enter_rate():
    while True:
        try:
            rate = float(input('Enter the interest rate(%): '))
            
            if rate > 100:
                print('Sorry, the rate should be under 100.')
                continue
            
            elif rate < 0:
                print('Sorry, the rate should be a positive number.')
                continue
                
            else:
                return rate
                break
                
        except ValueError:
            print('Please enter a valid number.')

def enter_loan():
    
    while True:
         
        try:
            loan = float(input('Enter the loan(in dollars): '))
            
            if loan < 10000:
                print('Sorry, the minimum loan is 10000 dollars.')
                continue
            
            elif loan < 0:
                print('Sorry, the loan should be a positive number.')
                continue
                
            else:
                return loan
                break
                
        except ValueError:
            print('Please enter a valid number.')

if __name__ == '__main__':
    
    terms = enter_terms()
    rate = enter_rate()
    loan = enter_loan()
    
    monthly_rate = rate / 12 /100
    months = terms * 12
    monthly_payback_rate = (((1 + monthly_rate) ** months) * monthly_rate) / ((( 1 + monthly_rate) ** months) -1)
    monthly_payment = loan * monthly_payback_rate

# 每月應付本息金額之平均攤還率＝
# {[(1＋月利率)^月數]×月利率}÷{[(1＋月利率)^月數]－1}
# 平均每月應攤付本息金額＝貸款本金×每月應付本息金額之平均攤還率

    print(f'Your monthly payment is {monthly_payment:.2f} dollars.')