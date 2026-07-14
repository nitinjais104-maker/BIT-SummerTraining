# Question 1
students = ["Aman", "Priya", "Shalu", "Raj", "Ansh"]

print("Student Names:")
for student in students:
    print(student)

# Question 2
students.append("Nitin")

print("\nUpdated Student List:")
for student in students:
    print(student)

# Question 3
cities = ("Gorakhpur", "Lucknow", "Deoria", "Varanasi", "Delhi")

print("\nSecond City:")
print(cities[1])

# Question 4
courses = {"Python", "Java", "Data Analytics", "AI", "Machine Learning"}

courses.add("Cloud Computing")

print("\nCourses:")
print(courses)

# Question 5
student = {
    "Name": "Nitin Jaiswal",
    "Branch": "CSE",
    "Batch": "2024-2028",
    "Marks": 85
}

# Question 6
print("\nStudent Details:")
for key, value in student.items():
    print(f"{key}: {value}")