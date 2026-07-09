
# Question 1: List Append
# =========================

students = ["Aman", "Priya", "Shalu", "Raj", "Ansh"]
students.append("Vivek")
print(students)

# =========================
# Question 2: Tuple Indexing
# =========================

cities = ("Mumbai", "Lucknow", "Delhi", "Kanpur", "Pune")
print(cities[2])

# =========================
# Question 3: Set Add
# =========================

courses = {"Python", "SQL", "Machine Learning", "Data Analytics"}
courses.add("AI")
print(sorted(courses))

# =========================
# Question 4: Dictionary Access
# =========================

student = {
    "name": "Rahul",
    "course": "Python Data AI",
    "batch": "Batch A",
    "city": "Gorakhpur"
}

print("Name:", student["name"])
print("Course:", student["course"])

# =========================
# Question 5: Filter Even Numbers
# =========================

numbers = list(range(1, 11))
even_numbers = [num for num in numbers if num % 2 == 0]
print(even_numbers)

# =========================
# Question 6: Count Word Frequency
# =========================

words = ["python", "ai", "python", "data", "ai", "python"]

word_count = {}

for word in words:
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1

print(word_count)

# =========================
# Question 7: Nested Student Dictionary
# =========================

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

# =========================
# Question 8: Common Elements
# =========================

python_students = {"Aman", "Priya", "Raj", "Neha"}
ai_students = {"Raj", "Neha", "Vivek", "Shalu"}

common_students = sorted(python_students.intersection(ai_students))
print(common_students)