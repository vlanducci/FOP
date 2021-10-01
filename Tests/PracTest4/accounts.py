#
#  Practical Test 3 
#
#  accounts.py - class for bank accounts
#  
#  Student Name   : Viola Landucci
#  Student Number : 20769446
#  Date/prac time : 01/10/2021
#
class BankAccount ():
    interest_rate = 0.5  # class variable interest_rate
    fee = 20  # class variable fee
    def __init__(self, name, number, balance):
        self.name = name  # instance variable name
        self.num = number  # instance variable number
        self.bal = balance  # instance variable balance

    def withdraw(self, amount):
        if self.bal < amount:
            raise ValueError("Exception: Withdrawal exceeds balance")
        else:
            self.bal = self.bal - amount


    def deposit(self, amount):
        self.bal = self.bal + amount

    def add_interest(self):
        self.bal += self.bal * self.interest_rate
    
    def charge_fees(self):
        self.bal = self.bal - self.fee

