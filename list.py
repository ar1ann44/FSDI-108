# list are written with squere brackets []

my_list = [10, 20, 30, 40, 50]
print(my_list)


# list can contain different data types
mixed_list = [1, "apple", 3.5, True]
print(mixed_list)

#access by their INDEX number
#(indexing starts at 0)

fruits = ["apple", "banana", "cherry"]
print(fruits[0])
print(fruits[2])

# you can also use negative indexes to count from the end 
print(fruits[-1]) 

# modify list items 
fruits[1] = "mango" # changes banana -> mango
print(fruits)

# adding items
fruits.append("orange") # adds to the END
print(fruits)

fruits.insert(1, "kiwi") 
print(fruits)

# removing items
fruits.remove("cherry") 
print(fruits)

fruits.pop() 
print(fruits)

# looping through a list
for fruit in fruits:
    print(fruit)

# check if ITEM exists
if "mango" in fruits:
    print("yes, mango is in the list")

# list length
print(len(fruits)) # number of items in the list

'''
MINI CHALLENGE: Favortie movies
create a list of 4 of your favorties movies 
replace the second movie (index 1) with a new one

remove on movie 
    option A: remove by value
    option B: remove by index
print the list
print the length
'''

favorite_movies = ["the departed", "jingle all the way", "interstellar", "toy story"]

favorite_movies[1] = "the bee movie"

favorite_movies.remove("the bee movie")

print(favorite_movies)
print(len(favorite_movies))

