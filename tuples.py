#count()=>Returns the number of times a specified value occurs in a tuple
#index()=>Searches the tuple for a specified value and returns the position of where it was found

tuple1 = (5, 5.5, "Grishma", "Neupane", [5, 6, 7.5], 5, 1, 1, 5)
print(tuple1)

print(tuple1.count(5))
print(tuple1.index(5))
print(tuple1.index([5, 6, 7.5]))

#Nested Tuple
#tuple2 = (5, 5.5, "Grishma", "Neupane", [5, 6, 7.5], (1, 2, 3, 4))