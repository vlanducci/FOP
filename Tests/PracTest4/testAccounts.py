#
#  Practical Test 4
#
#  testAccounts.py - program to test functions of accounts.py
#  
#  Student Name   : Viola Landucci
#  Student Number : 20769446
#  Date/prac time : 01/10/2021
#
from accounts import BankAccount

my_accounts = []

def balances():
    print('\n#### Balances of All Accounts####\n')
    total = 0
    for i in range(len(my_accounts)):
        print("Name: ", my_accounts[i].name, "\tNumber: ", my_accounts[i].num, \
              "\tBalance: ", my_accounts[i].bal)
        total = total + my_accounts[i].bal
    print("\t\t\t\t\tTotal: ", total)

print('\n#### Bank Accounts ####\n')
account1 = BankAccount("Savings", "200000-1", 2000)
account2 = BankAccount("Everyday", "200000-2", 200)
my_accounts.append(account1)
my_accounts.append(account2)

balances()

# add code for tasks here
my_accounts[0].deposit(200)

try:
    my_accounts[1].withdraw(20)
except ValueError as error:
    print(error)

try:
    my_accounts[0].withdraw(2000)
except ValueError as error:
    print(error)

my_accounts[0].add_interest()
my_accounts[1].add_interest()

my_accounts[0].charge_fees()
my_accounts[1].charge_fees()

balances()