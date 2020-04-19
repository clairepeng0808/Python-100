#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 15 15:42:55 2020

@author: clairepeng
"""


def enter_num():
    
    while True:
        
        try: 
            num = int(input('Please enter a number: '))
            return num
            
        except ValueError:
            print('Please enter a positive integer.')


def fac(num):
    
    fac = 1
    for i in range(num):
        
        fac *= (i+1)
    
    return fac


while True:
    
    num = enter_num()
    factorial = fac(num)
    print(f'The result of {num}! is {factorial}.')