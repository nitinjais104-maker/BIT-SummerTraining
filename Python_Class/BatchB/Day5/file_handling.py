# File handling 
# Create, Read, Write, Append, 
# Update, Delete/Check

# file = open("students.txt", "r")
# content = file.read()
# print(content)
# file.close()


# with open("students.txt", r) as file:
#     content = file.read()
#     print(content)

# with open("students.txt", "w") as file:
#     file.write("Rahul\n")
#     file.write("priya\n")
#     file.write("Aman\n")

# with open("students.txt", "a") as file:
#     file.write("Neha\n")

# students = ["Rahul", "Priya", "Aman", "Neha"]

# with open("students.txt", "w") as file:
#     for student in students:
#         file.write(student + "\n")

# with open("students.txt", "r") as file:
#     for line in file:
#         print("Students:", line.strip())


# citites = ["Gorakhpur", "Delhi", "Gurgaon"]


# count = 0

# with open("students.txt", "r") as file:
#     for line in file:
#         count += 1
    
# print("Total Students:", count)


search_name = "Aman"
found = False

with open("students.txt", "r") as file:
    for line in file:
        if line.strip() == search_name:
            found = True
            break

if found:
    print("Student FOund")
else:
    print("Student Not Found")