'''
if condition:
    -code block that runs if the condition is true 
    
elif (else if):
    -code block runs if the first condition is false 
    -and this condition only works if its True
else:
    -code block runs if none of the above conditions are true
'''

x = 5

if x > 0:
    print("x is positive")
elif x == 0:
    print("x is zero")
elif x >= 5:
    print("x is equal to 5")
else:
    print("x is not a positive number") 
    
#short hand IF statements
if x > 5: print("x is greater than 5")

#short hand IF-ELSE statements
x = 21
print("Even") if x % 2 == 0 else print("odd")

# nested if statements
x = 15
if x > 0:
    if x < 20:
        print("x is a positive number less than 20")

# combining conditions 
age = 18

if age >= 18 and age <= 21:
    print("you are between 18 and 21")

'''
MINI CHALLENGE:
1. ask the user to enter todays temperature in farenheit and store
it in a variable called temperature 

2. use if-elif statements to classify the temperature:
if temp >= 86, print "it is hot outside!"
if temp >= 68 and temp < 86, print "the weather is nice!"
if temp >= 50 and temp < 68, print "it is a bit chilly"
otherwise, print "it is cold!"

3. create a variable called jacket:
set it to True if temp < 59, otherwise set it to False

4. bonus: if jacket is true, print "better wear a jacket!" otherwise print "no jacket needed"
'''
temperature = int(input("enter todays temperature in fahrenheit: "))

if temperature > 86:
    print("it is hot outside!")
elif temperature > 68 and temperature < 86:
    print("the weather is nice!")
elif temperature > 50 and temperature < 68:
    print("it is a bit chilly")
else:
    print("it is cold!")

jacket = True if temperature < 59 else False

if jacket:
    print("better wear a jacket!")
else:
    print("no jacket needed")

