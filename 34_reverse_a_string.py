#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 24 22:46:56 2020

@author: clairepeng

**Reverse a String** - 
Enter a string and the program will reverse it and print it out.
"""

def enter_string():
    
     s = str(input('Please enter a string: '))
     return s


from utility import utility as util

while True:
    string = enter_string()
    print(f'Your reversed string is "{string[::-1]}".')
    
    if not util.replay():
        break