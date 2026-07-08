# Question 1: Create a list of 5 student names and print all names

students = ["Rishabh", "Aman", "Rahul", "Priya", "Ankit"]

print("Student Names:")
for student in students:
    print(student)

# Question 2: Add one new student name to the list

students.append("Shivam")

print("\nUpdated Student List:")
print(students)

# Question 3: Create a tuple of 5 city names and print the second city

cities = ("Lucknow", "Kanpur", "Varanasi", "Prayagraj", "Noida")

print("\nSecond City:")
print(cities[1])

# Question 4: Create a set of 5 course names and add one new course

courses = {"Python", "Java", "C", "C++", "Machine Learning"}

courses.add("Data Science")

print("\nCourses:")
print(courses)

# Question 5: Create a dictionary for one student

student = {
    "name": "Rishabh Bhaskar Shahi",
    "branch": "Computer Science",
    "batch": "Batch A",
    "marks": 85.5
}

# Question 6: Print the student dictionary in a readable format

print("\nStudent Details:")
for key, value in student.items():
    print(f"{key}: {value}")