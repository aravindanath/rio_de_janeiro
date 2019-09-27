
"""
https://www.geeksforgeeks.org/class-method-vs-static-method-python/
"""

class TypeOfMethods():

    def __init__(self):
        print("I am a constructor")

    def normalMethod(self):
        print("Normal method")

    @classmethod
    def classMethod(cls):
        print("class method")

    @staticmethod
    def staticMethod():
        print("static method")

#  THis is the object of the class
# t = TypeOfMethods()
# t.normalMethod()
# t.classMethod()

class TypeOfMethods2():

    def normalMethod(self):
        TypeOfMethods.staticMethod()


obj =  TypeOfMethods2();
obj.normalMethod()






