#Python Set Methods
#1. add()=>Adds one item to a set
#2. update()-Adds multiple items to a set.
#3. remove()-Removes a specific item
#4. discard()-Also removes an item.
#5. pop()-Removes one item from the set
#6. clear()-Removes all items from the set.
#7. copy()-Creates a copy of a set.
#8. union()-union() combines two or more sets.
#9. intersection()-Finds the items that are present in both sets.
#10. difference()-Finds items that are in the first set but not the second set
#11. symmetric_difference()-This gives you the items that are in one set or the other, but not both.
#12. intersection_update()-This changes the original set and keeps only the common items.
#13. difference_update()-Removes from the first set all items that are also present in the second set.
#14. symmetric_difference_update()-Updates the first set so that it contains items that are in either set but not both
#15. issubset()-Checks whether all items of one set are inside another set
#16. issuperset()-This is basically the opposite of issubset().It checks whether a set contains all items of another set
#17. isdisjoint()-Checks whether two sets have nothing in common.



#set = {1, 2, 3}
#set.add(5)
#print(set)
#set.add("abc")
#print(set)
#set.update(6, 7, 8)
#print(set)

#a = {"a", "bhg", "dfe", "asd"}
#b = {"x", "y", "z"}
#a.update(b)
#print(a)  #add the items to a
#b.update(a)
#print(b)  #add the items to b

#a.remove("bhg") 
#print(a)
#b.discard("x") 
#print(b)

#remove()   → remove it, and complain if it doesn't exist
#discard()  → remove it, but don't complain

#numbers = {1, 2, 3, 4}
#numbers.pop()
#print(numbers)

#Because sets are unordered, you should not rely on which particular item gets removed.
#numbers.clear()
#print(numbers)

#numbers = {1, 2, 3, 4}
#new_numbers = numbers.copy()
#print(new_numbers)


#a = {"grishma", "hp", "csit", "acer", 2.5}
#b = {"neupane", 2, "csit", 2.5, "course" }
#result = a.union(b) #a|b can be used like this
#print(result)
#result = a.intersection(b) #a&b can be used
#print(result)
#result = a.difference(b) # a-b can be used
#print(result)
#result = b.difference(a) #b-a
#print(result)

#result = a.symmetric_difference(b) # a^b
#print(result)
#result = a.intersection_update(b)
#print(result)

a = {3, 4, 5, 6}
b = {4, 6, 8, 10}
result = a.symmetric_difference(b)
print(result)

a.intersection_update(b)
print(a)

a.difference_update(b)
print(a)

a.symmetric_difference_update(b)
print(a)

print(a.issubset(b)) #  a<=b
print(b.issubset(a))

print(a.issuperset(b)) #issuperset
print(a.isdisjoint(b)) #isdisjoint