#Exception Handling
#also called Error Handling

# list1 = [1,2,3,4,5]
# print(list1[0])
# print(list1[-1]) #negative indexing
# print(list1[10]) #This leads to error cause index 1o isnot present in the list.
#so to handle this error, we use Try and Except keyword

#try => In try block, we write the code that may raise an error
#error aauna sakhne code lai try block bhitra lekhne
#If error occured then except block(code written here) is executed
#If error aayena vaney,[else] try block gets executed

#except => In except, we write the code that is executed if error occured in try block

# list1 = [1,2,3,4,5]
# try:
#     print(list1[10]) #this line bring error so we write it inside try block
# except:
#     print("An error occured") 


# num1 = int(input("Enter number 1:"))
# num2 = int(input("Enter number 2:"))
# print(num1+num2)
#if we write string like my name when it accept only integer then it shows us value error
#so to handle error

# list1 = [1,2,3,4,5]
# try:
#     print(list1[2])
#     num1 = int(input("Enter number 1:"))
#     num2 = int(input("Enter number 2:"))
#     print(num1+num2)
# except:
#     print("An error occured")    


#Index error, Value Error, Zero Division Error - sabai ma except code run hunxa

#General Error Handling
# Jasto sukai error aayeni(index, value, zero) euta except block le kaam gari raxa vaney teslai general error handling vaninxa


#Special Error Handling
#Each error lai xutta xuttai handle garnu parxa
#Euta try bhitra multiple except haru lekhnu parxa
#Except pachadi error name dinu parxa
# list1 = [1,2,3,4,5]
# try:
#     print(list1[1])
#     num1 = int(input("Enter number 1:"))
#     num2 = int(input("Enter number 2:"))
#     print(num1/num2)
#     file = open("aaa.txt", "r") #yesto case ma arkai error aauxa cause aaa.txt file xaina
#                            #to read from it so error aauxa
#     file.close()
# except IndexError:
#     print("Index not found")
# except ValueError:
#     print("Cannot convert into integer")
# except ZeroDivisionError:
#     print("Num2 cannot be 0") 
# except:            #index,value,zero handle by specific tyo bhayek aru error yesle handle garxa
#     print("An error occured")      #for file handling and for other also

#we can use for loop inside except
#we can do anything inside except

list1 = [1,2,3,4,5]
try:
    print(list1[1])
    num1 = int(input("Enter number 1:"))
    num2 = int(input("Enter number 2:"))
    print(num1/num2)
    file = open("aaa.txt", "r") #yesto case ma arkai error aauxa cause aaa.txt file xaina
    file.close() #to read from it so error aauxa
except IndexError:
    for i in range(10):
        print(i)
except ValueError:
    print("Cannot convert into integer")
except ZeroDivisionError:
    print("Num2 cannot be 0") 
except FileNotFoundError:            
     file=open("aaa.txt","w") #file is created. error is handled by creating a file
     file.close()

#If index error le jhe value return garxa, tehi kura print garna mann lagyo vaney
#Specific error handling with intial error message
list1 = [1,2,3,4,5]
try:
    print(list1[1])
    num1 = int(input("Enter number 1:"))
    num2 = int(input("Enter number 2:"))
    print(num1/num2)
    file = open("aaa.txt", "r") 
    file.close()
except IndexError as ie:
    print(ie)    
except ValueError as ve:
    print(ve)
except ZeroDivisionError as ze:
    print(ze)
except:
    print("An error occured")     

#This is called custom error handling

#Recommended way
list1 = [1,2,3,4,5]
try:
    print(list1[3])
    num1 = input("Enter number 1:")
    num2 = input("Enter number 2:")
    print(num1/num2) 
    file = open("aaa.txt","r")
    file.close()
except Exception as e:
    print("An error occured:", e)   

#exception => handle index, value, zerodivision
#specific error handling as well as SEH with initial error message

#Finally => cannot handle error even though it is printed
#Finally block is executed either when error is occured or not
list1 = [1,2,3,4,5]
try:
    print(list1[10])
    num1 = input("Enter number 1:")
    num2 = input("Enter number 2:")
    print(num1/num2) 
    file = open("aaa.txt","r")
    file.close()
except Exception as e:
    print("An error occured:", e) 
finally:
    print("It is executed or printed anyways")   

#finally ma pani aru code garna payinxa like loop mostly print is done
# Nested try except:
# try bhitra try-except and except bhitra pani try-except garna payinxa     
