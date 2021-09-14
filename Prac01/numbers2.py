#
# numbers2.py: Read in ten numbers and give sum of numbers
#

total = 0

loopNum = int(input("How many numbers do you want to add?: "))

for i in range(loopNum):
    number = int(input("Enter number " + str(i+1) + " : "))
    total = total + number

    print(total)

