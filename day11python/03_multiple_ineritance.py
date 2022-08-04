#multiple inheritance occurs when base class aquared the properties from more than 
#more than one  parents class

class Employee:
    
    company = "visa"
    ecode = 232
class Freelancer:
    company = "Fiverr" 
    level = 0
    def upgrade_level(self):
        self.level = self.level + 1

class Programmer (Employee,Freelancer): # joh pehle likha honga use priority milengi 
    name = "Virat"   

p = Programmer()
p.upgrade_level()
print(p.company)

