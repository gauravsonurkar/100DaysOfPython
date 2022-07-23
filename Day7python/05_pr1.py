# Write a function to find a greatest of three number 

def Max_numbers (num1 , num2 , num3):
    if(num1>num2):
        if(num1>num3):
            return num1
        else:
            return num3
    else:
        if(num2>num3):
            return num2
        else:
            num3                        

a = int(input("Enter the 1st number : "))
b = int(input("Enter the 2nd number : "))
c = int(input("Enter the 3rd number : "))

m = Max_numbers(a,b,c)
print("The value of the maximum is " + str(m))