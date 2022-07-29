words = ["donkey","chutiya" , "bsdk"]
with open("sensoredfile.txt",'r') as f:
    content = f.read()

for word in words:
    content = content.replace(word,"####")
    with open('sensoredfile.txt','w') as f:
        f.write(content)
 

