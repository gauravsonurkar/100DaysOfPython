
mydict = {
    "Gaurav" : "Satkar",
    "vastu" : "goods",
    "chendu" : "ball",
}


print(mydict.keys())
a =  input("Enter the value that you want from above  : ")
# this will throw the value of the dict

# print("The meaning of your word is : " , mydict[a]) 

# Below line will not throw an error if the key is not present in the dictionary

print("The meanin of your word is : ",mydict.get(a))

