#day5
# Question 1: Create and Write a File
# Expected Output:
# File created successfully
with open("student.txt", "w") as file:
    file.write("Name: Rahul\n")
    file.write("Age: 20\n")
    file.write("College: BIT\n")
print("File created successfully")

# Question 2: Read a File
# Expected Output:
# Name: Rahul
# Age: 20
# College: BIT
with open("student.txt", "r") as file:
    print(file.read())


# Question 3: Append to a File
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
# Expected Output:
# Total lines: 5
with open("student.txt", "r") as file:
    total_lines = len(file.readlines())

print("Total lines:", total_lines)


# Question 5: Write Multiple Students
# Expected Output:
# Aman
# Priya
# Shalu
# Raj
# Ansh
students = ["Aman", "Priya", "Shalu", "Raj", "Ansh"]
with open("students.txt", "w") as file:
    for student in students:
        file.write(student + "\n")
with open("students.txt", "r") as file:
    print(file.read())

# Question 6: Search a Name in File
# Example Input:
# Priya
# Expected Output:
# Enter student name: Priya
# Found
name = input("Enter student name: ")
with open("students.txt", "r") as file:
    data = file.read().splitlines()
if name in data:
    print("Found")
else:
    print("Not Found")


# Question 7: Copy File Content
# Expected Output:
# Backup created successfully
with open("students.txt", "r") as file:
    content = file.read()
with open("students_backup.txt", "w") as file:
    file.write(content)
print("Backup created successfully")


# Question 8: Marks File Summary
# Expected Output:
# Total marks: 433
# Average marks: 86.6
marks = [85, 90, 78, 92, 88]
with open("marks.txt", "w") as file:
    for mark in marks:
        file.write(str(mark) + "\n")
with open("marks.txt", "r") as file:
    marks_data = file.readlines()
total = sum(int(mark) for mark in marks_data)
average = total / len(marks_data)
print("Total marks:", total)
print("Average marks:", average)
