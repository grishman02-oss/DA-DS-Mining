#OOP => Object Oriented Programming 
#Organize code using classes and object  
#OOP is a new way of writing the code or to make our code structured using classes and object
#Class => blueprint to create a object
#Attributes or methods(properties) that a object should have

#Object => Instance(example) of a class

#To define a class, we use Class keyword
#syntax:
# class ClassName:
    #attributes - variables defined inside the class
    #methods - functions defined inside the class

class Student:
    name = "Grishma Neupane" #these are attributes
    age = 23
    marks = 98  

    def display(one): #these are methods
        print(one)
        #print(name) - this create error
        print("I am GRISHMA NEUPANE")  
std1 = Student() #here a variable std1 call the class student - object       
print(std1)

#By only defining a class doesn't works, we need to create the objects of the class
#To create the object, we need to call the class
# when a variable call the class, it become object
#The properties of class should be accessed through object

print(std1.name)
print(std1.age)
print(std1.marks)
std1.display() #function call like this and this shows error - we need parameter like one or self
#self parameter can be used on methods
# self le jun object bata method call bhairaxa tehi object lai linxa

std2 = Student()
print(std2)
print(std2.name)
print(std2.age)
print(std2.marks)
std2.display()

#Class Attributes -> The value of attribute donot change according to the object
#Object Attributes -> The value of attributes changes according to the object
#To create object attributes, we need a method that assigns value to the attribute

class Students:
    def set_info(self,name,age,marks):
        self.name = name    #these are object attributes
        self.age = age
        self.marks = marks
    def display(self):
        print(f"Name ={self.name}")
        print(f"Age ={self.age}")
        print(f"Marks ={self.marks}")
std1 = Students()  
print(std1)     
std1.set_info("Grishma",23,99) #set_info method is called by an object 'std1'
std1.display() #It is called so the content inside display gets printed
print()

std2 = Students()
print(std2)
std2.set_info("Laxmi",24,25)
std2.display()

#del -> deletes the property of class but cannot delete a class

print(std1.name)
del std1.name
#print(std1.name) already deleted so showed error

print(std2.name)
del std2.name
print()
#std1.display()
std2.display()
