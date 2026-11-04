#Constructor -> It is a special kind of method that gets automatically called when an object is created
#there is only one constructor and that is __init__
#constructor is used to define object attributes

class Students:
    def __init__(self,name,age,marks):
        self.name = name    #these are object attributes
        self.age = age
        self.marks = marks
    def display(self):
        print(f"Name ={self.name}")
        print(f"Age ={self.age}")
        print(f"Marks ={self.marks}")
        print()

std1 = Students("Laxmi", 23, 99) #value is pass like this in constructor, don't need to call the method
std1.display()

std2 = Students("Anisha", 78, 55)
std2.display()


#Decorators -> Decorators are the special kind of function that receives another function as an argument
#Decorator has a nested function -> wrapper function
#It is used to modify that received function without changing its original code
#The modification of the received function is handled by the nested function
#Decorator returns the nested function

def my_decorator(func): #func takes a function as an arguments
    def wrapper():
        for i in range(5):
            func()
            print(i) #receive garya function lai call garya
    return wrapper
        
@my_decorator
def display():
    print("I am Grishma Neupane from Bharatpur, Chitwan.")
display()    

#we should use decorator by adding decorator name just above the function and using @ as a prefix

#@my_decorator -> yesko tala ko function lai func ma receive garne bhayo decorator le
#wrapper bhitra jhe code xa tei print hunxa as it modify the function wihtout changing the original code
#we only pre built decorators in pythons
#we don't need to create our own decorators

#Built in decorator
#1. static method decorator
#2. abstract method decorator

#static method: If self isnot used, we donot need to use self parameter by using @staticmethod
class Students:
    def __init__(self,name,age,marks):
        self.name = name
        self.age = age
        self.marks = marks
    def display(self):
        print(f"Name = {self.name}")
        print(f"Age = {self.age}")
        print(f"Marks = {self.marks}")
        print()
    @staticmethod    
    def abc():
        print("ABC")   

std1 = Students("MOHIT", 24, 99) 
std1.abc()            