'''
Bank Account Manager - Create a class called Account which will be an
abstract class for three other classes called CheckingAccount,
SavingsAccount and BusinessAccount. Manage credits and debits
from these accounts through an ATM style program.
'''

from utility import utility as util


class Account:

    def __init__(self, category, initial_balance):
        self.balance = initial_balance
        self.category = category

    def deposit(self, amount):
        self.balance += amount
        print(
            f'Success. Your {self.category} account balance: {self.balance} dollars.')

    def withdraw(self, amount):
        self.balance -= amount
        print(
            f'Success. Your {self.category} account balance: {self.balance} dollars.')


class CheckingAccount(Account):

    def __init__(self, category, initial_balance):
        super().__init__(category, initial_balance)


class SavingsAccount(Account):

    def __init__(self, category, initial_balance):
        super().__init__(category, initial_balance)


class BusinessAccount(Account):

    def __init__(self, category, initial_balance):
        super().__init__(category, initial_balance)


def choose_account():

    while True:
        account = (input(
            'Please select a type of account: '
            'c for checking account, s for savings account, '
            'and b for business account: ').lower()
            or " ")[0]

        if account == 'c':
            return 'checking'
        elif account == 's':
            return 'savings'
        elif account == 'b':
            return 'business'
        else:
            print('Invalid input.')


def choose_operation():

    while True:

        o = input(
            'c for check balance, d for deposit, w for withdrawal: ').lower()[0]

        if o in {'c', 'd', 'w'}:
            return o
        else:
            print('Invalid input.')


def input_amount():
    while True:
        try:
            amount = int(
                input('Please enter the amount (in dollars): '))

            if amount <= 0:
                print('The amount should be no less than 0 dollars.')

            return amount

        except ValueError:
            print('Please enter a valid number.')


if __name__ == '__main__':

    checking = CheckingAccount('checking', 10000)
    savings = SavingsAccount('savings', 20000)
    business = BusinessAccount('business', 0)

    accounts = {
        'checking': checking,
        'savings': savings,
        'business': business,
    }

    while True:
        choice = accounts[choose_account()]
        operation = choose_operation()

        if operation == 'c':
            print(
                f'Your {choice.category} account balance: {choice.balance} dollars.')

        elif operation == 'd':
            amount = input_amount()
            choice.deposit(amount)

        elif operation == 'w':
            amount = input_amount()
            if amount > choice.balance:
                print('Insufficient balance.')
            else:
                choice.withdraw(amount)

        if not util.replay('perform any other actions'):
            break
