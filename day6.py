#Loops
#Loops are the keywords used to repeat same block of code multiple times
#Types of loops:
#for loop => used when we know the start and stop conditions
#syntax: 
#     for iterator in iterable
        #block of code to be executed
#iterator => A variable that stores the current data while loop is running
#iterable => A group data type where the loops get executed
#iteration => One complete cycle of loop

list1 = [1,2,3,4,5,6,"Grishma","Neupane"]
for i in list1:
    print(i)

#range()=> range() generates the sequence of number
# range(start, end, step)
# End value is exclusive, start value is inclusive
# 1 value in range(),that value will end, start will be 0    
#for i in range(5):
    #print(i)  #print upto 4 cause last value is exclusive

# 2 value in range(), first will be for start, second will be for end
for i in range(5,10):
    print(i)   

# 3 value in range(), first will be for start,second will be for end
# third will be for step
for i in range(7,20,3):
    print(i)

#list indexing and slicing
#break and continue
#break => when break encountered, it exits from the current loop

for i in range(1,6):
    if i == 4:
        print("Break Encountered")
        break
    print(i) 

#continue =>When continue encounters,it break current iteration but doesnot
# exit the loop    
for i in range(1,6):
    if i == 3:
        print("Continue encounter")
        continue
    print(i)
print("Continue encountered but loop kept running")    


#list indexing and slicing
#Indexing=> Accessing single element of list
#Slicing=> Accessing multiple element of list

list1 = ["Grishma",1,2,3,4,5,6,7,"Neupane"]
#list1[index_number]=> indexing
print(list1[0]) #0 => Positive indexing
print(list1[-1]) #-1 => Negative indexing
print(list1[-5])

#list1[start_index : end_index : step] => slicing
list1 = ["Grishma","ABC","DEF",50,"GHI",10,"NEUPANE"]
#we should give start=>Positive indexing
#End index is always exclusive,start index is always inclusive
print(list1[1:5])
print(list1[1:5:2])
print(list1[1:5:3])

#Negative Slicing => Negative index
print(list1[-1:1:-1])
print(list1[-1:1:-2])

print(list1[::])
#If no value is given in start, it starts from 0 index
#If no value is given in end, it includes upto last element
#If no value is given in step, it default value to 1


#list comprehension
#writing the keywords inside list

list2=[i for i in range(15)]
list2=[i+2 for i in range(15)]
list2=[i*2 for i in range(15)]
list2=[i for i in range(15) if i%2==0]
#If you are using simple if, use if keyword after loop
#If you are if else, we need to use if else before loop
list2=["Even" if i%2==0 else "Odd" for i in range(15)]
list2=[f"Even - {i}" if i%2==0 else f"Odd - {i}" for i in range(15)]
# f => Formatted string
#formatted string allows us to write string and variable inside the same quotation marks
#to write variable inside f string => we should wrap the variable by {}
print(list2)


#Dictionary Comprehension

