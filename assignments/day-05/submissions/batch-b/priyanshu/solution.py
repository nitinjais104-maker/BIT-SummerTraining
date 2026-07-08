### Question 1: Create and Write a File
file = open("student.txt", "w")
file.write("Name: PRIYANSHU\nAge: 21\nClg_name: BIT.")
print("File created successfully.")
file.close()


### Question 2: Read a File
file = open("student.txt", "r")
content = file.read()
print(content)
file.close()    

### Question 3: Append to a File
file = open("student.txt", "a")
file.write("\nCourse: B.Tech/nCity: Jaipur")
file.close()

### Question 4: Count Lines in a File
file = open("student.txt", "r")
lines = file.readlines()
print("Total lines:", len(lines))
file.close()

### Question 5: Write Multiple Students
file = open("students.txt", "w+")
file.write(" PRIYANSHU\n AMAN\n ALOK\n UTTAM\n AKASH\n")
file = open("students.txt", "r")
content = file.read()
print(content)
file.close()

### Question 6: Search a Name in File
name = input("Enter a name to search: ")
file = open("students.txt", "r")
content = file.read()
if name in content:
    print("Found")
else:
    print("Not Found")
    
    
### Question 7: Copy File Content
file = open("students.txt", "r")
content = file.read()

backup = open("students_backup.txt", "w")
backup.write(content)

file.close()
backup.close()

print("Backup created successfully")



### Question 8: Marks File Summary
# Read marks from file
file = open("marks.txt", "r")
total = 0
count = 0

for line in file:
    total += int(line.strip())
    count += 1
file.close()

average = total / count
print("Total marks:", total)
print("Average marks:", average)