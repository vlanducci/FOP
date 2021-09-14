#
# fileAnimals.py - uses classes to assign animals
#

from animals import Cat
from animals import Dog
from animals import Bird

aFile = open('animals.csv', 'r')
data = aFile.readlines()
aFile.close()
print(data)

self = []
name = []
dob = []
colour = []
breed = []

for line in data:
    splitline = line.split(",")
    self.append(splitline[0])
    name.append(splitline[1])
    dob.append(splitline[2])
    colour.append(splitline[3])
    breed.append(splitline[4])

for i in range(0, len(self)):
    if self[i] == "Dog":
        self[i] = Dog(name[i], dob[i], colour[i], breed[i])
    if self[i] == "Cat":
        self[i] = Cat(name[i], dob[i], colour[i], breed[i])
    if self[i] == "Bird":
        self[i] = Bird(name[i], dob[i], colour[i], breed[i])
    self[i].printit()
    print()

