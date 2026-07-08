# ===========================
# Question 1: Create and Write a File
# ===========================

with open("student.txt", "w") as file:
    file.write("Name: Ashish Sharma\n")
    file.write("Age: 20\n")
    file.write("College: BIT\n")

print("File created successfully")


# ===========================
# Question 2: Read a File
# ===========================

print("\nQuestion 2 Output:")
with open("student.txt", "r") as file:
    print(file.read())


# ===========================
# Question 3: Append to a File
# ===========================

with open("student.txt", "a") as file:
    file.write("Course: Python Data AI\n")
    file.write("City: Gorakhpur\n")

print("\nUpdated File:")
with open("student.txt", "r") as file:
    print(file.read())


# ===========================
# Question 4: Count Lines
# ===========================

with open("student.txt", "r") as file:
    lines = file.readlines()

print("Total lines:", len(lines))


# ===========================
# Question 5: Write Multiple Students
# ===========================

students = ["Aman", "Priya", "Shalu", "Raj", "Ansh"]

with open("students.txt", "w") as file:
    for student in students:
        file.write(student + "\n")

print("\nStudent Names:")
with open("students.txt", "r") as file:
    print(file.read())


# ===========================
# Question 6: Search Name in File
# ===========================

name = input("Enter student name: ")

found = False

with open("students.txt", "r") as file:
    for student in file:
        if student.strip().lower() == name.lower():
            found = True
            break

if found:
    print("Found")
else:
    print("Not Found")


# ===========================
# Question 7: Copy File Content
# ===========================

with open("students.txt", "r") as source:
    data = source.read()

with open("students_backup.txt", "w") as backup:
    backup.write(data)

print("Backup created successfully")


# ===========================
# Question 8: Marks File Summary
# ===========================

marks = [85, 90, 78, 92, 88]

with open("marks.txt", "w") as file:
    for mark in marks:
        file.write(str(mark) + "\n")

total = 0
count = 0

with open("marks.txt", "r") as file:
    for line in file:
        total += int(line.strip())
        count += 1

average = total / count

print("Total marks:", total)
print("Average marks:", average)