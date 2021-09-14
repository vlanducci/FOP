#
# bucket2.py - bucket list builder
#

print("\nBUCKET LIST BUILDER\n")

bucket = []

choice = input("Enter selection: e(X)it, (A)dd, (L)ist, (D)elete: ")
choice = choice.upper()

while choice[0] != "X":
    if choice[0] == "A":
        newItem = input("Enter list item: ")
        bucket.append(newItem)
    elif choice[0] == "L":
        counter = 1
        for item in bucket:
            print(counter, item)
            counter = counter+1
    elif choice[0] == "D":
        delItem = int(input("Item name or number on list: "))
        del bucket[delItem]
    else:
        print("Invalid selection.")                                                     choice = input("Enter selection: e(X)it, (A)dd, (L)ist, (D)elete: ")
    choice = choice.upper()

print("\nGOODBYE!\n")
