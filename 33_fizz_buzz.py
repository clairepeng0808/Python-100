#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 24 22:42:13 2020

@author: clairepeng

**Fizz Buzz**

Write a program that prints the numbers from 1 to 100. 
But for multiples of three print “Fizz” instead of the 
number and for the multiples of five print “Buzz”. 
For numbers which are multiples of both three and 
five print “FizzBuzz”.

"""

for n in range(1,101):
    
    if n % 15 == 0:
        print('FizzBuzz')
    
    elif n % 3 == 0:
        print('Fizz')
    
    elif n % 5 == 0:
        print('Buzz')
    
    else:
        print(n)