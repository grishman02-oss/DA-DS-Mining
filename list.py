#Task : Try out every methods of these data types(List, Tuple, Set, Dictionary)
#List - using all the built in methods of list

#append() => add an element at the end of the list
#list1= [1, 2, 5, 10, 15, 100]
#list1.append(1000)
#print(list1)

#list2 = ["Abcd", "Data", "Python", "Kathmandu"]
#list2.append("Nepal")
#print(list2)

#insert()=> add an element at a specific position or the index 
#list = ['HP', 'Dell', 'Lenovo']
#list.insert(0, 'Acer')
#print(list)
#list.insert(2, 'Laptop')
#print(list)

#remove()=> remove a specific value
list = [1, 2.5, True, "Grishma", [2, 2.5, False, "Neupane"]]
list.remove("Grishma")
print(list)
list.remove([2, 2.5, False, "Neupane"])   #thats how we remove
print(list)

#pop() => Remove an item using its index
#list = [9, 8.0, True, False, "HP",(1,"ABC")]
#list.pop(5)
#print(list)

#clear() => Removes Everything from the list
list = ["ABC", "HGH", "678", 3.5]
list.clear()
print(list)

#Index() => Find the position of an item
list = [1, 3.5, "grishma", True, ("a", "b"), ["abc", "hjk"], {2, 6, 7}]
print(list.index(("a", "b")))
print(list.index(["abc", "hjk"]))

#Count() => How many times an item appears
list = [3, 4.5, 6.0, 3, {"a", "b"}, [3, 4, 5]]
print(list.count(3))

#sort() => Sort the list
list = [3, 4, 6, 3, 9, 1]
list.sort()
print(list)

#reverse() => reverse the order of the list
list = [4, 5, 9, 1, 0]
list.reverse()
print(list)

#copy() 
list = [1, 4, 6, {"a", "b", "c"}]
new_list = list.copy()
print(new_list)
