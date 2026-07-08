# Question 1: List Append
students = ["Aman", "Priya", "Shalu", "Raj", "Ansh"]
students.append("Vivek")
print(students)


# Question 2: Tuple Indexing
cities = ("Lucknow", "Mumbai", "Delhi", "Jaipur", "Pune")
print(cities[2])


# Question 3: Set Add
courses = {"Python", "SQL", "Machine Learning", "Data Analytics"}
courses.add("AI")
print(sorted(courses))


# Question 4: Dictionary Access
student = {
    "name": "Rahul",
    "course": "Python Data AI",
    "batch": "B",
    "city": "Lucknow"
}

print("Name:", student["name"])
print("Course:", student["course"])


# Question 5: Filter Even Numbers
numbers = list(range(1, 11))
even_numbers = []

for num in numbers:
    if num % 2 == 0:
        even_numbers.append(num)

print(even_numbers)


# Question 6: Count Word Frequency
words = ["python", "ai", "python", "data", "ai", "python"]

count = {}

for word in words:
    if word in count:
        count[word] += 1
    else:
        count[word] = 1

print(count)


# Question 7: Nested Student Dictionary
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


# Question 8: Common Elements
python_students = {"Aman", "Priya", "Raj", "Neha"}
ai_students = {"Raj", "Neha", "Vivek", "Shalu"}

common = sorted(python_students.intersection(ai_students))
print(common)