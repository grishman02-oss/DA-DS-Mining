#1. Create and Write a File
#Write a program to create a new text file named notes.txt,write multiple lines of text into it,
#and ensure the file closes properly using a with statement.

# file = open("notes.txt", "w")
# content = file.write("Nepal is hit by massive flood \n")
# file.write("Bhotekoshi flood \n")
# file.write("Grishma Neupane")
# print(content)
# file.close()

#using with statement - with open and close file automatically no need to write file.close()
with open("notes.txt", "w") as file:
    content = file.write("Today is very sunny \n")
    file.write("Another flood happened today \n")
    file.write("Using with statement")

#2. Read Entire File Content.
# Write a program to open notes.txt in read mode ('r'), load all its text into a string 
# using read(), and print the contents to the console.   

file = open("notes.txt", "r")
content = file.read()
print(content)
file.close()

with open("notes.txt", "r") as file:
    file.read()   


#3.Read File Line by Line
#Write a program that iterates through notes.txt using a for loop to read and print each line
#individually after stripping out extra newline characters.
with open("notes.txt", "r") as file:
    for line in file:
        print(line.strip())
#for line in file: reads one line at a time.
#strip() removes extra whitespace, including the newline character \n. 


#4.Append New Data
#Write a program to open notes.txt in append mode ('a') and add a new timestamp or log line to 
#the bottom without erasing existing content.
from datetime import datetime

file = open("notes.txt", "a")
file.write("\nUpdated at:"+str(datetime.now())+"\n")
print("New data added")
file.close()
datetime.now() #gets the current date and time.
#str() converts the date and time into a string.

#5.Count Lines, Words, and Characters
#Write a program that opens a text file, counts the total number of lines, words, and characters 
#inside it, and displays the summary.

with open("notes.txt", "r") as file:
    content = file.read()

Lines = content.splitlines() # count lines
words = content.split() # count words
characters = len(content) # count characters

print("Total lines:", len(Lines))
print("Total words:", len(words))
print("Total character:", characters)
#splitlines() method separates a string into a list of lines.
#split() method separates a string into a list of words using whitespace such as spaces, tabs, and newlines.
#len() function returns the length of a string, list, tuple, or other supported collection.

#6. Find and Replace Text
#Write a program that reads a file, searches for a specific target word (for example, change all 
#instances of "old" to "new"), and saves the updated text back to the file.

with open("notes.txt", "r") as file:
    content = file.read()

updated_content = content.replace("flood", "landslides")

with open("notes.txt", "w") as file:
    file.write(updated_content)
print("Text replaced successfully")  

#7. Copy File Contents
# Write a program that opens a source file (source.txt), reads its content, and writes that 
#exact content into a new destination file (backup.txt).
with open("notes.txt", "r") as file:
    content = file.read()

with open("backup.txt","w") as file:
    file.write(content)

#8.Read and Write CSV Data
#Write a program using Python's built-in csv module to read rows from a .csv file, filter or
#modify the data, and write the output into a new .csv file   

#CSV stands for Comma-Separated Values.
#CSV file is a file used to store data in a table-like format, where values are usually separated by commas. 




