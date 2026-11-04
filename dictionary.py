# Python dictionary methods
#Stores information as key:value pairs

student = {
    "name": "Grishma",
    "age": 23,
    "course": "BSc CSIT"
}

print(student)

#1. get() => Returns the value of the specified key/Gets the value of a key.
#2. keys() => Returns all keys/Returns a list containing the dictionary's keys
#3. values() => Returns all values/	Returns a list of all the values in the dictionary
#4. items() => Returns both keys and values
student = {
    "name": "Grishma",
    "age": 23,
    "course": "BSc CSIT"
}

print(student)
print(student.get("name"))
print(student.keys())
print(student.values())
print(student.items())

#5. update() =>Adds or changes information.
#6. pop() =>Removes a specific key and its value.
#7. popitem() =>Removes the last key-value pair.
#8. clear() =>Removes everything.
#9. copy() =>Copies a dictionary.
#10. setdefault() =>Gets a value if the key exists. If the key doesn't exist, it creates it.
#11. fromkeys() => Returns a dictionary with the specifies key and value

dict1 = {
    "name" : "Grishma",
    "age" : 23,
    "Education" : "Graduate",
    "Year" : 2026,
    "dict2" : {
        "Faculty" : "Csit",
        "Methods" : "dict",
        "university": "Tribhuvan University",
        "percentage": 81.74

    }
}
print(dict1)
dict1.update({"city" : "Kathmandu"}) #add 
print(dict1)
dict1.update({"Education" : "Pass Out", "percentage" : 82}) #changes
print(dict1)
dict1.pop("age") #nested dictionary ko key remove garna milena
print(dict1)
dict1.popitem() #removes last key value pair
print(dict1)
#dict1.clear() #removes everything
#print(dict1)

new_dict = dict1.copy()
print(new_dict)

dict1.setdefault("year", 30)
print(dict1)

