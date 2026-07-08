# Day 4 Assignment - Python Data Structures

# Question 1: List Append
students = ['Aman', 'Priya', 'Shalu', 'Raj', 'Ansh']
students.append('Vivek')
print(students)

# Question 2: Tuple Indexing
cities = ('Mumbai', 'Lucknow', 'Delhi', 'Pune', 'Jaipur')
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
    "city": "Varanasi"
}
print(f"Name: {student['name']}")
print(f"Course: {student['course']}")

# Question 5: Filter Even Numbers
numbers = list(range(1, 11))
even_numbers = [n for n in numbers if n % 2 == 0]
print(even_numbers)

# Question 6: Count Word Frequency
words = ["python", "ai", "python", "data", "ai", "python"]
word_count = {}
for word in words:
    word_count[word] = word_count.get(word, 0) + 1
print(word_count)

# Question 7: Nested Student Dictionary
student_info = {
    "name": "Neha",
    "marks": {"python": 85, "data": 90},
    "skills": ["Python", "SQL"]
}
student_info["skills"].append("Pandas")
print(student_info)

# Question 8: Common Elements
python_students = {"Aman", "Priya", "Raj", "Neha"}
ai_students = {"Raj", "Neha", "Vivek", "Shalu"}
common = python_students & ai_students
print(sorted(common))