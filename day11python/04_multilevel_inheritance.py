class Person:
    contry = "India"

    def take_breath(self):
        print("Im breathing .. ")


class Employee(Person):
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
        print("Im a programmer im also breathing ")        


p = Person()
e = Employee()
pr = Programmer()
pr.take_breath()
e.take_breath()
print(e.Company)
print(e.contry)