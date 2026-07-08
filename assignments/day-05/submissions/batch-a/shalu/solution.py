### Question 1: Create and Write a File

# Create a file named `student.txt`. Write your name, age, and college name in the file. Then print `File created successfully`.

# Expected Output:
# File created successfully
with open("student.txt","w") as file:
    file.write("Name: Rahul \nAge: 20\nCollege: BIT")
print("File created successfully")
print("="*45)
### Question 2: Read a File

#Read the `student.txt` file created in Question 1 and print its content.

# Expected Output:
# Name: Rahul
# Age: 20
# College: BIT
with open("student.txt","r") as file:
    content = file.read()
print(content)
print("="*45)

### Question 3: Append to a File

# Append your course name and city to `student.txt`. Then read and print the updated file content.

# Expected Output:
# Name: Rahul
# Age: 20
# College: BIT
# Course: Python Data AI
# City: Gorakhpur

with open("student.txt","a") as file:
    file.writelines("\nCourse: Python Data AI\nCity: Gorakhpur")
with open("student.txt","r") as file:
    content = file.read()
print(content)
print("="*45)

### Question 4: Count Lines in a File

# Count the total number of lines in `student.txt` and print the result.

# Expected Output:
# Total lines: 5

with open("student.txt","r") as file:
    content = file.readlines()   
print("Total lines:",len(content))
print("="*45)

### Question 5: Write Multiple Students

# Create a file named `students.txt`. Write 5 student names, one name on each line. Read the file and print all names.

# Expected Output:
# Aman
# Priya
# Shalu
# Raj
# Ansh

with open("students.txt","w") as file:
    file.writelines("Aman \nPriya \nShalu \nRaj \nAnsh")
with open("students.txt","r") as file:
    content = file.read()
print(content)
print("="*45)

### Question 6: Search a Name in File

# Ask the user to enter a student name. Check whether that name exists in `students.txt`. Print `Found` if the name exists, otherwise print `Not Found`.

# Example Input:
# Priya
#
# Expected Output:
# Found
name=input("enter the name ")
found=False
with open("students.txt","r")as file:
    for line in file:
        if line.strip()==name:
            found=True
            break
if found==True:
    print("Found")
else:
    print("not found")
print("="*45)
### Question 7: Copy File Content

# Copy all content from `students.txt` to a new file named `students_backup.txt`. Then print `Backup created successfully`.

# Expected Output:
# Backup created successfully
with open("students.txt","r") as file:
    data=file.read()
with open("students_backup.txt","w") as file2:
    file2.write(data)
print("Backup created successfully")
print("="*45)
### Question 8: Marks File Summary

# Create a file named `marks.txt` with 5 marks, one mark on each line:

# 85
# 90
# 78
# 92
# 88

# Read the marks from the file and print the total marks and average marks.
with open("marks.txt","w") as file:
    file.write("85\n90\n78\n92\n88\n")
marks=[]
with open("marks.txt","r") as file:
    data = file.readlines()
for mark in data:
    marks.append(int(mark.strip()))
total_marks=sum(marks)
average_marks=total_marks/len(marks)

print("Total marks:",total_marks)
print("Average marks:",average_marks)
print("="*45)

