# Day 4 Assignment - Python Data Structures
# Student: Rohan Nishad
# Batch: B

print("=" * 50)
print("BASIC QUESTIONS")
print("=" * 50)

# Question 1: List Append
print("\nQuestion 1: List Append")
students = ['Aman', 'Priya', 'Shalu', 'Raj', 'Ansh']
students.append('Vivek')
print(students)

# Question 2: Tuple Indexing
print("\nQuestion 2: Tuple Indexing")
cities = ('Mumbai', 'Bangalore', 'Delhi', 'Hyderabad', 'Chennai')
print(cities[2])

# Question 3: Set Add
print("\nQuestion 3: Set Add")
courses = {'Python', 'SQL', 'Machine Learning', 'Data Analytics'}
courses.add('AI')
courses_sorted = sorted(list(courses))
print(courses_sorted)

# Question 4: Dictionary Access
print("\nQuestion 4: Dictionary Access")
student_info = {
    'name': 'Rahul',
    'course': 'Python Data AI',
    'batch': 'B',
    'city': 'Patna'
}
print(f"Name: {student_info['name']}")
print(f"Course: {student_info['course']}")

print("\n" + "=" * 50)
print("MEDIUM QUESTIONS")
print("=" * 50)

# Question 5: Filter Even Numbers
print("\nQuestion 5: Filter Even Numbers")
numbers = list(range(1, 11))
even_numbers = [num for num in numbers if num % 2 == 0]
print(even_numbers)

# Question 6: Count Word Frequency
print("\nQuestion 6: Count Word Frequency")
words = ["python", "ai", "python", "data", "ai", "python"]
word_count = {}
for word in words:
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1
print(word_count)

# Question 7: Nested Student Dictionary
print("\nQuestion 7: Nested Student Dictionary")
student_nested = {
    'name': 'Neha',
    'marks': {'python': 85, 'data': 90},
    'skills': ['Python', 'SQL']
}
student_nested['skills'].append('Pandas')
print(student_nested)

# Question 8: Common Elements
print("\nQuestion 8: Common Elements")
python_students = {"Aman", "Priya", "Raj", "Neha"}
ai_students = {"Raj", "Neha", "Vivek", "Shalu"}
common_students = sorted(list(python_students & ai_students))
print(common_students)
