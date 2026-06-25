#Question 1: Create a file named student.txt. Write your name, age, and college name in the file.
#  Then print File created successfully.
# Expected Output:
# File created successfully
with open("student.txt", "w") as file:
    file.write("Name: Rahul\n")
    file.write("Age: 20\n")
    file.write("College: BIT\n")

print("File created successfully")

# Question 2: Read a File
# Read the student.txt file created in Question 1 and print its content.
# Expected Output:
# Name: Rahul
# Age: 20
# College: BIT
with open("student.txt", "r") as file:
    print(file.read())

# Question 3: Append to a File
# Append your course name and city to student.txt. Then read and print the updated file content.
# Expected Output:
# Name: Rahul
# Age: 20
# College: BIT
# Course: Python Data AI
# City: Gorakhpur
with open("student.txt", "a") as file:
    file.write("Course: Python Data AI\n")
    file.write("City: Gorakhpur\n")

with open("student.txt", "r") as file:
    print(file.read())



# Question 4: Count Lines in a File
# Count the total number of lines in student.txt and print the result.
# Expected Output:
# Total lines: 5
with open("student.txt", "r") as file:
    lines = file.readlines()

print("Total lines:", len(lines))

# Medium Questions
# Question 5: Write Multiple Students
# Create a file named students.txt. Write 5 student names, one name on each line.
# Read the file and print all names.
# Expected Output:
# Aman
# Priya
# Shalu
# Raj
# Ansh
students = ["Aman", "Priya", "Shalu", "Raj", "Ansh"]

with open("students.txt", "w") as file:
    for name in students:
        file.write(name + "\n")

with open("students.txt", "r") as file:
    for name in file:
        print(name.strip())


# Question 6: Search a Name in File
# Ask the user to enter a student name. Check whether that name exists in students.txt.
# Print Found if the name exists, otherwise print Not Found.
# Example Input:
# Priya
# Expected Output:
# Found
search_name = input("Enter student name: ")

with open("students.txt", "r") as file:
    found = False

    for name in file:
        if name.strip().lower() == search_name.lower():
            found = True
            break

if found:
    print("Found")
else:
    print("Not Found")


# Question 7: Copy File Content
# Copy all content from students.txt to a new file named students_backup.txt. 
# Then print Backup created successfully.
# Expected Output:
# Backup created successfully
with open("students.txt", "r") as source:
    data = source.read()

with open("students_backup.txt", "w") as backup:
    backup.write(data)

print("Backup created successfully")



# Question 8: Marks File Summary
# Create a file named marks.txt with 5 marks, one mark on each line:
# 85
# 90
# 78
# 92
# 88
# Read the marks from the file and print the total marks and average marks.
# Expected Output:
# Total marks: 433
# Average marks: 86.6
marks = [85, 90, 78, 92, 88]

with open("marks.txt", "w") as file:
    for mark in marks:
        file.write(str(mark) + "\n")

total = 0
count = 0

with open("marks.txt", "r") as file:
    for mark in file:
        total += int(mark.strip())
        count += 1

average = total / count

print("Total marks:", total)
print("Average marks:", average)
