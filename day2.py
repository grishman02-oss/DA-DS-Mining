#Operators
#Operators are the symbols that performs specific operation

#Types:
#1. Arithmetic Operators => +, -, *, /, %, **, // => FLOOR DIVISION
# 2. Comparison Operators => ==, !=, <, >, <=, >=, == Boolean answer
# 3. Logical  Operators => and, or, not => Used in 2 conditions 
  # and, or need 2 conditions to be true or false (a>b and c<d) (a<b or c>d)
  # not => 1 condition to be true or false , change true to false and false to true of condition 1
# 4. Assignment Oprators => =, +=, -=, *=, /=, %=, **=, //= => used to assign value to variable

a = 10
print(a)
a += 5
print(a)

# 5. Membership Operators => Checks if data is prrsent in group data type or not => in, not in
#6. Identity Operators => check the memory location instead of actual value


# Normal Calculator Program
#num1 = input("Enter number 1: ")
#num2 = input("Enter number 2: ")
#print(num1 + num2) This program will not work becaue we didnot defined the
#datatype. So it will concatenate the 2 number when we try to add it


num1 = int(input("Enter number 1: "))
num2 = int(input("Enter number 2: "))
print(num1 + num2)

# we should convert str into int
#Converting from one data type to another data type => Type Casting
#int() => convert any data type into integer
#float() => convert any data type into float
#str() => convert any data type into string
#bool() => convert any data type into boolean

#Value error => when we try to convert str into int or float
 # task : write a program to develop a simple calculator

 #type() = type() gives the data type of an element

a = 10
print(type(a))

b = 10.5
print(type(b))

c = "Abcd"
print(type(c))

d = True
print(type(d))

