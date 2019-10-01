class Fruit():
    def __init__(self):
        print("fruits type")
    def Nutrition(self):
        print("vitamin c")
    def FruitShape(self):
       print("oval")

class Banana(Fruit):
    def __init__(self):
        print("fruits type: Banana")
    def Nutrition(self):
        print("Vitamin D")

class Apple(Fruit):
    def __init__(self):
        print("fruits type: Apple")
    def FruitShape(self):
        print("round")
g =Apple()
g.Nutrition()
g.FruitShape()