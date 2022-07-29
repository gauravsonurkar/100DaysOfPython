f = open("sample.txt",'r')
text = f.readline() # it will read a 1st line of the file
print(text)
text = f.readline() # it will read 2nd line of the file
print(text)
text = f.readline() # it will read 3rd line of the file
print(text)
f.close()