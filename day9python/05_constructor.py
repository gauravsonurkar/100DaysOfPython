# attribute , varible , instance same hi hai

class Employe:
    comapany = "Google"

    # init is automatically run hojata hai its called as constructor because it initialize a object
    def __init__(self, name, salary, subunit):
        self.name = name
        self.salary = salary
        self.subunit = subunit
        print("Employe is created ")

    def getdetails(self):
        print(f"The name of the user is {self.name}")
        print(f"The salary of the user is {self.salary}")
        print(f"The subunit of the user is {self.subunit}")

    def getsalary(self, signature):
        print(f"salary is {self.salary} for a {self.comapany}\n{signature}")

    @staticmethod  # aise hi bna na hai tb .   --> decorator
    def greet():
        print("good moring sir")

    @staticmethod
    def time():
        print("time is 9am in the moring . ")


gaurav = Employe("harry", 100, "YouTube")
# gaurav = Employe() # this throws an error TypeError: Employe.__init__() missing 3 required positional arguments: 'name', 'salary', and 'subunit'
gaurav.getdetails()
