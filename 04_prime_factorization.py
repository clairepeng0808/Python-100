#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr  9 16:52:46 2020

@author: clairepeng

Prime Factorization - 
Have the user enter a number and find all Prime Factors 
(if there are any) and display them.

"""

def enter_num():
    
    while True:

        try:
            num = int(input('Please enter an integer.'))
        
        except ValueError:
            print('Please enter an integer')
        
        except Exception as e:
            print(e)
            print('Error! Please re-enter a number.')
            
        else: 
            if num > 0:
                return num
                break
            
            else:
                print('Please enter a positive number.')
                continue
            

print('Welcome to prime factory game. Enter a number and I will display its prime factors.')    

num = enter_num()

for n in range(2,num+1):
    if (num % n == 0):
        isprime = 1
        
        for j in range(2,n//2 +1):
            if (n%j == 0):
                isprime = 0
                break
        
        if (isprime == 1):
            print(f'{n} is a prime factor of a given number {num}')