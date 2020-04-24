#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 24 23:46:12 2020

@author: clairepeng

**Pig Latin** - 

Pig Latin is a game of alterations played on the English language game. 
To create the Pig Latin form of an English word the initial consonant 
sound is transposed to the end of the word and an ay is affixed 
(Ex.: "banana" would yield anana-bay). 

Read Wikipedia for more information on rules.
"""

cons_clusters = {'sm','st','gl','tr','fl'}
vowels = {'a','e','i','o','u'}

def enter_string():
    
    while True:
        
        s = input('Please enter a word: ')
        
        if s.isalpha() == False:
            print('Please enter only one word with English letters:')
            continue
        
        else:
            return s


from utility import utility as util

while True:  
    
    s = enter_string()
    
    if s[0:2] in cons_clusters:
        print(s[2:] + s[0:2] + "ay")
    
    elif s[0] in vowels:
        print(s[:] + "ay")
    
    elif s[0] not in vowels:
        print(s[1:] + s[0] + "ay")
        
    if not util.replay():
        break