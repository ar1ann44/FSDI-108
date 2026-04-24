#dictionaries store data in KEY: VALUE pairs
#written with curly brackets {}

student = {
    "name": "ari",
    "age": 20,
    "major": ["software engineering"]
}
print(student)

# accessing items 
print(student["name"])
print(student.get("major"))

# adding new items
student["graduation_year"] = 2025
print(student)

# changing values
student["age"] = 21
print(student)

#removing items 
student.pop("major") # removes key "major" and its value
print(student)

# check if key exists
if "name" in student:
    print("key name exists")

#nested dictionaries
studentss = {
    "student1": {"name": "ari", "age": 20,},
    "student2": {"name": "bob", "age": 22}
}
print(studentss)
print(studentss["student2"]["age"]) 

'''
MINI CHALLENGE: student report card
you need to store and analyze a student grades.
1. create a dictionary called "report_card" with keys:
- "name"
- "subjects" 
- "grades" (use a tuple with 3 numbers)
EXAMPLE: {"name": "leo", "subject": ["math"], "grades": (85, 90, 92)}
2 print the students name and subject
3. calculate the avarage of the 3 grades (HINT: use the sum() and len() )
4. add a new key called "average" with the calculated results 
5. if the avarage is 90 or above, print "excellent!"
if beteween 70 and 89, print "good job!"
otherwise, print "needs improvement"
6. remove the "subject" key and print the updated dictionary
'''

print("\n=================================================\n")

report_card = {
    "name": "ari",
    "subjects": ["math"],
    "grades": (85, 90, 100)
}

print(report_card["name"])
print(report_card["subjects"])

average = sum(report_card["grades"]) / len(report_card["grades"])
report_card["average"] = average
print(report_card)

if average > 90:
    print("excellent!")
elif average > 70:
    print("good job!")
else:
    print("needs improvement")

report_card.pop("subjects")

print(report_card)
