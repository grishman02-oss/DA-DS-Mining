#Types of datatypes
#1. Mutable Datatypes => Are the datatypes that can be changed/modified after creation
# list, set, dictionary


#2. Non Mutable / Immutable Datatypes => They cann't be modified once created
# => If we need to modify the immutable datatype, python creates a new object.
# int, float, str, tuple, boolean


#List => Mutable =>  can be originally changed after creation
# List is an ordered group data type
# List is wrapped with []
#Eg: List1 = [5, 20.5, True, False, "Grishma", "Neupane"]

List1 = [5, 20.5, True, False, "Grishma", "Neupane"]
print(List1)

#Group data type is the collection of multiple data types
#Index => Every ordered data type gives an unique index_value to its elements
#Index always starts from 0

#Nested  => One inside another
# Nested_list => One list inside another list

list2 = [5, 20.5, True, False, "Grishma", "Neupane", [1, 2, 3, 4]]
print(list2)

#Tuple => non mutable dattype, ordered group data type
# Tuple is wrapped with ()
# Eg: tuple1 = (5, 5.5, "Grishma", "Neupane", [5, 6, 7.5])

tuple1 = (5, 5.5, "Grishma", "Neupane", [5, 6, 7.5])
print(tuple)

#Nested Tuple
#tuple2 = (5, 5.5, "Grishma", "Neupane", [5, 6, 7.5], (1, 2, 3, 4))

#Set => mutable unordered group data type
# we cannot store list, dictionary and set inside set
# Set is wrapped with {}
# Set cannot contain duplicates values

set1 = {1, 2, 3, 5.5, 4.5, True, False, False, True, "Grishma", "Class", "Data Science"}
print(set1)

#Dictionary => Mutable unordered  data type
#elements come in key:value pair
#Dictionary is wrapped with {}
#Example
dict1 = {
    "Name" : "Grishma",
    "Age" : 23,
    "Country" : "Nepal",
}

#Task : Try out every methods of these data types
#String is also a ordered group data type => Group of character

#Membership Operator => in, not in
#Check if the value is present in the group data type or not
usernames = ["Ram", "Grishma", "Sita", "Hari"]
username = input("Enter your username: ")
print(username in usernames) #True or False
print(username not in usernames)
