#
# banking.py - simulating bank account transactions
#

from accounts import BankAccount

loop = True
accounts = []

def balances():
  total = 0
  for i in range(len(accounts)):
    print(i)
    print("Name:", accounts[i].name, "\tNumber: ", accounts[i].number, "\tBalance: ", accounts[i].balance)
    total += accounts[i].balance
  print("\t\t\t\t\tTotal: ", total)

print("\n---------- BANK ACCOUNT TRANSACTIONS ----------\n")

# Create Account: 
name = input("Enter name: ")
num = input("Enter number: ")
bal = int(input("Enter balance: "))
bank = BankAccount(name, num, bal)
accounts.append(bank)
balances()


while loop:
  choice = (input("\nSelect Transactions - \nW for Withdrawal, D for deposit, I for interest, B for balance and X for exit: ")).upper()
  
  if choice == "W":
    amount = int(input("Amount: "))
    accounts[0].withdraw(amount)

  elif choice == "D":
    amount = int(input("Amount: "))
    accounts[0].deposit(amount)

  elif choice == "I":
    accounts[0].add_interest()

  elif choice == "B":
    balances()

  elif choice == "X":
    loop == False

print("\nGoodbye :)\n")



    



