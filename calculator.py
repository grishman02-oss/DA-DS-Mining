#Update calculator program using function

def add(a,b):  # define function for each operation
    print(a+b)
def sub(a,b):
    print(a-b)
def mul(a,b):
    print(a*b)
def div(a,b):
    print(a/b)
def power(a,b):
    print(a**b)    
        

num1 = float(input("Enter first number:"))
num2 = float(input("Enter second number:"))

choice = input("Enter 1 for addition, 2 for subtraction, 3 for multiplication, 4 for division, 5 for power:")

match choice:
    case '1':
        add(num1, num2) #function is called
    case '2':
        sub(num1, num2)
    case '3':
        mul(num1, num2)        
    case '4':
        div(num1, num2)
    case '5':
        power(num1, num2)        
    case _:
        print("Invalid choice")  
        

#calculator program using function and loop(while)

def add(a,b):  # define function for each operation
    print(a+b)
def sub(a,b):
    print(a-b)
def mul(a,b):
    print(a*b)
def div(a,b):
    print(a/b)
def power(a,b):
    print(a**b)          

# num1 = float(input("Enter first number:"))
# num2 = float(input("Enter second number:"))

while True:
    num1 = float(input("Enter first number:"))
    num2 = float(input("Enter second number:"))
    choice = input("Enter 1 for addition, 2 for subtraction, 3 for multiplication, 4 for division, 5 for power, 6 for exit: ")
    if choice == '1':
        add(num1,num2)
        

    elif choice == '2':
        sub(num1,num2)
        

    elif choice == '3':
        mul(num1,num2)
        

    elif choice == '4':
        if num2 != 0:
            div(num1,num2)
            
        else:
            print("Cannot Divide by Zero")

    elif choice == '5':
        power(num1,num2)
        

    elif choice == '6':
        print("Exit the program")
        break

    else:
        print("Invalid Input")           



       
