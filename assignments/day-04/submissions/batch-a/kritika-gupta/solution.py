## Question 1: List Append

#Create a list of 5 student names. Add one new student name to the list and print the final list.


students = ["Aman", "Priya", "Shalu", "Raj", "Ansh"]
students.append("Vivek")
print(students)

## Question 2: Tuple Indexing

#Create a tuple of 5 city names and print the third city.


cities = ("Mumbai", "Kolkata", "Delhi", "Chennai", "Jaipur")
print(cities[2])

## Question 3: Set Add

#Create a set of 4 course names. Add `"AI"` to the set and print the sorted list of courses.


courses = {"Python", "SQL", "Machine Learning", "Data Analytics"}
courses.add("AI")
print(sorted(courses))

## Question 4: Dictionary Access

#Create a dictionary with keys `name`, `course`, `batch`, and `city`. Print the student's name and course.


student_info = {
"name": "Rahul",
"course": "Python Data AI ",
"batch": "Batch-A",
"city": "Gorakhpur"
}

print("Name:", student_info["name"])
print("Course:", student_info["course"])

##Question 5: Filter Even Numbers

#Create a list of numbers from 1 to 10. Create a new list that contains only even numbers and print it.


numbers = list(range(1, 11))
even_numbers = [num for num in numbers if num % 2 == 0]

print(even_numbers)

## Question 6: Count Word Frequency

#Create a list of words:


words = ["python", "ai", "python", "data", "ai", "python"]

word_count = {}

for word in words:
 word_count[word] = word_count.get(word, 0) + 1

print( word_count)

## Question 7: Nested Student Dictionary

#Create a nested dictionary for one student with name, marks, and skills. Add one new skill `"Pandas"` and print the updated dictionary.


student = {
"name": "Neha",
"marks": {
"python": 85,
"data": 90
},
"skills": ["Python", "SQL"]
}

student["skills"].append("Pandas")

print("Q7:", student)

## Question 8: Common Elements

#Create two sets:

#```python
#python_students = {"Aman", "Priya", "Raj", "Neha"}
#ai_students = {"Raj", "Neha", "Vivek", "Shalu"}


##Find the common students and print them as a sorted list.



python_students = {"Aman", "Priya", "Raj", "Neha"}
ai_students = {"Raj", "Neha", "Vivek", "Shalu"}

common_students = []

# Check each Python student
for student in python_students:
    if student in ai_students:
        common_students.append(student)

# Sort the list alphabetically
common_students.sort()

print(common_students)




