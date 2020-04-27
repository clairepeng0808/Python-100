#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 27 15:52:44 2020

@author: clairepeng

**Check if Palindrome** - Checks if the string entered by the user 
is a palindrome. That is that it reads the same forwards as backwards 
like “racecar”
"""
from utility import utility as util

def enter_string():
    string = input('Enter a string: ').lower()    
    return string

def check_palindrome(string):
    
    if string[:] == string[::-1]:
        return True
    else:
        return False
    

while True:
    string = enter_string()
    print(string)
    string.reverse()
    print(string)
    
    if check_palindrome(string):
        print(f'Congrats! The string \'{string}\' is a palindrome.')
    
    else:
        print(f'Sorry, the string \'{string}\' is not a palindrome.')
    
    if not util.replay():
        break