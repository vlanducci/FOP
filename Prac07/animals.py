#
# animals.py - classes on animals
#

# class Cat():
#   myclass = "Cat"
#   def __init__(self, name, dob, colour, breed):
#     self.name = name
#     self.dob = dob
#     self.colour = colour
#     self.breed = breed
  
#   def printit(self):
#     print('Name: ', self.name)
#     print('DOB: ', self.dob)
#     print('Colour: ', self.colour)
#     print('Breed: ', self.breed)
#     print('Class: ', self.myclass)

# class Dog():
#   myclass = "Dog"
#   def __init__(self, name, dob, colour, breed):
#     self.name = name
#     self.dob = dob
#     self.colour = colour
#     self.breed = breed
#   def printit(self):
#     print('Name: ', self.name)
#     print('DOB: ', self.dob)
#     print('Colour: ', self.colour)
#     print('Breed: ', self.breed)
#     print('Class: ', self.myclass)

# class Bird():
#   myclass = "Bird"
#   def __init__(self, name, dob, colour, breed):
#     self.name = name
#     self.dob = dob
#     self.colour = colour
#     self.breed = breed

#   def printit(self):
#     print('Name: ', self.name)
#     print('DOB: ', self.dob)
#     print('Colour: ', self.colour)
#     print('Breed: ', self.breed)
#     print('Class: ', self.myclass)
  
class Animal():

  myclass = "Animal"
  
  def __init__(self, name, dob, colour, breed):
    self.name = name
    self.dob = dob
    self.colour = colour
    self.breed = breed

  def __str__(self):
    return(self.name + '|' + self.dob + '|' + self.colour + '|' +
      self.breed)

  def printit(self):
    spacing = 5 - len(self.myclass)
    print(self.myclass.upper(), spacing*' ' + ': ',
      self.name,'\tDOB: ', self.dob,'\tColour: ',
      self.colour,'\tBreed: ', self.breed)

class Dog(Animal):
  myclass = "Dog"

class Cat(Animal):
  myclass = "Cat"

class Bird(Animal):
  myclass = "Bird"

class Shelter():
  def __init__(self, name, address, phone):
    self.name = name
    self.address = address
    self.phone = phone
    self.processing = []
    self.available = []
    self.adopted = []

  def displayProcessing(self):
    print('Current processing list:')
    for a in self.processing:
      a.printit()
    print()

  def displayAvailable(self):
    print("Available:")
    for a in self.available:
      print(" -", a)
    print()

  def displayAdopted(self):
    print("Adopted:")
    for a in self.adopted:
      print(" - ", a)
    print()

  def displayAll(self):
    self.displayProcessing()

  def newAnimal(self, type, name, dob, colour, breed):
    temp = None
    if type == 'Dog':
      temp = Dog(name, dob, colour, breed)
    elif type == 'Cat':
      temp = Cat(name, dob, colour, breed)
    elif type == 'Bird':
      temp = Bird(name, dob, colour, breed)
    else:
      print('Error, unknown animal type: ', type)
    if temp:
      self.processing.append(temp)
      print('Added ', name, ' to processing list')
      self.displayAll()

  def makeAvailable(self, name):
    self.available.append(name)
    
  def makeAdopted(self, name):
    self.adopted.append(name)
    self.available.remove(name)


