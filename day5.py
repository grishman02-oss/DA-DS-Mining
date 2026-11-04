#match
#match matches the cases

#syntax:
#  match variable_name:
#        case possible_value1:
             #code to be executed
#        case possible_value2:
             #code to be executed
#        case possible_value3:
            # code to be executed
#        case_: #default case
            #default code


choice = input("Enter 1 for subtraction, 2 for multiplication, 3 for division, 4 for power, 5 for floor division, 6 for modulus: ")
match choice:
    case '1':
        num1 = int(input("Enter first number:"))
        num2 = int(input("Enter second number:"))
        print("Subtraction=", num1-num2)
    case '2':
            num1 = int(input("Enter first number:"))
            num2 = int(input("Enter second number:"))
            print("Multiplication=", num1*num2)
    case '3':
          num1 = int(input("Enter first number:"))
          num2 = int(input("Enter second number:"))
          print("Division=", num1/num2)
    case '4':
            num1 = int(input("Enter first number:"))
            num2 = int(input("Enter second number:"))
            print("Power=", num1**num2)   
    case '5':
            num1 = int(input("Enter first number:"))
            num2 = int(input("Enter second number:"))
            print("Floor Division=", num1//num2) 
    case '6':
            num1 = int(input("Enter first number:"))
            num2 = int(input("Enter second number:"))
            print("Modulus=", num1%num2) 
    case _ :
            print("Invalid Input")    


#Login Register with Username only

usernames = ['Grishma', 'Ram', 'Sita', 'Fatima'] #when we run the code and register the name there then we can write here.

choice = input("Enter 1 for Register, 2 for Login:")

match choice:
       case '1':
              username = input("Enter your username:")
              usernames.append(username)
              print(usernames)
       case '2':
              username = input("Enter your username:")
              if username in usernames:
                     print("Login Successful")
              else:
                     print("Login Failed")
       case _ :
              print("Invalid Input")                     
                           