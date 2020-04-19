#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr 11 17:08:16 2020

@author: clairepeng

Binary to Decimal and Back Converter - 
Develop a converter to convert a decimal number to 
binary or a binary number to its decimal equivalent.
"""

def pick_converter():
    
    global d_to_b
    global b_to_d
        
    while True:
        
        converter = input('Which converter are you going to use? ''d'' stands for decimal to binary, "b" stands for binary to decimal: ').lower()[0]
    
        if converter != 'd' and converter != 'b':
            print('\nPlease enter d or b.')
            continue
        
        elif converter == 'd':
            d_to_b = True
            break
        
        elif converter == 'b':
            b_to_d = True
            break
    

def enter_number():
    
    while True:
        
        try:
            number = int(input('Please enter a number: '))
            
            if number < 0:
                print('You must enter a positive number.')
                continue
            
            else:
                return number
                break
        
        except ValueError:
            print('Please enter an integer.')
            continue
        

def decimal_to_binary(decimal):
    
    binary_list = []
    
    while (decimal // 2) >= 1:
        remainder = decimal % 2
        binary_list.append(remainder)
        decimal = decimal // 2
        
    binary_list.append(decimal)
    binary_list.reverse()
    binary = map(str,binary_list)
    return ''.join(binary)

def binary_to_decimal(binary):
    
    binary_list = [int(i) for i in str(binary)]
    
    binary = 1
    # [1,0,1,0,0]
    # for i, x in enumerate(binary_list):
    for i in range(len(binary_list)-1):
        binary = binary * 2 + binary_list[i+1]
    
    return binary



while True:
    
    d_to_b = False
    b_to_d = False
    
    pick_converter()
    
    if d_to_b:
        num = enter_number()
        converted_num = decimal_to_binary(num)
        print(f'The binary of {num} is {converted_num}.')
    
    if b_to_d:
        num = enter_number()
        converted_num = binary_to_decimal(num)
        print(f'The binary of {num} is {converted_num}.')

