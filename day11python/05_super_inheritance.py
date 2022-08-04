class Person:
    contry = "India"

    def __init__(self):
        print("initializing person \n. ")

    def take_breath(self):
        print("Im breathing .. ")


class Employee(Person):
    def __init__(self):
        super().__init__()
        print("initializing Employee .\n ")
    Company = "HERO HONDA"

    def getSalary(self):
        print(f"The salary is {self.salary}")

    def take_breath(self):
        print("Im a employe im also breathing ")


class Programmer(Employee):
    Company = "Fiverr"

    def getSalary(self):
        print(f"No salary to programmer ")

    def take_breath(self):
        super().take_breath() # Employee
        print("Im a programmer im also breathing ")        


# p = Person()
# p.take_breath()

e = Employee()
# e.take_breath()

# pr = Programmer()
# pr.take_breath()


