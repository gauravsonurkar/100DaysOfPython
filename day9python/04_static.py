
class Employe:
    comapany = "Google"
    def getsalary(self,signature): 
        print(f"salary is {self.salary} for a {self.comapany}\n{signature}")
    @staticmethod # aise hi bna na hai tb .   --> decorator      
    def greet():
        print("good moring sir") 
    @staticmethod          
    def time():
        print("time is 9am in the moring . ")        

gaurav =  Employe() 
gaurav.salary =  100000
gaurav.getsalary("thanks") 
gaurav.greet()

gaurav.time()
# Employe.salary(gaurav)