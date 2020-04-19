#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr  9 17:38:08 2020

@author: clairepeng

Find Cost of Tile to Cover W x H Floor - 

Calculate the total cost of tile it would take to cover a 
floor plan of width and height, using a cost entered by the user.

"""
while True:
    
    print('Calculate the total cost of tile it would take to cover a floor plan of width and height')
    
    w = float(input('Please enter the width (in meter): '))
    h = float(input('Please enter the height (in meter): '))
    cost = float(input('Cost of a 1 square meter (usd):'))
    
    if w <= 0 or h<=0 or cost <= 0:
        print('You have to input positive numbers.')
        continue
    
    else:
        print(f'\nThe Total cost of {w:.2f} x {h:.2f} floor plan is {w*h*cost:.2f} dollars.')
        break