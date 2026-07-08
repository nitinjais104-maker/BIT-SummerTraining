
# ----------------------------------------------------------------------
# Question 1: Create and Write a File
# ----------------------------------------------------------------------
with open("student.txt", "w") as f:
    f.write("Name: Rahul\n")
    f.write("Age: 20\n")
    f.write("College: BIT\n")

print("File created successfully")


# ----------------------------------------------------------------------
# Question 2: Read a File
# ----------------------------------------------------------------------
with open("student.txt", "r") as f:
    content = f.read()

print(content)


# ----------------------------------------------------------------------
# Question 3: Append to a File
# ----------------------------------------------------------------------
with open("student.txt", "a") as f:
    f.write("Course: Python Data AI\n")
    f.write("City: Gorakhpur\n")

with open("student.txt", "r") as f:
    updated_content = f.read()

print(updated_content)


# ----------------------------------------------------------------------
# Question 4: Count Lines in a File
# ----------------------------------------------------------------------
with open("student.txt", "r") as f:
    lines = f.readlines()

print(f"Total lines: {len(lines)}")


# ----------------------------------------------------------------------
# Question 5: Write Multiple Students
# ----------------------------------------------------------------------
students = ["Aman", "Priya", "Shalu", "Raj", "Ansh"]

with open("students.txt", "w") as f:
    for name in students:
        f.write(name + "\n")

with open("students.txt", "r") as f:
    for line in f:
        print(line.strip())


# ----------------------------------------------------------------------
# Question 6: Search a Name in File
# ----------------------------------------------------------------------
search_name = input("Enter a student name: ").strip()

with open("students.txt", "r") as f:
    all_names = [line.strip() for line in f.readlines()]

if search_name in all_names:
    print("Found")
else:
    print("Not Found")


# ----------------------------------------------------------------------
# Question 7: Copy File Content
# ----------------------------------------------------------------------
with open("students.txt", "r") as source:
    data = source.read()

with open("students_backup.txt", "w") as backup:
    backup.write(data)

print("Backup created successfully")


# ----------------------------------------------------------------------
# Question 8: Marks File Summary
# ----------------------------------------------------------------------
marks_list = [85, 90, 78, 92, 88]

with open("marks.txt", "w") as f:
    for mark in marks_list:
        f.write(str(mark) + "\n")

with open("marks.txt", "r") as f:
    marks = [int(line.strip()) for line in f.readlines()]

total_marks = sum(marks)
average_marks = total_marks / len(marks)

print(f"Total marks: {total_marks}")
print(f"Average marks: {average_marks}")