

class Employe:
    company = 'Google'

    def getDetails(self):
        print("This is an employe")


# this is inheritance which is dirived class accuared the properties of base class.
class Programmer(Employe):
    language = "python"
    def getlanguage(self):
        print(f"This is {self.language}")
    def getDetails(self):
        print("This is an employe from the programmer class") # you can overwrite the function by the help of inheritance overwrite means 
        # agr base class mai ek func1 hai to waisa hi same name ka function hum derived class mai bna skte hai bina kisi error ke  isi ko bolte hai inheritance


e = Employe()
p = Programmer() 
e.getDetails()
p.getlanguage()
p.getDetails() # This can able to access the method of Employee ***This is the main reason of Ingeritance***
