#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 29 18:02:31 2020

@author: clairepeng

**Count Words in a String** - Counts the number of individual 
words in a string. For added complexity read these strings in from 
a text file and generate a summary.
"""

from utility import utility as util

def choose_file_type():
    
    global game
    
    while True:
        
        choice = input('Do you want to start with manual input or from a text file? m for manual input, and t for text file: ').lower()[0]
        
        
        if choice == 'm':
            game = 'm'
            break
        
        elif choice == 't':
            game = 't'
            break
        
        else:
            print('Please enter "m" or "t".')

def count_input():
    string = input('Please enter a string: ').strip().split()
    
    if len(string) in {0,1}:
        print(f'There is {len(string)} word in your string.')
    
    else:
        print(f'There are {len(string)} words in your string.')

def enter_file_name():
    
    while True:
        
        try:
            filename = input('Please input the filename: ')
            f = open(filename, "r")
            a = f.read().strip().split()
        
        except FileNotFoundError:
            print('File not Found.')
        
        else:
            
            if len(a) in {0,1}:
                print(f'There is {len(a)} word in your string.')
                break
    
            else:
                print(f'There are {len(a)} words in your string.')
                break
        

if __name__ == '__main__':
    
    while True:
        
        game = ''
        choose_file_type()
        
        if game == 'm':
            count_input()
        
        else:
            enter_file_name()
    
        if not util.replay():
            break
    