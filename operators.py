#arithmetic operators - math operations
# if you hace enough typed out use TAB to auto fill
x = 1
y = 2.99
res = 0

res = x + y # +, -, *, /, %, **, //
print(res)


#assignment operators - used to assign values to variables
# +=, all operators have to be before the = 
x = 5
x += 5
x -= 3
x *= 3
x /= 3
print(x)

#comparison operators
#use to compare two values- same as the if else statements

# == equal to
# != not equal to
# >< greater/less than
# >= less than or equal to
# <= greater than or equal to

#logical operators- used to combine conditional statements
# used with true and false values like conditions
#and -> both must be true
#or -> one must be true
#not -> flips True to False and False to True

x = 10
y = 10
z = 3

print(x == y and y == z) #false because both conditions are not true

print(x == y or y == z) #true because one condition is true

print(not x == y)

#identity operators- used to compare objects, not if they are equal

#but if they are actually the same object with the same memory location

# is -> checks if two things are the exact same object in memory
# is not -> checks if two things are not the same object in memory

x = 3
y = 3

print(x is y) # returns true since they are the same 
print(x is not y) # returns false since they are the same

#membership operators- used to test if a sequence is present in an object   
# in -> cheks if something exists in a sequence (list, string, etc...)
# not in -> checks if something is NOT inside 

x = [1, 2, 3, 4, 5] # this is a list

print(4 in x) #true bc 4 is in the list
print(9 not in x) #true bc 9 is not in the list




