from turtle import update


myDict = {
    "fast ":  "in fast manner ",
    "Gaurav": "Satkar ",
    "Marks":   [1, 2, 3],
    "anotherdict": {'harry':  'player'}

}

# Dictionary Methods
# print(myDict.keys())  # the output will come under the tuple
# print the keys of the dictionary
# print(list(myDict.keys())) # now output will come under the list

# print(" Value of the dictionary \n  ", myDict.values())

# print("Items of the dictionary .\n: ", myDict.items())


# print(myDict)

update_Dict = {
    "lovish": "Friends",
    "Divya": "Friends",
    "Gaurva":  "friends",
    "harry": "A dancer"
}

# updates the dictionary bt adding key value pairs from updateDict
myDict.update(update_Dict)
# print(myDict)
# print(myDict["harr1y"]) it will throw an error
print(myDict.get("harry"))  # print the value associated with key "Harry "
