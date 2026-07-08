# # Question 1: List Append (Create a list of 5 student names. Add one new student name to the list and print the final list.)
# Expected Output: ['Aman', 'Priya', 'Shalu', 'Raj', 'Ansh', 'Vivek']

a_list = ["Aman", "Priya", "Shalu", "Raj","Ansh"]
a_list.append("Vivek")
print(a_list)



# ### Question 2: Tuple Indexing  (Create a tuple of 5 city names and print the third city.)
# # Expected Output: Delhi

city = ("Gorakhpur", "Lucknow","Delhi","Hydrabad","Vishakha Pattnam")
print(city[2])


# ### Question 3: Set Add  (Create a set of 4 course names. Add `"AI"` to the set and print the sorted list of courses.)
# # Expected Output: ['AI', 'Data Analytics', 'Machine Learning', 'Python', 'SQL']

course_set = {"Data Analytics", "Machine Learning", "Python", "SQL"}
course_set.add("AI")
course = sorted(course_set)
print(course)


# ### Question 4: Dictionary Access (Create a dictionary with keys `name`, `course`, `batch`, and `city`. Print the student's name and course.)
# # Expected Output:
# # Name: Rahul
# # Course: Python Data AI

student_dic = {
    "Name":"Rahul",
    "Course": "Python Data AI",
    "Batch": "A",
    "City": "Gorakhpur"
}
for key,value in student_dic.items():
    print(f"{key}:{value}")


# ### Question 5: Filter Even Numbers  (Create a list of numbers from 1 to 10. Create a new list that contains only even numbers and print it.)
# # Expected Output: [2, 4, 6, 8, 10]

nums = [1,2,3,4,5,6,7,8,9,10]
even_list = []
for num in nums:
    if num %2==0:
        even_list.append(num)
print(even_list)
    

# ### Question 6: Count Word Frequency  (Create a list of words:)
# words = ["python", "ai", "python", "data", "ai", "python"]

words = ["python", "ai", "python", "data", "ai", "python"]
freq = {} # Hash map function using in this
for word in words:
    if word in freq:
        freq[word] +=1
    else:
        freq[word] =1

for key, value in freq.items():
    print(f"{key} : {value}")



# Question 7: Nested Student Dictionary  (Create a nested dictionary for one student with name, marks, and skills. Add one new skill `"Pandas"` and print the updated dictionary. )
# # Expected Output: {'name': 'Neha', 'marks': {'python': 85, 'data': 90}, 'skills': ['Python', 'SQL', 'Pandas']}

student_dic = {
    "name" : "Neha",
    "marks":{
        "python" : 85,
        "data" : 90
    },
    "skills": ["Python" , "SQL"]
}
student_dic["skills"].append("Pandas")
print(student_dic)


# Question 8: Common Elements  (Create two sets:)
# python_students = {"Aman", "Priya", "Raj", "Neha"}
# ai_students = {"Raj", "Neha", "Vivek", "Shalu"}
# Find the common students and print them as a sorted list.

python_students = {"Aman", "Priya", "Raj", "Neha"}
ai_students = {"Raj", "Neha", "Vivek", "Shalu"}
               
common_student = []
for student in python_students :
    if student in ai_students:
        common_student.append(student)

common_student.sort()
print(common_student)