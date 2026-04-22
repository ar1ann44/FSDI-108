print("hello world from python!")
print(2)
print(2 + 3)
print(True)

#this is a comment

'''
everything inside here is a comment
useful for guide/ code breakdown
'''

#create a variable
name = "ariana"
age = 20
print(name)

print ("my name is  " + name + ", and I am " + str(age) + " years old")

name = "Jenifer"
age = 21
middle_name = "Ariana"
last_name = "Osuna"
found = False 

print("my name is " + name + " " + middle_name + " " + last_name + ", and I am " + str(age) + " years old")

# f-strings
print(f"my name is {name} {middle_name} {last_name}, and I am {age} years old")

'''
MINI CHALLENGE
write a breife strory using 5 variables and print the strory in the terminal 
you should use strings and numeric variables
concatenate your variables to create the story
use f strings to combine all your variables into one print line
'''

character_name = "Ariana"
place = "the park"
activity = "playing soccer"
weather = "sunny"
character_name2 = "Jesse"
character_name3 = "Robert"
activity2 = "eating ice cream"

print(f"{character_name} and {character_name2} were {activity} at {place} on a {weather} day and {character_name3} was {activity2} nearby.")



print(character_name + " and " + character_name2 + " were " + activity + " at " + place + " on a " + weather + " day and " + character_name3 + " was " + activity2 + " nearby")


#type functions
print(type(name))
print(type(age))
print(type(True))


#casting (changing data types)
print(20 + int("20"))
print(20 + age)
print(20 + 2.98)

# input function
#user_name = input("enter your name:")

#print(f"Hello, {user_name}")

#input() always returns string

#print(type(input("enter your age:")))

#new_age = int(input("enter your age: "))
#print(age + new_age)

"""
MINI CHALLENGE
pizza calculator
-ask how many slices of pizza and how many people
-use math operators to calculate slice per person
-show the results with and f-string
"""

slices = int(input("how many slices of pizza? "))
people = int(input("how many people? "))

slices_per_person = slices / people

print(f"each person gets {slices_per_person} slices of pizza")


