#
# number3.py: Read in a list of numbers (negative to exit) and give the sum of the numbers
#

count = 0
total = 0
number = int(input("Enter number to add. Enter 0 or a  negative number to exit: "))

while number > 0:
    total += number
    count += 1
    number = int(input("Next number: "))

    print("Total:", str(total), "\nCount:", str(count))

