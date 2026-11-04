#Types of functions
#The functions that are predefined in python are called built-in-functions
#print(), input(), len(), int(), str()
#user defined functions => The functions that are defined by the user/programmer
#example: operation(), sum()


#Returnable function => The function that returns a certain value
#return keyword is used in returnable function

def sub(a,b):
    print(a-b)
def sum(a,b):
    return f"Sum is {a+b}"    
    return a+b

sub(10,5)
result = sum(5,10)
print(result)
#for return, it needed a variable to return the value

#Non returnable function => The function that don't return any value
#return keyword isnot used in non returnable function
#return keyword returns the value to that line from where that function is being called


#lambda function => function in one line
#syntax:
#   lambda parameters : operation
#lambda function is also called nameless function, name isnot needed to define function
#but to call a function, we need its name
#lambda function returns the operation by default

#sum = lambda a,b : a+b
#print(sum(a+b))

sum = lambda a,b : print(a+b)
sum(10,20) # function is called here

#lambda function is only used to small functions

#Map Function: Map works only on group datatype
#Syntax: map(function, group_data_type)
#Map applies the function to every elements of group data type

list1 = [5,7,8,9,2]
result = map(lambda x:x**2, list1)
print(list(result))

#map print object
#typecast is done to get result 
#print(list/tuple(result))- type casting

list2 = ["UJJWAL", "RAM", "SHYAM"]
result = map(lambda x:x.lower(), list2)
print(list(result)) #we can change the it into list or tuple
print(tuple(result))


#Filter Function => Filters out the elements from group data type according to the functions
#syntax:
#filter(function, group_data_type)

num = [1,2,3,4,5,6,7,8,9]
result = filter(lambda x:x>5, num)
print(list(result))


#reduce function => from functools import reduce
#reduce function reduces the element of group data type into a single value
#syntax: reduce(function, group_data_type)
# numbers = [1,2,3,4,5]
# result = reduce(lambda x,y:x+y,numbers)
# print(result) # no type cast needed



#zip function: It combines the elements of multiple group data type in a tuple
names = ["Ujjwal", "Shyam", "Ram", "Hari"]
marks = [98.5, 96, 99, 20]
grade = [10,9,8,7]
result = zip(names,marks,grade)
print(list(result))
#bhitra answer tuple ma aauxa zip ma
print(tuple(result))

#ARGS => Positional Arguments. It is denoted by *
#KWARGS => Keywords Arguments. It is denoted by **

def abc(*args,**kwargs):
    print(args)
    print(kwargs)
abc(1,2,3,4,5,"Ujjwal","Neupane", True, 98.5, name = "Grishma", age = 29, position = "Data Science")

