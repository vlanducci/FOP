#
# testPeople.py - uses classes to assign people
#

from people import Address, Person, Staff, Postgrad, Student, Undergrad

def processlist(linelist):
  address = []
  newlist = linelist.split(':')

  address = (newlist[3]).split(",")
  number = (newlist[3])[:1]
  street = (newlist[3])[2:]

  testAdd = Address(number, street, address[1], address[2])

  if newlist[0] == "Person":
    testPerson = Person(newlist[1], newlist[2], testAdd)
  elif newlist[0] == "Student":
    testPerson = Student(newlist[1], newlist[2], testAdd, newlist[4])
  elif newlist[0] == "Postgrad":
    testPerson = Postgrad(newlist[1], newlist[2], testAdd,newlist[4])
  elif newlist[0] == "Undergrad":
    testPerson = Undergrad(newlist[1], newlist[2], testAdd,newlist[4])
  elif newlist[0] == "Staff":
    testPerson = Staff(newlist[1], newlist[2], testAdd,newlist[4])
  testPerson.displayPerson()
  print()


print('#### People Test Program ###')

try:
  with open('people.csv', 'r') as f:
    lines = f.readlines()
except OSError as err:
  print('Error with file open: ', err)
except:
  print('Unexpected error: ', err) 

for i in lines:
  processlist(i)


# testAdd = Address('10', 'Downing St', 'Carlisle', '6101')
# testPerson = Person('Winston Churchill', '30/11/1874', testAdd)
# testPerson.displayPerson()
# print()

# testAdd2 = Address('1', 'Infinite Loop', 'Hillarys', '6025')
# testPerson2 = Staff('Professor Awesome', '1/6/61', testAdd2, '12345J')
# testPerson2.displayPerson()
# print()

# testAdd2 = Address('1', 'Infinite Loop', 'Hillarys', '6025')
# testPerson2 = Student('Professor Awesome', '1/6/61', testAdd2, '12345J')
# testPerson2.displayPerson()
# print()

# testAdd2 = Address('1', 'Infinite Loop', 'Hillarys', '6025')
# testPerson2 = Postgrad('Professor Awesome', '1/6/61', testAdd2, '2222')
# testPerson2.displayPerson()
# print()

# testAdd2 = Address('1', 'Infinite Loop', 'Hillarys', '6025')
# testPerson2 = Undergrad('Professor Awesome', '1/6/61', testAdd2, '2222')
# testPerson2.displayPerson()
# print()