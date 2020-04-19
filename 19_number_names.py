#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 17 16:30:45 2020

@author: clairepeng

Number Names - Show how to spell out a number in English. 
You can use a preexisting implementation or roll your own, 
but you should support inputs up to at least one million 
(or the maximum value of your language's default bounded 
integer type, if that's less). Optional: Support for inputs 
other than positive integers (like zero, negative integers, 
and floating-point numbers).

"""
def enter_num():
    
    while True:
        
        try:
            num = int(input('Please enter a number: '))
            
            if num > 1000000:
                print('Please enter a number less than 1 million.')
                continue
            
            elif num < 0:
                print('Please enter a positive number.')
                continue
                
            return str(num)
        
        except ValueError:
            print('Please enter an integer.')
        
    
number_dict = {
    '0':'zero',
    '1':'one',
    '2':'two',
    '3':'three',
    '4':'four',
    '5':'five',
    '6':'six',
    '7':'seven',
    '8':'eight',
    '9':'nine',
    '10':'ten'
}

ten_digit = {
    '0':'zero',
    '1':'ten',
    '2':'twenty',
    '3':'thirty',
    '4':'forty',
    '5':'fifty',
    '6':'sixty',
    '7':'seventy',
    '8':'eighty',
    '9':'ninety',
}

def get_three(num):
    
    if len(num) == 1:
        print(number_dict[num])
    

    elif len(num) == 2:
        tendigit = ten_digit[num[1]]
        unitdigit = number_dict[num[0]]
    
        if num[0] == '0':
            print(f'{tendigit}')
        
        else:
            print(f'{tendigit} {unitdigit}')

    elif len(num) == 3:
        hundigit = number_dict[num[2]]
        tendigit = ten_digit[num[1]]
        unitdigit = number_dict[num[0]]
        
        if num[0] == '0' and num[1] == '0':
            print(f'{hundigit} hundred')
        
        elif num[1] == '0':
            print(f'{hundigit} hundred and {unitdigit}')
        
        elif num[0] == '0':
            print(f'{hundigit} hundred and {tendigit}')
            
        else:
            print(f'{unitdigit} hundred and {tendigit} {unitdigit}')

def slice(num):
    reversed = num[::-1]
    li = []

    for i in range(0,len(reversed),3):
        li.append(reversed[i:i+3])
    return li

if __name__ == '__main__':
    num = enter_num()[::-1]
    sliced = slice(num)
    get_three(sliced)
    
    
    
    











        
        

