class Employe:
    comapany = "Google"
    def getsalary(self): # self ek aisa parameter hai joh a=automatically pass hota hai .
        print(f"salary is {self.salary} for a {self.comapany}")

gaurav =  Employe() 
gaurav.salary =  100000
gaurav.getsalary() # without self TypeError: Employe.salary() takes 0 positional arguments but 1 was given __because "gaurav  is a parameter "__

# Employe.salary(gaurav)