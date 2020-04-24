#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 24 23:02:38 2020

@author: clairepeng
"""

def replay():
    
    while True:
        
        replay = input('Are you going to replay? y or n: ').lower()[0]
        
        if replay != 'y' and replay != 'n':
            continue
        
        elif replay == 'y':
            return True
        
        else:
            print('Goodbye!')
            return False


