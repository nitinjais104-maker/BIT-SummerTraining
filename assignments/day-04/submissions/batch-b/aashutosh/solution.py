#-----------------------------------------------------------------
# Question 1: List Append
# ---------------------------------------------------------------------
students = ['Aman', 'Priya', 'Shalu', 'Raj', 'Ansh']
students.append('Vivek')
print(students)
print("="*30)

# ---------------------------------------------------------------------
# Question 2: Tuple Indexing
# ---------------------------------------------------------------------
cities = ('Mumbai', 'Kolkata', 'Delhi', 'Chennai', 'Pune')
print(cities[2])
print("="*30)

# ---------------------------------------------------------------------
# Question 3: Set Add
# ---------------------------------------------------------------------
courses = {"Python", "SQL", "Machine Learning", "Data Analytics"}
courses.add("AI")
print(sorted(courses))
print("="*30)

# ---------------------------------------------------------------------
# Question 4: Dictionary Access
# ---------------------------------------------------------------------
student = {
    "name": "Rahul",
    "course": "Python Data AI",
    "batch": "batch-a",
    "city": "Gorakhpur"
}
print("Name:", student["name"])
print("Course:", student["course"])
print("="*30)

# ---------------------------------------------------------------------
# Question 5: Filter Even Numbers
# ---------------------------------------------------------------------
numbers = list(range(1, 11))
even_numbers = [n for n in numbers if n % 2 == 0]
print(even_numbers)
print("="*30)

# ---------------------------------------------------------------------
# Question 6: Count Word Frequency
# ---------------------------------------------------------------------
words = ["python", "ai", "python", "data", "ai", "python"]
word_count = {}
for word in words:
    word_count[word] = word_count.get(word, 0) + 1
print(word_count)
print("="*30)

# ---------------------------------------------------------------------
# Question 7: Nested Student Dictionary
# ---------------------------------------------------------------------
neha = {
    "name": "Neha",
    "marks": {"python": 85, "data": 90},
    "skills": ["Python", "SQL"]
}
neha["skills"].append("Pandas")
print(neha)
print("="*30)

# ---------------------------------------------------------------------
# Question 8: Common Elements
# ---------------------------------------------------------------------
python_students = {"Aman", "Priya", "Raj", "Neha"}
ai_students = {"Raj", "Neha", "Vivek", "Shalu"}
common_students = sorted(python_students & ai_students)
print(common_students)