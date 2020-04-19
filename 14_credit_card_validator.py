#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 13 15:37:14 2020

@author: clairepeng

**Credit Card Validator** - 
Takes in a credit card number from a common credit card vendor 
(Visa, MasterCard, American Express, Discoverer) and 
validates it to make sure that it is a valid number 
(look into how credit cards use a checksum).

"""

def enter_num():
    
    while True:
        ccnum = input('Please enter your credit card number: ')
        
        if len(ccnum) != 16:
            print('There should be 16 digits.')
            continue
        
        elif ccnum.isdigit() != True:
            print('Please enter 16-digit numbers!') 
        
        else:
            return str(ccnum)
            break
                
# Starting with the first digit, multiply every second digit by 2:
def multiply_digit(l):
    ccnum_list = []
    for i, e in enumerate(l):
        if i % 2 == 0:
            ccnum_list.append(e*2)
        else:
            ccnum_list.append(e)
    return ccnum_list

# Every time you have a two-digit number, 
# just add those digits together for a one-digit result:
def add_two_digits(l):
    ccnum_list = [i-9 if i >= 10 else i for i in l]
    return ccnum_list

# Finally, add all the numbers together:
def add_all_num(l):
    n = 0
    for i in l:
        n += i
    return n

def replay():
    
    
    while True:
        
        replay = input('Do you want to re-enter your credit cards number?').lower()[0]
        
        if replay != 'y' and replay!='n':
            continue
        
        elif replay == 'y':
            return True
    
        elif replay == 'n':
            return False
            print('Goodbye!')

if __name__ == '__main__':

    print('Welcome to credit card validator!')

    while True:
        
        ccnum = enter_num()
        ccnum_list = [x for x in ccnum]
        check_digit = ccnum_list.pop()
        ccnum_list = map(int,ccnum_list)
        
        ccnum_list = multiply_digit(ccnum_list)
        ccnum_list = add_two_digits(ccnum_list)
        ccnum_list = add_all_num(ccnum_list)
        
        
        # When this number is added to the check digit, 
        # then the result must be an even multiple of 10.
        
        if (ccnum_list + int(check_digit)) % 10 == 0:
            print(f'This is valid credit card number!')
        
        else:
            print(f'It is invalid credit card number.')
        
        
        if not replay():
            break