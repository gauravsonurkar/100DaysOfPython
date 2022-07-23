def greet(name):
    print("Good day " + name)  # func defination


names = input("Enter your name : ")
greet(names)    # function call


# two types of function
# 1} user define function Eg: greet
# 2} build in function eg: len() , range .

# function of adding two number :

def mySum(num1, num2):
    return num1 + num2


s = mySum(32, 8)
print(s)
