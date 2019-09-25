

class MinOfTransport():

    def roadways(self,state):
        print(state," Road ways")

    def waterways(self, state):
        print(state, " Water ways")

class TamilNadu():

    # def tnRoadWays(self):
    #     self.roadways("TN")

    def metro(self):
        print("TN Metro")

class AP(MinOfTransport,TamilNadu):

    def apRoadWays(self):
        self.roadways("AP")


    def apMetro(self):
        self.metro()



ap = AP()
ap.apRoadWays()
ap.apMetro()
