# Day 3 Assignment

# 1. Create a list of 5 student names and print all names.
students = ["Ashish", "Rahul", "Aman", "Rohit", "Ankit"]
print("Student Names:", students)

# 2. Add one new student name to the list.
students.append("Sumit")
print("Updated Student List:", students)

# 3. Create a tuple of 5 city names and print the second city.
cities = ("Lucknow", "Kanpur", "Delhi", "Mumbai", "Jaipur")
print("Second City:", cities[1])

# 4. Create a set of 5 course names and add one new course.
courses = {"Python", "Java", "C", "HTML", "CSS"}
courses.add("Machine Learning")
print("Courses:", courses)

# 5. Create a dictionary for one student.
student = {
    "name": "Ashish Sharma",
    "branch": "CSE",
    "batch": "B",
    "marks": 85
}

# 6. Print the student dictionary in a readable format.
print("\nStudent Details")
print("Name:", student["name"])
print("Branch:", student["branch"])
print("Batch:", student["batch"])
print("Marks:", student["marks"])