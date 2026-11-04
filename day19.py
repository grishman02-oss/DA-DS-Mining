#Abstraction
#The main idea of abstraction is showing what is needed hiding the implementation details

#conditions:
#1.The parent class should have inherited from ABC(Abstract Base Class)
#2. The parent class should have at least one abstract method.
#3. The child class should inherit from parent class

#If these 3conditions are satisifed, then
#Every child class that inherits from parent class should also have abstractmethod.

from abc import ABC, abstractmethod

class Teacher(ABC):
    name = "teacher"
    @abstractmethod
    def teaches(self):
        print("I am a teacher")
class EnglishTeacher(Teacher):
    name = "englishteacher"
    def teaches(self):
        print("I am a english teacher")  
class MathTeacher(Teacher):
    name = "mathteacher"
    def teaches(self):
        print("I am a math teacher")  
class ComputerTeacher(Teacher):
    name = "computerteacher"
    def teaches(self):
        print("I am a computer teacher")  

c1 = ComputerTeacher()
print(c1.name)
c1.teaches()
print()
e1 = EnglishTeacher()
print(e1.name)
e1.teaches()
print()
m1=MathTeacher()
print(m1.name)
m1.teaches()
print()


#MAGIC METHODS
#Magic methods are the special type of methods that executes automatically under certain conditions
#Magic methods starts and end with __
#__init__ -> Runs automatically when an object is created
#__str__ ->Runs automatically when an object is printed, always return a value
#__add__ -> + automatically calls __add__
#__sub__ -> - automatically calls __sub__
#__mul__ -> * automatically calls __mul__
#__new__ 


#for every methods, there is a magic methods
class number:
  def __init__(self,value):
    self.value = value

  def __str__(self):
      return f"{self.value} object is being printed"
  def __add__(self,other):
      return f"The addition is {self.value + other.value}"  

n1 = number(12)
print(n1.value)
print(n1)

n2 = number(3)
print(n2.value)
print(n2)

print(n1.value +n2.value)  
print(n1+n2)