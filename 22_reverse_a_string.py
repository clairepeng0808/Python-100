#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 24 22:46:56 2020

@author: clairepeng

**Reverse a String** - 
Enter a string and the program will reverse it and print it out.
"""

def enter_string():
    
    while True:
        
        try:
            s = str(input('Please enter a string: '))
            return s
        
        except ValueError:
            print('Incorrect format! Please enter a string: ')
            continue

import utility

while True:
    string = enter_string()
    print(string[::-1])
    
    if not utility.replay():
        break