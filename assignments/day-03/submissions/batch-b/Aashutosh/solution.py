
# 1. List of 5 student names

students = ["Aashutosh", "Rahul", "Priya", "Sneha", "Vikram"]
print("List of students:", students)
print("="*30)

# 2. Add one new student name to the list

students.append("Karan")
print("\nUpdated list after adding new student:", students)
print("="*30)

# 3. Tuple of 5 city names, print the second city

cities = ("Kanpur", "Lucknow", "Delhi", "Mumbai", "Patna")
print("\nTuple of cities:", cities)
print("Second city:", cities[1])
print("="*30)

# 4. Set of 5 course names, add one new course

courses = {"Python", "Java", "C++", "DBMS", "Web Development"}
print("\nSet of courses:", courses)
courses.add("Machine Learning")
print("Updated set after adding new course:", courses)
print("="*30)

# 5. Dictionary for one student with name, branch, batch, and marks

student_info = {
    "name": "Aashutosh",
    "branch": "Computer Science",
    "batch": "batch-b",
    "marks": 88.5
}
print(student_info)

print("="*30)

# 6. Print the student dictionary in a readable format
print("\nStudent Details:")
for key, value in student_info.items():
    print(f"{key.capitalize()}: {value}")
