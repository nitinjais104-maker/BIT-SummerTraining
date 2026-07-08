students = ["Aman", "Priya", "Shalu", "Raj", "Ansh"]
students.append("Vivek")
print(students)

cities = ("Mumbai", "Chennai", "Delhi", "Kolkata", "Jaipur")
print(cities[2])

courses = {"Python", "SQL", "Machine Learning", "Data Analytics"}
courses.add("AI")
print(sorted(courses))

student = {"name": "Rahul", "course": "Python Data AI", "batch": "B", "city": "Delhi"}
print("Name:", student["name"])
print("Course:", student["course"])

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even = [n for n in numbers if n % 2 == 0]
print(even)

words = ["python", "ai", "python", "data", "ai", "python"]
freq = {}
for word in words:
    freq[word] = freq.get(word, 0) + 1
print(freq)

student2 = {"name": "Neha", "marks": {"python": 85, "data": 90}, "skills": ["Python", "SQL"]}
student2["skills"].append("Pandas")
print(student2)

python_students = {"Aman", "Priya", "Raj", "Neha"}
ai_students = {"Raj", "Neha", "Vivek", "Shalu"}
common = python_students & ai_students
print(sorted(common))