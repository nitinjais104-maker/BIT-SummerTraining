# Day 3 Assignment solution for Rohan Nishad

# 1. Create a list of 5 student names and print all names.
students = ["Rohan", "Amit", "Priya", "Sneha", "Vikas"]
print("Student names:")
for student in students:
    print(student)

# 2. Add one new student name to the list.
students.append("Anjali")
print("Updated student list:", students)

# 3. Create a tuple of 5 city names and print the second city.
cities = ("Patna", "Mumbai", "Delhi", "Kolkata", "Chennai")
print("Second city:", cities[1])

# 4. Create a set of 5 course names and add one new course.
courses = {"Math", "Physics", "Chemistry", "Biology", "Computer Science"}
courses.add("English")
print("Courses:", courses)

# 5. Create a dictionary for one student with name, branch, batch, and marks.
student_info = {
    "name": "Rohan Nishad",
    "branch": "Computer Science",
    "batch": "B",
    "marks": 88
}

# 6. Print the student dictionary in a readable format.
print("Student information:")
for key, value in student_info.items():
    print(f"{key.capitalize()}: {value}")
