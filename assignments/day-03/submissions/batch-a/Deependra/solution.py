# 1. create a list of 5 students names and print all names
students = ["Deependra", "Aryan", "Kuldeep", "Malya", "Rohit"]
print("Student Names:") 
for student in students:
    print(student,end=", ")  #end=", " is used to print all names in one line separated by a comma and space

# 2. Add one new student name to the list
new_student = "Suman"
students.append(new_student)
print("\nUpdated Student Names:")
for student in students:
    print(student, end=", ")  #end=", " is used to print all names in one line separated by a comma and space



# 3. create a tuple of 5 city names and printy the second city name
cities = ("New York", "London", "Paris", "Tokyo", "Sydney")
print("\nSecond City:-->", cities[1])

# 4. create a set of 5 course names and add one new course 
courses = {"Mathematics", "Physics", "Chemistry", "Biology", "Computer Science"}
new_course = "History"  
courses.add(new_course)
print("Updated Courses Set:")
for course in courses:
    print(course, end=", ")  # end=", " is used to print all course names in one line separated by a comma and space

# 5. create a dictionary for one student with name, branch, batch, and marks
student_info={
    "Name": "Deependra",
    "Branch": "Computer Science",
    "Batch": "2028",
    "Marks": 95
}
print("Student Information:")
for key, value in student_info.items():
    print(f"{key}: {value}")