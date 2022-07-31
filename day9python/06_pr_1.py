class Programmer:
    company = "Microsoft"
    def __init__(self,name , product):
        self.name = name 
        self.product = product       
    def printData(self):
        print(f"The name of the programmer is {self.name} and works on the product {self.product}")

a = input ("Enter the user Name :")
b = input ("Enter the working of you wich is assigned by the company  :")
# Gaurav = Programmer("Gaurav " , "YouTube") # Using Local Method 
# Vaibhav = Programmer("Gaurav " , "YouTube")
Gaurav = Programmer(a , b) # Using Input Function ()
Vaibhav = Programmer(a , b)


Gaurav.printData()
Vaibhav.printData()



