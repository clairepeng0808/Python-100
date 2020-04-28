#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 27 15:16:48 2020

@author: clairepeng

**Count Vowels** - Enter a string and the program counts the number 
of vowels in the text. For added complexity have it report a sum 
of each vowel found.
"""

import itertools 
from utility import utility as util

vowels = ['a','e','i','o','u']

def enter_string():
    string = input('Enter a string: ').lower()    
    return string
        

def count_vowel(string):   
    count = [i for i in string if i in vowels]
    #for i in string:
    #    if i in vowels:
    #        count.append(i)
    return count
    
def return_sum(count):
    group = []
    for k,g in itertools.groupby(sorted(count)):
        group.append((k,len(list(g))))
    return group
        
while True:
    
    string = enter_string()
    count = count_vowel(string)
    sum_vowels = return_sum(count)
    group = return_sum(count)
    
    print(f'I found {len(count)} vowels in the string!')
    
    for l,t in group:
        if t == 1:
            print(f'Vowel \'{l}\': found {t} occurence')
        else:
            print(f'Vowel \'{l}\': found {t} occurences')
    
    if not util.replay():
        break