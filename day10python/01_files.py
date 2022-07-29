# reading the file using open function 

f = open("sample.txt" , 'r')
# text = f.read(5) # it can read a first 5 character of the file
text = f.read() 
print(text)
f.close()