



class Constructor():

    def __init__(self):
        print("I am constructor")

    def method(self):
        print("i am method")


    def addNum(self,a,b):
        sumofnum = a + b
        return sumofnum

    def subNum(self,a,b):
        sub =  a -b
        print(sub)

c = Constructor()
c.method()
var = c.addNum(1,2)
print(var)
var = c.subNum(44,88)
print(var)