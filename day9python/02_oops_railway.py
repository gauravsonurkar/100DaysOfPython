class RailwayForm:
    formType = "RailwayForm"
    def printData(self):
        print(f"Name is : {self.name}")
        print(f"Train is : {self.train}")



Gauaravapplication = RailwayForm()
Gauaravapplication.name = input("Enter your name : ")
Gauaravapplication.train = input("Enter the train name :")
Gauaravapplication.printData()