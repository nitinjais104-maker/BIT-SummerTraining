# # ### Question 1: List Append

# # Create a list of 5 student names. Add one new student name to the list and print the final list.

# # ```python
# # # Expected Output:
# # # ['Aman', 'Priya', 'Shalu', 'Raj', 'Ansh', 'Vivek']
student_name = ['Aman','Priya','Shalu','Raj','Ansh']
student_name.append('Vivek')
print(student_name)

# ### Question 2: Tuple Indexing

# Create a tuple of 5 city names and print the third city.

# ```python
# # Expected Output:
# # Delhi

city = ("gorakhpur","vishakhapatnam","maharajganj","Delhi","mumbai")
print(city[3])

### Question 3: Set Add

# Create a set of 4 course names. Add `"AI"` to the set and print the sorted list of courses.

# ```python
# # Expected Output:
# # ['AI', 'Data Analytics', 'Machine Learning', 'Python', 'SQL']
course = {'Data Analytics','Machine Learning','Python','SQL'}
course.add('AI')
sor =sorted(course)
print(sor)



## Question 4: Dictionary Access

# Create a dictionary with keys `name`, `course`, `batch`, and `city`. Print the student's name and course.

# ```python
# # Expected Output:
# # Name: Rahul
# # Course: Python Data AI
student = {
    "name": "Rahul",
    "course": "Python Data AI",
    "batch": "B1",
    "city": "Lucknow"
}

print("Name:", student["name"])
print("Course:", student["course"])


### Question 5: Filter Even Numbers

# Create a list of numbers from 1 to 10. Create a new list that contains only even numbers and print it.

# ```python
# Expected Output:
# [2, 4, 6, 8, 10]


numbers = list(range(1, 11))

even_numbers = []

for num in numbers:
    if num % 2 == 0:
        even_numbers.append(num)

print(even_numbers)


### Question 6: Count Word Frequency

# Create a list of words:

# ```python
# words = ["python", "ai", "python", "data", "ai", "python"]
# ```

# Use a dictionary to count how many times each word appears and print the dictionary.

# ```python
# # Expected Output:
# # {'python': 3, 'ai': 2, 'data': 1}
# Create a list of words
words = ["python", "ai", "python", "data", "ai", "python"]
frequency = {}
for word in words:
    if word in frequency:
        frequency[word] += 1
    else:
        frequency[word] = 1
print(frequency)


### Question 7: Nested Student Dictionary

# Create a nested dictionary for one student with name, marks, and skills. Add one new skill `"Pandas"` and print the updated dictionary.

# ```python
# # Expected Output:
# # {'name': 'Neha', 'marks': {'python': 85, 'data': 90}, 'skills': ['Python', 'SQL', 'Pandas']
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



## Question 8: Common Elements

# Create two sets:

# ```python
# python_students = {"Aman", "Priya", "Raj", "Neha"}
# ai_students = {"Raj", "Neha", "Vivek", "Shalu"}
# ```

# Find the common students and print them as a sorted list.

# ```python
# # Expected Output:
# # ['Neha', 'Raj']


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
