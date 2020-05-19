#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 24 23:02:38 2020

@author: clairepeng
"""
import os.path
import json


def get_project_root(path=__file__):
    directory = os.path.dirname(path)

    while directory != '/':
        p = os.path.join(directory, 'requirements.txt')
        if os.path.isfile(p):
            return directory
        else:
            directory = os.path.dirname(directory)
    return None


def replay(string):

    while True:

        replay = input(f'Are you going to {string}? y or n: ').lower()[0]

        if replay != 'y' and replay != 'n':
            continue

        elif replay == 'y':
            return True

        else:
            print('Goodbye!')
            return False
