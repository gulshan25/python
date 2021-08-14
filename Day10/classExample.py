""""
class
A class is a blueprint for the object
An object has two characteristics
1. Attributes/Properties
2. Behavior/Method

Syntax - 
class className(object):
    --snip--

Creating class object
objectName = className(arguments)

"""

class myClass(object):
    '''
    Document String
    This is my first Class
    '''
    a = 20
    def myFunc(self):
        print('Hello')

# obj = myClass()
# obj.myFunc()

print(myClass.a)
print(myClass.__doc__)
print(myClass.__name__)
print(myClass.__base__)

class Parrot():
    # class attribute
    species = "Bird"

    # instance attribute 
    def __init__(self, n, a):
         # pass
         print('This is Parrot Class')
         self.name = n
         self.age = a

tiya = Parrot('Mitu',2)
print(f'{tiya.name} is {tiya.age} years old')
print(f'{tiya.name} is {tiya.species}')
print(tiya.__class__)
# tota = Parrot()
# doel = Parrot()






