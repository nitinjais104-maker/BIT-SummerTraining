#  1.Create a list of 5 student names.
#  Add one new student name to the list and print the final list.
# Expected Output:
# ['Aman', 'Priya', 'Shalu', 'Raj', 'Ansh', 'Vivek']

students = ["Aman", "Priya", "Shalu", "Raj", "Ansh"]
students.append("Vivek")
print(students)

# 2.Create a tuple of 5 city names and print the third city.

# Expected Output:
# Delhi
cities = ("Mumbai", "Kolkata", "Delhi", "Chennai", "Bengaluru")
print(cities[2])

# 3.Create a set of 4 course names. Add "AI" to the set and print the sorted list of courses.

# Expected Output:
# ['AI', 'Data Analytics', 'Machine Learning', 'Python', 'SQL']
courses = {"Python", "SQL", "Machine Learning", "Data Analytics"}
courses.add("AI")
print(sorted(courses))

# 4.Create a dictionary with keys name, course, batch, and city. Print the student's name and course.

# Expected Output:
# Name: Rahul
# Course: Python Data AI
student = {
    "name": "Rahul",
    "course": "Python Data AI",
    "batch": "BIT-2025",
    "city": "Gorakhpur"
}

print("Name:",student["name"])
print("Course:",student["course"])

# 5.Create a list of numbers from 1 to 10. Create a new list that contains only even numbers and print it.

# Expected Output:
# [2, 4, 6, 8, 10]

numbers = list(range(1, 11))

even_numbers = []

for num in numbers:
    if num % 2 == 0:
        even_numbers.append(num)

print(even_numbers)

# 6.Create a list of words:

# = ["python", "ai", "python", "data", "ai", "python"]
# Use a dictionary to count how many times each word appears and print the dictionary.

# Expected Output:
# {'python': 3, 'ai': 2, 'data': 1}
words = ["python", "ai", "python", "data", "ai", "python"]

frequency = {}

for word in words:
    if word in frequency:
        frequency[word] += 1
    else:
        frequency[word] = 1

print(frequency)

# 7.Create a nested dictionary for one student with name, marks, and skills. Add one new skill "Pandas" and print the updated dictionary.

# Expected Output:
# {'name': 'Neha', 'marks': {'python': 85, 'data': 90}, 'skills': ['Python', 'SQL', 'Pandas']}
student = {
    "name": "Neha",
    "marks": {
        "python": 85,
        "data": 90
    },
    "skills": ["Python", "SQL"]
}

student["skills"].append("Pandas")

print(student)


# 8.Create two sets:
# python_students = {"Aman", "Priya", "Raj", "Neha"}
# ai_students = {"Raj", "Neha", "Vivek", "Shalu"}
# Find the common students and print them as a sorted list.
# Expected Output:
# ['Neha', 'Raj']
python_students = {"Aman", "Priya", "Raj", "Neha"}
ai_students = {"Raj", "Neha", "Vivek", "Shalu"}

common_students = sorted(python_students.intersection(ai_students))

print(common_students)