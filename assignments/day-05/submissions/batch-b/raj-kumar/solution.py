## Basic Questions

### Question 1: Create and Write a File

file = open("student.txt", "w")

file.write("Name: Rahul\n")
file.write("Age: 20\n")
file.write("College: BIT \n")

file.close()

print("File created successfully")


### Question 2: Read a File Read the `student.txt` file created in Question 1 and print its content.



# Read and print the contents of student.txt

with open("student.txt", "r") as file:
    content = file.read()

print(content)

### Question 3: Append to a File Append your course name and city to `student.txt`. Then read and print the updated file content.
# Append course name and city to student.txt

with open("student.txt", "a") as file:
    file.write("Course: Python Data AI")
    file.write("\nCity: Gorakhpur")

# Read and print updated content
with open("student.txt", "r") as file:
    content = file.read()

print(content)

# Question 4: Count Lines in a File Count the total number of lines in `student.txt` and print the result.

# Count total number of lines in student.txt

with open("student.txt", "r") as file:
    lines = file.readlines()

print("Total number of lines:", len(lines))

## Medium Questions

### Question 5: Write Multiple Students Create a file named `students.txt`. Write 5 student names, one name on each line. Read the file and print all names.

# Create students.txt and write 5 student names

with open("student.txt", "w") as file:
    file.write("Aman\n")
    file.write("Priya\n")
    file.write("Shalu\n")
    file.write("Raj\n")
    file.write("Ansh\n")

# Read and print all names

with open("student.txt","r") as file:
    content = file.read()

print(content)

### Question 6: Search a Name in File Ask the user to enter a student name. Check whether that name exists in `students.txt`. Print `Found` if the name exists, otherwise print `Not Found`.

# Search a student name in students.txt

name = input("Enter student name: ")

with open("student.txt", "r") as file:
    student = file.read().splitlines()

if name in student:
    print("Found")
else:
    print("Not Found")

### Question 7: Copy File Content Copy all content from `students.txt` to a new file named `students_backup.txt`. Then print `Backup created successfully`.
# Copy content from students.txt to students_backup.txt

source_file = open("student.txt", "r")
content = source_file.read()
source_file.close()

backup_file = open("student_backup.txt", "w")
backup_file.write(content)
backup_file.close()

print("Backup created successfully")

# Question 8: Marks File Summary Create a file named `marks.txt` with 5 marks, one mark on each line:
# Create marks.txt and write marks

file = open("marks.txt", "w")
file.write("85\n")
file.write("90\n")
file.write("78\n")
file.write("92\n")
file.write("88")
file.close()

# Read marks from the file

file = open("marks.txt", "r")
marks = file.readlines()
file.close()

total = 0

for mark in marks:
    total = total + int(mark)

average = total / len(marks)

print("Total marks:", total)
print("Average marks:", average)

