
### Question 1: List Append

#Create a list of 5 student names. Add one new student name to the list and print the final list.


students_name = ["Aman","Priya","Shalu","Raj","Ansh"]
students_name.append("Vivek")
print(students_name)



### Question 2: Tuple Indexing

#Create a tuple of 5 city names and print the third city.

city_names = ("Gorakhpur","Azamgarh","Delhi","Lucknow","Varanasi")
print(city_names[2])



### Question 3: Set Add

#Create a set of 4 course names. Add `"AI"` to the set and print the sorted list of courses.

courses = { "Data Analytics", "Machine Learning", "Python", "SQL"}
courses.add("AI")
print(sorted(courses))


### Question 4: Dictionary Access

#Create a dictionary with keys `name`, `course`, `batch`, and `city`. Print the student's name and course.
student = {"name":"Rahul",
           "course":"Python Data AI",
           "batch":"A",
           "city":"Gorakhpur"
           }
print("Name:",student["name"])
print("Course:",student["course"])



### Question 5: Filter Even Numbers

#Create a list of numbers from 1 to 10. Create a new list that contains only even numbers and print it.
numbers = [1,2,3,4,5,6,7,8,9,10]
even_numbers = []
for num in numbers:
    if num % 2 == 0:
        even_numbers.append(num)
    else:
        continue
print(even_numbers)


### Question 6: Count Word Frequency

# Create a list of words:
# words = ["python", "ai", "python", "data", "ai", "python"]
# Use a dictionary to count how many times each word appears and print the dictionary.

words = ["python", "ai", "python", "data", "ai", "python"]

count_word = {}
for word in words:
    if word in count_word:
        count_word[word] += 1 
    else:
        count_word[word] = 1

print(count_word)


### Question 7: Nested Student Dictionary

#Create a nested dictionary for one student with name, marks, and skills. Add one new skill `"Pandas"` and print the updated dictionary.
student = {
    "name":"Neha",
    "marks":{"python": 85,"data":90},
    "skills":["Python","SQL"]
    }
student["skills"].append("Pandas")
print(student)



### Question 8: Common Elements
# Create two sets:
# python_students = {"Aman", "Priya", "Raj", "Neha"}
# ai_students = {"Raj", "Neha", "Vivek", "Shalu"}

# Find the common students and print them as a sorted list.

python_students = {"Aman", "Priya", "Raj", "Neha"}
ai_students = {"Raj", "Neha", "Vivek", "Shalu"}
common_student = python_students.intersection (ai_students)
common_student = sorted(common_student)
print(common_student)