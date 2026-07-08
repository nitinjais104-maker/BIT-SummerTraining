#day04 solution
#1: List Append
#Expected Output:['Aman', 'Priya', 'Shalu', 'Raj', 'Ansh', 'Vivek']
list=["Aman", "Priya", "Shalu", "Raj", "Ansh"]
list.append("vivek")
print("updated list-->",list)


#2: Tuple Indexing
# Expected Output:Delhi
tuple=("Kanpur","Banaras","Delhi","Mumbai","Agra")
print(tuple[2])


#3: Set Add
#Expected Output:['AI', 'Data Analytics', 'Machine Learning', 'Python', 'SQL']
courses={"AI","Data Analytics","Machine Learning","Python"}
courses.add("SQL")
print(sorted(courses))


#4: Dictionary Access
# Expected Output: Name: Rahul
#                  Course: Python Data AI
student = {
    "name": "Rahul",
    "course": "Python Data AI",
    "batch": "Batch 1",
    "city": "Lucknow"
}
print("Name:", student["name"])
print("Course:", student["course"])


#5: Filter Even Numbers
# Expected Output:[2, 4, 6, 8, 10]
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers = []
for num in numbers:
    if num % 2 == 0:
        even_numbers.append(num)
print(even_numbers)


#6: Count Word Frequency
# Expected Output:{'python': 3, 'ai': 2, 'data': 1}
words = ["python", "ai", "python", "data", "ai", "python"]
word_count = {}
for word in words:
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1
print(word_count)

#7: Nested Student Dictionary
# Expected Output:{'name': 'Neha', 'marks': {'python': 85, 'data': 90}, 'skills': ['Python', 'SQL', 'Pandas']}
student = {
    "name": "Neha",
    "marks": {
        "python": 85,
        "data": 90},
    "skills": ["Python", "SQL"]
}
student["skills"].append("Pandas")
print(student)


#8: Common Elements
# Expected Output:['Neha', 'Raj']
python_students = {"Aman", "Priya", "Raj", "Neha"}
ai_students = {"Raj", "Neha", "Vivek", "Shalu"}
common_students = sorted(python_students & ai_students)
print(common_students) 