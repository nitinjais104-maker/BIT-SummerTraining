# 1. list of 5 student names
list = ["Malya", "Kirti", "Deependra", "Yashi", "Aryan"]
for i in list:
    print("students name==",i,end=",")


# 2. Add one new student name to the list
list.append("Kuldeep")
print("\nUpdated Student List:", list)


# 3.  tuple of 5 city names 
cities = ("Delhi", "Mumbai", "Kanpur", "Kolkata", "Chennai")
print("\nSecond City:", cities[1])


# 4. set of 5 course names and adding a new course
courses = {"Python", "Java", "C", "C++", "JavaScript"}
print("courses=",courses)
courses.add("Data Science")
print("\nupdated_Courses:", courses)


# 5. Create a dictionary for one student
student = {
    "name": "Malya",
    "branch": "AIML",
    "batch": "A",
    "marks": 85
}

# 6. Print the student dictionary in a readable format
print("\nStudent Details:")
print("Name  :", student["name"])
print("Branch:", student["branch"])
print("Batch :", student["batch"])
print("Marks :", student["marks"])