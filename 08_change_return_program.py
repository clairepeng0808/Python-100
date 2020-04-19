#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr  9 18:53:27 2020

@author: clairepeng

Change Return Program - 
The user enters a cost and then the amount of money given. 
The program will figure out the change and the number of 
quarters, dimes, nickels, pennies needed for the change.
"""

def enter_cost():
    
    while True:
        try:
            cost = round(float(input('Please enter the cost.')),2)
            
            if cost <= 0:
                print('The cost must be a positive number!')
                continue
            else:
                return cost
                break
        
        except ValueError:
            print('Please enter a number.')
            continue
            

def enter_paid():
    
    while True:
        
        try:
            paid = round(float(input('Please enter the money you paid.')),2)
            
            if paid < cost:
                print('\nYour paid amount must exceed the cost.')
                continue
            
            else:
                return paid
                break
        
        except ValueError:
            print('Please enter a number.')
            continue            
    

if __name__ == '__main__':
    
    print('Welcome to the change return program!')
    
    while True:
        
        cost = enter_cost()
        paid = enter_paid()
        change = paid - cost
        
        if change >= 1:
            print('Error! The change must be under 1 dollar.')
            continue
        
        elif change < 0:
            print('Error! Your paid amount must exceed your cost.')
            
        elif change == 0:
            print("There's no change.")
            break
        
        else:
            # Tony's solution
            coins = [0.25, 0.1, 0.05, 0.01]
            used = []
            left = change
            for c in coins:
                c_used = left // c
                left -= ((c_used) * c)
                used.append(c_used)
            
            # Claire's solution
            quarters = change // 0.25
            # left = (change % 0.25)
            dimes = (change % 0.25) // 0.1
            # left = (change % 0.25) % 0.1
            nickles = ((change % 0.25) % 0.1) // 0.05
            # left = (left % 0.05) % 0.1
            pennies = (round((((change % 0.25) % 0.1) % 0.05),2) // 0.01) 
        
            print(f'You will receive {change:.2f} dollars in change.')
            print(f'You will get {quarters:.0f} quarters, {dimes:.0f} dimes, {nickles:.0f} nickles, and {pennies:.0f} pennies.')
            break