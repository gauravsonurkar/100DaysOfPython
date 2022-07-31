class Train:
    def __init__(self, name, status, fare):
        self.name = name
        self.status = status
        self.fare = fare

    def traininfo(self):
        print(f"Name of the train is {self.name} ")

    def getStatus(self):
        print(f"The seat available is {self.status}")
        if (self.status > 0):
            print(f"your seat is booked your seat number is {self.status} ")
            self.status = self.status - 1

    def getFareInfo(self):
        print(f"The fare of the train is {self.fare}")


details = Train("Rajdhani Express", 90, 2)
details.traininfo()
details.getStatus()
details.getFareInfo()
