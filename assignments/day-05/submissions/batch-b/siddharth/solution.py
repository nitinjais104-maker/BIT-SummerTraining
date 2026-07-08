name = "Rahul"
age = 20
college = "BIT"
course = "Python Data AI"
city = "Gorakhpur"

f = open("student.txt", "w")
f.write("Name: " + name + "\n")
f.write("Age: " + str(age) + "\n")
f.write("College: " + college + "\n")
f.close()
print("File created successfully")

f = open("student.txt", "r")
content = f.read()
print(content)
f.close()

f = open("student.txt", "a")
f.write("Course: " + course + "\n")
f.write("City: " + city + "\n")
f.close()

f = open("student.txt", "r")
content = f.read()
print(content)
f.close()

f = open("student.txt", "r")
lines = f.readlines()
print("Total lines:", len(lines))
f.close()

students = ["Aman", "Priya", "Shalu", "Raj", "Ansh"]
f = open("students.txt", "w")
for s in students:
    f.write(s + "\n")
f.close()

f = open("students.txt", "r")
content = f.read()
print(content)
f.close()

search_name = input("Enter a student name: ")
f = open("students.txt", "r")
lines = f.read().splitlines()
f.close()

if search_name in lines:
    print("Found")
else:
    print("Not Found")

f1 = open("students.txt", "r")
data = f1.read()
f1.close()

f2 = open("students_backup.txt", "w")
f2.write(data)
f2.close()
print("Backup created successfully")

f = open("marks.txt", "w")
f.write("85\n90\n78\n92\n88\n")
f.close()

f = open("marks.txt", "r")
lines = f.readlines()
f.close()

marks = []
for line in lines:
    marks.append(int(line.strip()))

total = sum(marks)
average = total / len(marks)

print("Total marks:", total)
print("Average marks:", round(average, 1))