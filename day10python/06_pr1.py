
f = open("poem.txt", 'r')

text = f.read()
if "twinkle" in text:
    print("twinkle is present in the file ")
else:
    print("twinkle is not present in the file ")

f.close()
