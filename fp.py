# The point of this assignment is not to use the functional elements that are part of your chosen language (JavScript/Python).
# But, rather, implement the functionality from scratch using pure functions and higher level functions.
# Do the implimentation in order as given. 
# We have linked to info at MDN, this is just to give a sence of how the reduce,forEach,map and filter functions should work.
#
# 🛠️ Prerequisite:
# You must create an array persons that will contain the data from https:#raw.githubusercontent.com/MM-203/misc/main/data/data.json
# This must be done before the first task
#
# ----------------------------------------------------------------------------------------------------------------------------------
# Bonus challenge 🎉 (a bit hard), the functions forEach, filter and map can all be created using the function reduce. 
# If you feel up for a challenge, try doing so. NB! The bonus challenge is optional. 
# ----------------------------------------------------------------------------------------------------------------------------------

import requests
import json
from functools import reduce

url = "https://raw.githubusercontent.com/MM-203/misc/main/data/data.json"

response = requests.get(url)
data = response.json()

if isinstance(data, list):
    persons = data
else:

    persons = data['persons']

print(persons)



# 1
# Implement your own reduce function and count the number of people above the age of 50
# You can read about a reduce function https:#developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/reduce 

def people_above_50(acc, person):
    if person["age"] > 50:
        return acc + 1
    else:
        return acc
    
count = reduce(people_above_50, persons, 0)

print("Count:", count)


# 2
# Implement your own forEach function and use it to greet all the people in the persons array (say Hi, persons name).
# Read about forEach https:#developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/forEach

def greet_persons(person):
    print("Hi,", person["name"])

def forEach(array, action):
    for item in array:
        action(item)

forEach(persons, greet_persons)


# 3
# Implement your own map function and make everyone a year older.
# You can read about what the map function should do https:#developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/map 

def one_year_older(person):
    person["age"] += 1
    return person

def map_array(array, transform):
    return [transform(item) for item in array]

updated_persons = map_array(persons, one_year_older)
print(updated_persons)

# 4
# Implement your own filter function, and use it to find evryone under the drinking age.
# Read about filter https:#developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/filter

def under_drinking_age(person):
    return person["age"] < 18

def filter_persons_array(array, condition):
    return [item for item in array if condition(item)]

is_under_drinking_age = filter_persons_array(persons, under_drinking_age) 

for person in is_under_drinking_age:
    print(person["name"])

# 5
# Now create a function sum, that takes a list of numbers and returns the sum
# Try to use your previously created functions to make this function 
# Sum the total age of persons using this new function 
# NB! Do not manualy create the age listing

def sum_total_age(acc, person):
    return acc + person["age"]

total_age = reduce(sum_total_age, persons, 0)
print("Total age:", total_age)

# 6
# Now create a function average, that returns the average of a list of numbers
# Try to use your previously created functions to make this function 
# calculate the average age of the persons using this function
# NB! Do not manualy create the age listing

def calculate_average(array):
    total_age
    count = len(array)
    if count > 0:
        return total_age / count
    else:
        return 0
    
average_age = calculate_average(persons)
print("Average Age:", average_age)


# 7
# Finaly create a max and a min function that respectivly returns the maximum value and the minimum value
# Only use previously created functions to acchive this.
# Then find the min and max age of ther persons.

def find_max_age(acc, person):
    return max(acc, person["age"])

def find_min_age(acc, person):
    return min(acc, person["age"])

max_age = reduce(find_max_age, persons, float('-inf'))
min_age = reduce(find_min_age, persons, float('inf'))

print("Max Age:", max_age)
print("Min Age:", min_age)


