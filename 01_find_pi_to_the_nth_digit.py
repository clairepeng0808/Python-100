#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr  8 16:06:50 2020

@author: clairepeng

**Find PI to the Nth Digit** - 

Enter a number and have the program generate &pi; 
(pi) up to that many decimal places. Keep a limit 
to how far the program will go.

"""

from math import pi
from math import e


class Game:

    def __init__(self, name):
        self.name = name

    def greeting(self):
        print(
            f'\n\nEnter a number and have the program generate {self.name} up to that many decimal places.')

    def result(self, answer):
        print(f'Thank you! Your {self.name} is {self.answer}\n\n\n\n\n')

    def enter_number(self):

        while True:

            try:
                num = int(
                    input(f'please enter a number of your {self.name} decimal places.'))

            except ValueError:
                print('Please enter an integer!')

            except Exception as e:
                print('Please re-enter a number!')

            else:
                if num <= 0:
                    print('Please enter a positive number.')
                else:
                    return num


class PiGame(Game):
    def __init__(self):
        super().__init__(name="pi")

    def generate_pi(self, n):
        return round(pi, n)

    # x = generate_pi(4)
    # print(x)


class EGame(Game):
    def __init__(self):
        super().__init__(name="e")

    def generate_e(self, n):
        return round(e, n)

    # x = generate_pi(4)
    # print(x)


def choose_game():

    global is_pi_game
    global is_e_game

    while True:
        game = input(
            'What generator would you like to choose? pi or e').lower()[0]

        if game == 'p':
            is_pi_game = True
            break

        elif game == 'e':
            is_e_game = True
            break

        else:
            print('Please choose a generator. pi or e')
            continue


if __name__ == "__main__":

    is_pi_game = False
    is_e_game = False

    while True:

        print('Hello, welcome to generator!')
        choose_game()

        if is_pi_game == True:

            pi_game = PiGame()
            pi_game.greeting()
            num = pi_game.enter_number()
            answer = pi_game.generate_pi(num)
            pi_game.result()

        elif is_e_game == True:
            e_game = EGame()
            e_game.greeting()
            num = e_game.enter_number()
            answer = e_game.generate_e(num)
            e_game.result()
