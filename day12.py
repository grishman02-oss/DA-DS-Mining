#File Handling
#Open the file : file = open("file_path", mode)
#Perform operation on the file
#Close the file => file.close()

#Mode of Operation on the file
#r=> read mode
#w=> write mode
#a=> append mode

#r mode=> read the content of the file
# file.read()
#If the file is opened in read mode, but the file doesn't exist, then it throws an error

# file = open("abc.txt", "r")
# content = file.read()
# file.close()
# print(content)


#w-mode => Write the content in the file
# we can write only string or JSON in the file

#JSON = Javascript Object Notation => It is similar to dictionary
#If the file is opened in write mode, but the file doesn't exist, then it creates a new file with 
#the name and print the content 
# file = open("abc.txt", "w")
# content = file.write("I recently graduate\n") #If we write anither content replacing this, it will erase from the file and new one is shown
# content = file.write("Grishma Neupane")
# file.close()
# print(content)
# print(content)
#If we write another text, the previous content is erased and only new content is written in the file


#a => append mode
#Append the content in the file at last of file
#we can write only string or JSON in file
# If a file is opened in append mode, but the file doesnot exist, it creates a new file

file = open("abc2.txt", "a")
file.write("I am actually from Chitwan") #content keep adding at last, content doesn't erase when new content is written
file.close()
#In append mode, previous content is preserved and new content is append at last