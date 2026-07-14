# # Questions

# 1. Create a list of 5 student names and print all names.
students = ["Satyam", "Manu", "Sudha", "Neetu", "Pooja"]

print("Student Names:")
for student in students:
    print(student)
# 2. Add one new student name to the list.
students.append("Manu")

print("\nUpdated Student List:")
print(students)
# 3. Create a tuple of 5 city names and print the second city.
cities = ("Hyderabad", "Lucknow", "Mumbai", "Banglor", "Jaipur")

print("\nSecond City:")
print(cities[1])

# 4. Create a set of 5 course names and add one new course.
courses = {"Python", "Java", "Maths", "AI", "ML"}

courses.add("Data Science")

print("\nUpdated Course Set:")
print(courses)
# 5. Create a dictionary for one student with name, branch, batch, and marks.
student = {
    "name": "Manu",
    "branch": "MCA",
    "batch": "2026",
    "marks": 92
}
# 6. Print the student dictionary in a readable format.
print("\nStudent Details:")
print("Name   :", student["name"])
print("Branch :", student["branch"])
print("Batch  :", student["batch"])
print("Marks  :", student["marks"])