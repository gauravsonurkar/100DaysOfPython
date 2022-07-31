class Calculator:
    def __init__(self,number):
        self.num = number
    def square(self):
        print(f"The square of the {self.num} is {self.num **2}") # ** is an exponent operator which is used to take a square.
    def squareRoot(self):
        print(f"The squareRoot of the {self.num} is {self.num **3}")
    def cube(self):
        print(f"The Cube of the {self.num} is {self.num **0.5}")

a = int(input("Enter the value for square , squareroot , Cube : "))
cal = Calculator(a)

cal.square()
cal.squareRoot()
cal.cube()
        
        