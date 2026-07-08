# Question 1: Create and Write a File

with open("student.txt", "w") as file:
    file.write("Name: Rishabh Bhaskar Shahi\n")
    file.write("Age: 19\n")
    file.write("College: Buddha Institute of Technology\n")

print("File created successfully")


# Question 2: Read a File

print("\nContents of student.txt:")
with open("student.txt", "r") as file:
    print(file.read())


# Question 3: Append to a File

with open("student.txt", "a") as file:
    file.write("Course: Python Data AI\n")
    file.write("City: Umaria\n")

print("Updated student.txt:")
with open("student.txt", "r") as file:
    print(file.read())


# Question 4: Count Lines in a File

with open("student.txt", "r") as file:
    lines = file.readlines()

print("Total lines:", len(lines))


# Question 5: Write Multiple Students

students = ["Aman", "Priya", "Shalu", "Raj", "Ansh"]

with open("students.txt", "w") as file:
    for student in students:
        file.write(student + "\n")

print("\nStudent Names:")
with open("students.txt", "r") as file:
    print(file.read())


# Question 6: Search a Name in File

search_name = input("Enter a student name: ")

with open("students.txt", "r") as file:
    names = [line.strip() for line in file]

if search_name in names:
    print("Found")
else:
    print("Not Found")


# Question 7: Copy File Content

with open("students.txt", "r") as source:
    content = source.read()

with open("students_backup.txt", "w") as backup:
    backup.write(content)

print("Backup created successfully")


# Question 8: Marks File Summary

marks = [85, 90, 78, 92, 88]

with open("marks.txt", "w") as file:
    for mark in marks:
        file.write(str(mark) + "\n")

with open("marks.txt", "r") as file:
    marks = [int(line.strip()) for line in file]

total = sum(marks)
average = total / len(marks)

print("Total marks:", total)
print("Average marks:", average)