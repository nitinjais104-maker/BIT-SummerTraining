# Question 1: List Append
students = ["Aman", "Priya", "Shalu", "Raj", "Anshu"]
students.append("Neha")
print("Q1:", students)

# Question 2: Tuple Indexing
cities = ("Lucknow", "Mumbai", "Delhi", "Kolkata", "Chennai")
print("Q2:", cities[2])

# Question 3: Set Add
courses = {"Python", "Data Analytics", "Machine Learning", "SQL"}
courses.add("AI")
print("Q3:", sorted(courses))

# Question 4: Dictionary Access
student = {
    "name": "Rahul",
    "course": "Python Data AI",
    "batch": "B",
    "city": "Lucknow"
}
print("Q4:")
print("Name:", student["name"])
print("Course:", student["course"])

# Question 5: Filter Even Numbers
numbers = list(range(1, 11))
even_numbers = [num for num in numbers if num % 2 == 0]
print("Q5:", even_numbers)

# Question 6: Count Word Frequency
words = ["python", "ai", "python", "data", "ai", "python"]
freq = {}

for word in words:
    freq[word] = freq.get(word, 0) + 1

print("Q6:", freq)

# Question 7: Nested Student Dictionary
student = {
    "name": "Neha",
    "marks": {
        "python": 85,
        "ai": 90
    },
    "skills": ["Python", "SQL"]
}

student["skills"].append("Pandas")
print("Q7:", student)

# Question 8: Common Elements
python_students = {"Aman", "Priya", "Raj", "Neha"}
ai_students = {"Raj", "Neha", "Vivek", "Rohan"}

common_students = sorted(list(python_students & ai_students))
print("Q8:", common_students)