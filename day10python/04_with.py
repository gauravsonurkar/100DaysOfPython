# using with statement we no need to close() the file its will automatically do this 

# read file using with 
# with open("sample.txt",'r') as f:
#     text = f.read()
#     print(text)
#     

# write file using with function 

with open("withwrite.txt",'w') as f:
    text = f.write("this file is created using a with function ")