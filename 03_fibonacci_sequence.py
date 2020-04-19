#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr  8 18:08:45 2020

@author: clairepeng

Fibonacci Sequence - 
Enter a number and have the program generate the 
Fibonacci sequence to that number or to the Nth number.
"""
def gen_fibon(n):
    
    a = 1
    b= 1
    
    for i in range(n):
        yield a
        
        a, b = b, a+b

if __name__ == '__main__':
    
    
    print('Welcome to Fibonacci generator!')
    
    while True:
    
        try:   
            n = int(input('Please enter the number as the length of your fibon sequence'))
    
        except ValueError:
            print('Please enter an integer')
        
        except Exception as e:
            print('Error! Please re-enter the number.')
            print(e)
        
        else:
            if n > 100:
                print('Please enter a number less than 100.')
                continue
                
            elif n <= 0:
                print('Please enter a positive number!')
                continue
                    
            else:
                print(list(gen_fibon(n)))
                break
                
            
    print('\n\nI am live coding!!!')