class Employee:
    comapany = "Google"
    salary = 100
    location = "delhi"

    # def changeSalray(self,sal):
    #     self.__class__.salary = sal #thunder method yeh change kr denga class value ko
    @classmethod
    def changeSalray(cls,sal): # we can also use classmetod for the changing the attribute
        cls.salary = sal         


e = Employee()
print(e.salary)
e.changeSalray(488)
print(e.salary)
print(Employee.salary)
