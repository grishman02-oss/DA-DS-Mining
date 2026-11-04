#To develop simple calculator
# Simple Calculator

num1 = float(input("Enter the first number: "))
operator = input("Enter an operator (+, -, *, /): ")
num2 = float(input("Enter the second number: "))

if operator == "+":
    result = num1 + num2
elif operator == "-":
    result = num1 - num2
elif operator == "*":
    result = num1 * num2
elif operator == "/":
    result = num1 / num2
else:
    result = "Invalid operator"

print("Result:", result)

#Calculator

num1 = float(input("Enter a number: "))
num2 = float(input("Enter another number: "))

print("Addition: ", num1 + num2)
print("Subtraction: ", num1 - num2)
print("Multiplication: ", num1 * num2)
print("Division: ", num1 / num2)

name = input("Enter your name: ")
print("My Name is" + " " + name )
print("My name is:", " ", name)