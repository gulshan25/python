"""
Encapsulation - Data Hiding
We can restrict access to method
and variable.
This prevent data from direct modification which
is called Encapsulation

"""

class Computer:
    def __init__(self):
        self.__maxprice = 900 #__prefix used for private Attribute

    def sell(self):
        print(f'Selling price is {self.__maxprice}')

    def setMaxprice(self,price):
        self.__maxprice = price

    def __str__(self):
        return f'Compter-er daam {self.__maxprice}'

c = Computer()
c.sell()

c.__maxprice = 2000
c.sell()

c.setMaxprice(3000)
c.sell()
print(c)
