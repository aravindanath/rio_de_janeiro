class bangalore:
    def __init__(self):
        print("bangalore police informations")
    def marthahalli(self):
        print("you are cought by police in marthahalli")
    def koramanagala(self):
            print("you are cought by police in koramanagala")
class fine(bangalore):
    def __init__(self):
        print("fine details")
    def marthahalli(self):
        print("fine rupees 100")
    def koramanagala(self):
        print("fine rupees 200")

c = bangalore()
c.marthahalli()
c.koramanagala()

