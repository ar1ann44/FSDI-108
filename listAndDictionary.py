'''
You must create a new list (not the one from the example), just like we practiced in class.
lists.py

•  Creating a list

•  Accessing items by index

•  Replacing values

•  Removing items (by value or by index)

•  Printing the list and its length

Add a print after every step

You must create a new dictionary with your own values, following the same structure we used in class.
dictionaries.py

•  Creating a dictionary with key:value pairs

•  Accessing values using keys

•  Adding new keys

•  Updating existing values

•  Removing keys

•  Printing the dictionary and its length after every step

Add a print after every step
'''

# creating a list
colors = ["pink", "blue", "yellow", "red", "green"]
print(colors)

# accessing items by index
print(colors[0])

# replacing values
colors[1] = "purple"
print(colors)

# removing items by value
colors.remove("yellow")
print(colors)

# removing items by index
colors.pop(2)
print(colors)

# printing the list and its length
print(colors)
print(len(colors))


########################################

# creating a dictionary
dog = {
    "name": "Dexter",
    "age": 5,
    "breed": "malinois"
}
print(dog)

# accessing values using keys
print(dog["name"])

# adding new keys
dog["color"] = "black"
print(dog)

# updating existing values
dog["age"] = 6
print(dog)

# removing keys
dog.pop("breed")
print(dog)

# printing the dictionary and its length
print(dog)
print(len(dog))





