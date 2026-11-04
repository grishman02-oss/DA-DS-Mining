#4 Pillars of OOP
#1. Inheritance 2.Encapsulation 3.Abstraction 4.Polymorphism

#Inheritance -> The child classs can access the properties of the parent class
#1.Single Inheritance  2. Multiple Inheritance 3. Multi level Inheritance

#Example of Inheritance
class Dog:
    ears = 2
    legs = 4
    eyes = 2

    def sound(self):
        print("Bark")
    def eats(self):
        print("Bones")    
class GermanShepardDog(Dog):
    color = "Generally black and brown"
    pointed_ears = True
    height = "105cm"
    weight ="greater than 50kg" 
class GoldenRetriver(Dog):
    color = "Mostly golden"
    pointed_ears = False
    height = "105cm"
    weight = "greater than 50kg"

dog1 = Dog() #dog1 is the object of class Dog
print(dog1.ears)  #attribute is printed here
dog1.eats()  #eats method is called here  
#print(dog1.color)    #this leads to error because dog class doesnot have color attributes  

gs1 = GermanShepardDog() 
print(gs1.color)
print(gs1.pointed_ears)   
gs1.eats()   #as Germanshepard inherit the properties and method of Dog 
#first it check on its own class germanshepard, if there is no such method then it check the class from which he inherit

gs1.sound()
print(gs1.eyes)  

#1.Single Inheritance -> one child class inherits from only one parent class
#Task: Update this examples by using object attribute and using the constructor

class Parent:
    name = "Parent"
    def display(self):
        print("Displaying from parent class")
class Child(Parent):
    name = "Child"
    def display(self):
        print("Displaying from child class")
c1 = Child()
print(c1.name)  
c1.display()

#Property Overriding: The child class has the same property of parent class
#parent property is override by child property
 
#2.Multiple Inheritance : One child class inherits from multiple parent classes
class Parent1:
    name ="Parent1"
    def display(self):
        print("Displaying from Parent1 class")
class Parent2:
    name = "Parent2"
    def display(self):
        print("Displaying from Parent2 class")
class Child(Parent1,Parent2):
    pass 
    # name = "Child"
    # def display(self):
    #     print("Displayong from child class")   
#yesto case ma child class ma name and display ko content nabhayesi parent class haru ma check garxa
#first parent1 and then parent2, order wise
c1 = Child()
print(c1.name)
c1.display()   

#3.Multi Level Inheritance
# First, Child inherits from Parent Class
#Then, Parent inherits from Grand Parent class
#so ultimately, child class can access the properties of Grand Parent Class also

class GrandParent:
    name = "Grand Parent"
    def display(self):
        print("Displaying from Grand Parent class")
class Parent(GrandParent):
    name = "Parent" 
    def display(self):
        print("Displaying from Parent Class")
class Child(Parent):
    pass #in this case, child ma name and display xaina vaney it will look for it in parent class
#if parent ma ni xaina vaney, it will inherit from grandparent class
    # name = "Child"
    # def display(self):
    #     print("Displaying from child class")
c1 = Child()
print(c1.name)
c1.display()        