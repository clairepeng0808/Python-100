#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 19 18:49:00 2020

@author: clairepeng

**Coin Flip Simulation** - 
Write some code that simulates flipping a single coin 
however many times the user decides. The code should 
record the outcomes and count the number of tails and heads.
"""
import random

def flip():
    return random.choice(['tail','head'])

def enter_times():
    
    while True:
    
        try:
            times = int(input('Please enter times you\'d like to flip: '))
            
            if times <= 0:
                print('Please enter a positive number.')
                
            else:
                return times
        
        except ValueError:
            print('Please enter an integer.')

def replay():
    
    while True:
        
        replay = input('Do you want to replay? y or n: ').lower()[0]
        
        if replay != 'y' and replay != 'n':
            continue
        
        elif replay == 'y':
            return True
        
        else:
            return False
    

if __name__ == '__main__':
    
    while True:
    
        times = enter_times()
        
        tail = 0
        head = 0
        
        for _ in range(times):
            
            result = flip()
            
            if result == 'head':
                head += 1
            
            elif result == 'tail':
                tail += 1
        
        print(f'Tail: {tail} times, Head: {head} times')
    
        if not replay():
            break