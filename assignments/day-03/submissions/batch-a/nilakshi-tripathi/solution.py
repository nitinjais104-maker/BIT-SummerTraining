# 1. Create a list of 5 student names and print all names.
student=["Nilaskhi","Khushi","Mili","Shipra","Preeti",]

for names in student:
    print(names)


# 2. Add one new student name to the list.

student=["Nilaskhi","Khushi","Mili","Shipra","Preeti",]

student.append("seeta")
print(student)

# 3. Create a tuple of 5 city names and print the second city.

city=("Grakhpur","Basti","Mumbai","Kolkata","Lucknow",)
print(city[1])


# 4. Create a set of 5 course names and add one new course.

course={"Btech","BCA","MBA","Mtech","MCA"}

course.add("B.com")

print(course)


# 5. Create a dictionary for one student with name, branch, batch, and marks.

Student={
    "name":"Nilakshi",
    "branch":"CSE",
    "batch":"2024-28",
    "marks":90
}

print(Student)

# 6. Print the student dictionary in a readable format

student={
     "name":"Nilakshi",
    "branch":"CSE",
    "batch":"2024-28",
    "marks":90
}
print("students detail")
print("name :",student["name"])
print("branch :",student["branch"])
print("batch :",student["batch"])
print("marks:",student["marks"])