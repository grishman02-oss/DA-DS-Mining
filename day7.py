#While loop
# used when we don't know tje stopping condition
#syntax:
#while condition:
#  code to be executed
#Infinite loop => The loop keeps executing without any stopping condition
#Stopping condition should be given


#Calculator program using while loop
#The most use case of while loop 

while True:
    choice = input("Enter 1 for division, 2 for modulus, 3 for floor division, 4 for power, 5 for exit : ")
    match choice:
        case '1':
            num1=int(input("Enter number 1:"))
            num2=int(input("Enter number 2:"))
            print(num1/num2)
        case '2':
            num1=int(input("Enter number 1:"))
            num2=int(input("Enter number 2:")) 
            print(num1%num2)
        case '3':
            num1=int(input("Enter number 1:"))
            num2=int(input("Enter number 2:"))       
            print(num1//num2)
        case '4':
            num1=int(input("Enter number 1:"))
            num2=int(input("Enter number 2:"))
            print(num1**num2)
        case '5':
            print("Exiting the program")
            break
        case _:
            print("Invalid choice")


#Nested Loop
list1 =[i for i in range(100)]
print(list1.index(95))
print(list1) 

print(list[-5:-10:2])