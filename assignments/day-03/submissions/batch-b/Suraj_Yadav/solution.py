#1. Create a list of 5 student names and print all names
students = ["Suraj", "Aman", "Rohit", "Neha", "Priya"]

print(students)

#2. Add a new student
students.append("Sunita")
print(students)

#3. Tuple of 5 cities and print second city
cities = ("Delhi", "Mumbai", "Kolkata", "Chennai", "Bangalore")
print("Second city:", cities[1])

#4. Set of 5 courses and add one course
courses = {"Python", "Java", "C++", "JavaScript", "SQL"}
courses.add("React")
print("Courses:", courses)


#5. Student Dictionary
student = {
    "name": "Suraj",
    "branch": "CSE",
    "batch": "2026",
    "marks": 85
}
print("Student:", student)

#6. Print Dictionary
for key, value in student.items():
    print(f"{key}: {value}")