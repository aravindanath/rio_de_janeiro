

"""
Classes - Object Oriented Programming

Python is an object oriented programming language.

Almost everything in Python  class is an object, with its properties and methods.

A Class is like an object constructor, or a "blueprint" for creating objects.


The self Parameter

SELF

The self parameter is a reference to the current instance of the class,
 and is used to access variables that belongs to the class.

It does not have to be named self , you can call it whatever you like,
but it has to be the first parameter of any function in the class:
"""

class Calculator():



    def addNum(self,a,b):
        z = a+b
        print("Addition of two num is: ",z)

    def subNum(self, a, b):
        z = a - b
        print("Sub of two num is: ", z)



c = Calculator()
c.addNum(22,33)
c.subNum(322,333)