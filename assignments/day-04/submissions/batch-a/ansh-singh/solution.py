# question 1
student_name = ["Vivek Singh","Aman Singh","Ansh Singh","Sadanand","Raj Singh"]
student_name.append("Ayush Vishwakarma")
print(student_name)
 
#question 2
city_name = ("Gorakhpur","Kushinagar","Delhi","Mumbai","Lucknow")
print(city_name[2])

#question 3
course_name = {"Python","C","C++","Java"}
course_name.add("AI")
print(sorted(course_name))

#question 4
student_info ={
    "name" : "Vivek Singh",
    "course" : "CSE(AIML)",
    "batch" : "A",
    "city" : "Kushinagar"
}
print("Name :", student_info["name"])
print("Course :", student_info["course"])

#question 5
numbers = list(range(1, 11))
even_numbers = []

for num in numbers:
    if num % 2 == 0:
        even_numbers.append(num)

print(even_numbers)

#question 6
words = ["python", "ai", "python", "data", "ai", "python"]

count = {}

for word in words:
    if word in count:
        count[word] += 1
    else:
        count[word] = 1

print(count)

#question 7
student_info = {
    "name": "Neha",
    "marks": {"python": 85, "data": 90},
    "skills": ["Python", "SQL"]
}

student_info["skills"].append("Pandas")
print(student_info)

#question 8
python_students = {"Aman", "Priya", "Raj", "Neha"}
ai_students = {"Raj", "Neha", "Vivek", "Shalu"}

common_students = sorted(python_students & ai_students)
print(common_students)