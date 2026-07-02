## Day 5 Assignment
## Topic: Python File Handling
## Question. 1 Create and write a file
# Print("Create a file named student.txt. Write your name,age,and college name in the file. Then print File created successfully.")
file = open("student.txt","w") # create and write to student.txt
file.write("Name:Ritu\n") # variables name
file.write("Age:25\n") # variables age
file.write("College:Buddha institute of magament\n") # print the value of college name
file.close() 

print("File created successfully.")

## Question 2: Read a file
# Print("Read the student.txt file created in Question 1 and print its content.")
file = open("student.txt","r") # Read and print the contents of student.txt
content = file.read()
print(content)

## Question 3: Append to a file
# Print("Append your course name and city to student.txt.Then read and print the updated file content.")
file = open("student.txt","a") # append course name and city to student.txt
file.write("Course:MCA\n")
file.write("City: Gorkhpur\n")

file = open("student.txt","r") # read and print the updated file content 
content = file.read()
print(content)

## Question 4: Count Lines in a file
# print("Count the total number of lines in student.txt and print the result.")
file = open("student.txt", "r")
lines = file.readlines()
print("Total lines:", len(lines))
file.close()

## Question 5: Write Multiple Students
# Print("Create a file named students.txt.Write 5 student names, one name on each line. Read the filr and print all names.")
file = open("students.txt","w") # create and write 5student names to students.txt
file.write("Ritu\n")
file.write("Atul\n")
file.write("Ankita\n")
file.write("Anmol\n")
file.write("Anjali\n")

file = open("students.txt","r") # read and print all names
content = file.read()
print(content) # print the value

## Question 6: Search a Name in file
# print("Ask the user to e3nter a student name.check whether that name exists in students.txt.print found if the name exists,otherwise print not found.")
name = input("Ritu:") # ask the user to enter a student name
file = open("students.txt","r") # read the file and check if the name exists
students = file.read().splitlines()

if name in students:
    print("Found")
else:
    print("Not found")
 
 ## Question 7: Copy File Content
 # print("Copy all content from students.txt to a new file named students_backup.txt.Then print Backup created successfully.")
file = open("students.txt","r") # copy all content from students.txt to students_backup.txt.rad the original file.
content = file.read()
backup = open("students_backup.txt","w") # write the content to the backup file
backup.write(content)

print("Backup created successfully:") # print backup created successfully

## Question 8: Marks File Summary
# print("Create a file named marks.txt with 5 marks,one marks on each line:")
file = open("marks.txt", "r")
total = 0
count = 0

for line in file:
    total += int(line.strip())
    count += 1
file.close()

average = total / count
print("Total marks:", total)
print("Average marks:", average)