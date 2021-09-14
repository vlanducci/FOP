#
# accounts.py - Bank transactions classes
#

class BankAccount ():
  interest_rate = 0.03
  def __init__(self, name, number, balance):
    self.name = name
    self.number = number
    self.balance = balance

  def withdraw(self, amount):
    self.balance = self.balance - amount

  def deposit(self, amount):
    self.balance = self.balance + amount
    
  def add_interest(self):
    self.balance += self.balance * self.interest_rate


