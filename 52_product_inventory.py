#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 30 14:27:57 2020

@author: clairepeng

**Product Inventory Project** - Create an application 
which manages an inventory of products. 
Create a product class which has a price, id, and quantity on hand. 
Then create an *inventory* class which keeps track of various 
products and can sum up the inventory value.

"""


class Product:

    def __init__(self, price, id_, quantity):
        self.price = price
        self.id_ = id_
        self.quantity = quantity
        self.value = price*quantity


class Inventory:

    def __init__(self):
        self.inventory = {}
        self.value = 0

    def add_to_inventory(self, product):
        self.inventory.update({product.id_: product.value})
        self.value += (product.price)*(product.quantity)
        print(f'\n\nThe product {product.id_} is added to the inventory!')

    def __str__(self):
        inventory = ', '.join(list(self.inventory.keys()))
        return f'Your total inventory: {inventory}' + '\n' + f'The total value of your inventory is {self.value} dollars.'


def choose():

    while True:
        choice = input(
            '"c" for checking total inventory value, "a" for adding an item: ').lower()[0]

        if choice == 'c':
            return 'c'

        elif choice == 'a':
            return 'a'

        else:
            continue


def add_id():

    while True:
        id_ = input('Please enter the item id: ')

        if len(id_) != 3:
            print('ID should be a 3-digit number')

        elif id_ in inventory.inventory.keys():
            print('The ID is taken.')

        else:
            return id_


def add_price():

    while True:

        try:
            price = float(input('Please enter the item unit price(dollars): '))

        except ValueError:
            print('Please enter a valid price.')

        else:

            if price <= 0:
                print('Please enter a valid price.')

            else:
                return price


def add_quantity():

    while True:

        try:
            quantity = int(input('Please enter the item quantity: '))

        except ValueError:
            print('Please enter a positive integer.')

        else:
            if quantity <= 0:
                print('Please enter a positive integer.')

            else:
                return quantity


def add_item(inventory):

    id_ = add_id()
    price = add_price()
    quantity = add_quantity()
    product = Product(price, id_, quantity)
    inventory.add_to_inventory(product)


def select_inventory(inventory):

    while True:

        select = input(
            'What product would you like to check? Please enter the product id:  ')

        if len(select) != 3:
            print('ID should be a 3-digit number')

        elif select not in inventory.inventory.keys():
            print('Product not found.')

        else:
            product_value = inventory.inventory.get(select)
            print(
                f'The value of the product {select} is {product_value} dollars.')
            break


if __name__ == '__main__':

    print('\nWelcome to the Inventory Checker!\n')
    inventory = Inventory()

    while True:

        choice = choose()

        if choice == 'a':
            add_item(inventory)

        elif choice == 'c':
            print(inventory)
            select_inventory(inventory)
