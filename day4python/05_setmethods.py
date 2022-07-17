# creating the empty set


b = set()
print(type(b))

# Adding the values to an empty set
b.add(1)
b.add(6)
b.add(2)
b.add(1)
b.add(3)
b.add(6)  # adding the values in the set repeatedly does not changes  a set
b.add((1, 2, 3))  # adding the tuple into the set
# b.add([1,2,3]) ## adding the list  into the set

# in this 15 16 line we can easily add thw tuple  into the set  ,  but not the list because it is unhassable type
print(b)

# print the length of the set b .
print(len(b))

# removal of an item

b.remove(6)  # remove the 6 from the list
print(b)

print(b.pop())
print(b)
