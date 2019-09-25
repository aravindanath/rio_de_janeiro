
# Parent class
class Cars():

    def wheels(self,no):
        print(no," of Wheels")

    def doors(self,no):
        print(no, " of Doors")

    def colour(self, col):
        print(col, " of car")

# Child class
class BMW(Cars):

    def bmwWheels(self):
        Cars.wheels(self,4)
        print("BMW is having spare wheel")


b = BMW()
b.wheels(3)
b.bmwWheels()