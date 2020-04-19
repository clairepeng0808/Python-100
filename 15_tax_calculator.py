#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 14 14:59:49 2020

@author: clairepeng

**Tax Calculator** - 
Asks the user to enter a cost and either a country 
or state tax. It then returns the tax plus the total cost with tax.
"""

tax_rates = {
    'CAN':.05,
    'UK':.2,
    'JAP':.08,
    'TW' : .07
}

def enter_cost():
    
    while True:
        
        try:
            cost = float(input('Please enter a cost: '))
            break
        
        except ValueError:
            print('Cost must be a number.')
            continue
    
    return cost


def enter_country():
    
    while True:
        
        try:
            country = input('Please enter a country code (CAN,UK,JAP,TW): ').upper()
            return tax_rates[country]
    
        except KeyError:
            print('Please enter the country code in the list.')
            continue
        
        
        # 1. key not in tax_rates
        # 2. KeyError
        # 3. if tax_rates.get(key):
        
    
if __name__ == '__main__':
    
    print('Welcome to tax calculator.')
    
    while True:
        

        cost = enter_cost()
        rates = enter_country()
        
        total_tax = cost * rates
        total_cost_with_tax = cost * (1+rates)
        
        print(f'\nThe total tax is {total_tax:.2f} dollars, and the total cost with tax is {total_cost_with_tax:.2f} dollars.')
