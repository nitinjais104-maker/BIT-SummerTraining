# Question 1: List of 5 student names
students = ["Aman", "Rahul", "Priya", "Neha", "Rohit"]

print("Student Names:")
for name in students:
    print(name)


# Question 2: Add a new student
students.append("Suman")

print("\nAfter adding new student:")
for name in students:
    print(name)


# Question 3: Tuple of 5 cities
cities = ("Delhi", "Mumbai", "Kolkata", "Chennai", "Bangalore")

print("\nSecond city:", cities[1])


# Question 4: Set of 5 courses
courses = {"Python", "Java", "C++", "JavaScript", "SQL"}

courses.add("Data Science")

print("\nCourses:")
for course in courses:
    print(course)


# Question 5: Student dictionary
student = {
    "name": "Aman Singh",
    "branch": "CSE",
    "batch": "2026",
    "marks": 85
}


# Question 6: Print dictionary in readable format
print("\nStudent Details:")
for key, value in student.items():
    print(key, ":", value)