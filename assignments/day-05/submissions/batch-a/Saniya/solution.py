#Day 5 Assignment
#==========================================================>>>
# Question 1: Create and Write a File
# Create a file named `student.txt`. Write your name, age, and college name in the file. Then print `File created successfully`.
file = open("student.txt", "w")
file.write("Name: Rahul\n")
file.write("Age: 20\n")
file.write("College: BIT\n")
file.close()
print("File created successfully")                                                # File created successfully
print("="*50)
#==========================================================>>>
## Question 2: Read a File
# Read the `student.txt` file created in Question 1 and print its content.
file = open("student.txt", "r")
content = file.read()
print("Content of student.txt:")
print(content)                                                                  # Reading the content of student.txt and printing it
file.close()
print("="*50)
#==========================================================>>>
# Question 3: Append to a File
#Append your course name and city to `student.txt`. Then read and print the updated file content.
file = open("student.txt", "a")
file.write("Course:Python  Data AI\n")
file.write("City: Gorakhpur\n")
file.close()
file = open("student.txt", "r")
content = file.read()
print("Updated content of student.txt:")
print(content)                                                                  # Appending course name and city to student.txt and printing the updated content
file.close()
print("="*50)
#==========================================================>>>
# Question 4: Count Lines in a File
#Count the total number of lines in `student.txt` and print the result.
file = open("student.txt", "r")
lines = file.readlines()
print(f"Total number of lines in student.txt: {len(lines)}")
file.close()
print("="*50)
#==========================================================>>>
# Question 5: Write Multiple Students
#Create a file named `students.txt`. Write 5 student names, one name on each line. Read the file and print all names.
file = open("students.txt", "w")
file.write("Shalu\n")
file.write("Aman\n")
file.write("Priya\n")
file.write("Ansh\n")
file.write("Raj\n")
file.close()
file = open("students.txt", "r")
names = file.readlines()
print("Names in students:")
for name in names:
    print(name.strip())                                                          # Writing 5 student names to students.txt and printing them
file.close()
print("="*50)
#=========================================================>>>
# Question 6: Search a Name in File
# Ask the user to enter a student name. Check whether that name exists in `students.txt`. Print `Found` if the name exists, otherwise print `Not Found`.
name = input("Enter student name: ")
with open("students.txt", "r") as file:
    names = file.read().splitlines()
if name in names:
    print("Found")
else:
    print("Not Found")
print("="*50)                                                                  # Searching for a student name in students.txt and printing the result   
#=========================================================>>>
# Question 7: Copy File Content
# Copy all content from `students.txt` to a new file named `students_backup.txt`. Then print `Backup created successfully`.
file = open("students.txt", "r")
content = file.read()
file.close()
file = open("students_backup.txt", "w")
file.write(content)
file.close()
print("Backup created successfully")                                              # Copying content from students.txt to students_backup.txt and printing success message
print("="*50)
#=========================================================>>>
# Question 8: Marks File Summary
#Create a file named `marks.txt` with 5 marks, one mark on each line:
file = open("marks.txt", "w")
file.write("85\n")
file.write("90\n")
file.write("78\n")
file.write("92\n")
file.write("88\n")
file.close()
file = open("marks.txt", "r")
marks = file.readlines()
total = 0
for mark in marks:
    total = total + int(mark)
average = total / len(marks)
print("Total marks:", total)
print("Average marks:", average)
file.close()
print("="*50)                                                                  # Creating marks.txt with 5 marks, calculating total and average marks, and printing them    
#=========================================================>>>