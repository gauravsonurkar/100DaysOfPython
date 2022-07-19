sub1 = int(input("Enter the marks of sub1 : "))
sub2 = int(input("Enter the marks of sub1 : "))
sub3 = int(input("Enter the marks of sub1 : "))

if(sub1 < 33 or sub2 < 33 or sub3 < 33):
    print("You are fail ")

elif(sub1 + sub2 + sub3)/3 < 40:
    print("You are fail ")

else:
    print("Congratulation's! you passed the exam  ")
