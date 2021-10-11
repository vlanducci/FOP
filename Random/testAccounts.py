#
#  Practical Test 4
#
#  testAccounts.py - program to test functions of accounts.py
#  
#  Student Name   :
#  Student Number :
#  Date/prac time :
#
from accounts import BankAccount

def balances():
    print('\n#### Balances of All Accounts####\n')
    total = 0
    for i in range(len(my_accounts)):
        print("Name: ", my_accounts[i].name, "\tNumber: ", my_accounts[i].num, \
              "\tBalance: ", my_accounts[i].bal)
        total = total + my_accounts[i].bal
    print("\t\t\t\t\tTotal: ", total)

print('\n#### Bank Accounts ####\n')
my_accounts = []

# add code for tasks here

balances()