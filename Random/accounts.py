#
#  Practical Test 3 
#
#  accounts.py - class for bank accounts
#  
#  Student Name   :
#  Student Number :
#  Date/prac time :
#
class BankAccount ():
    interest_rate = 0.3
    def __init__(self, name, number, balance):
        self.name = name
        self.num = number
        self.bal = balance

    def withdraw(self, amount):
        self.bal = self.bal - amount

    def deposit(self, amount):
        self.bal = self.bal + amount

    def add_interest(self):
        self.bal += self.bal * self.interest_rate

