### Question 1: Create and Write a File

with open("student.txt","w") as file:
    student= ["Name: Vipul Yadav\n","Age: 20\n","College: BIT\n"]
    file.writelines(student)
    file.seek(0)
    
print("File created successfully")



### Question 2: Read a File

with open("student.txt","r")as file :
    student = file.read()
print(student)

### Question 3: Append to a File
with open("student.txt","a+")as file:
    file.write("Course: Python Data AI\n")
    file.write("City: Gorakhpur\n")
    file.seek(0)
    student = file.read()
    print(student)


### Question 4: Count Lines in a File
with open("student.txt","r")as file:
    content = file.readlines()
print("Total lines:",len(content))





### Question 5: Write Multiple Students

with open ("students.txt","w+")as file:
    students = ["Aman\n","Priya\n","Shalu\n","Raj\n","Ansh\n"]
    file.writelines(students)
    file.seek(0)
    content =  file.read()
print(content)



### Question 6: Search a Name in File

student_name = input("Enter the Name of student:")
with open ("students.txt","r") as file:
    content = file.read()
    if student_name  in content:
        print("Found")
    else:
        print("Not Found!")


### Question 7: Copy File Content
with open("students.txt","r")as file:
    content = file.read()
with open("students_backup.txt","w") as file_backup:
    file_backup.writelines(content)
    file_backup.seek(0)
print("Backup created successfully!")   


### Question 8: Marks File Summary
with open("marks.txt","w+")as file:
    student_marks = ["85\n","90\n","78\n","92\n","88\n"]
    file.writelines(student_marks)
    file.seek(0)
    marks = file.readlines()
    
    total = 0
    for mark in marks :
        total += int(mark)  
    average = total/len(marks)
    print("Total marks:",total)
    print("Average marks:",average)