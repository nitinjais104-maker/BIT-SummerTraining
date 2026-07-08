#assignment_3

#Question 1
#Create a list of 5 student names and print all names.
student_names = ["soni", "muskan", "kajal", "radhika","sanjana"]
for name in student_names:
    print(name)


#Question 2
#Add one new student name to the list.
student_names = ["muskan", "kajal", "radhika","sanjana"]
student_names.append("soni")
print(student_names)


#Question 3
#Create a tuple of 5 city names and print the second city.
cities = ("Delhi", "Mumbai", "Kolkata", "Chennai", "Bengaluru")
print("Second city:", cities[1])


#Question 4
#Create a set of 5 course names and add one new course.
courses = {"BA", "BBA", "BCA", "B.Tech", "B.sc"}
courses.add("MBBS")
print("Courses:", courses)

#Question 5
#Create a dictionary for one student with name, branch, batch, and marks.
student = {
    "name": "Soni Sahani",
    "branch": "ECE",
    "batch": "A",
    "marks": 83
}

#Question 6
#Print the student dictionary in a readable format.
student = {
    "name": "Soni Sahani",
    "branch": "ECE",
    "batch": "A",
    "marks": 83
}
print("student Detaile")
for key, value in student.items():
    print(f"{key}:{value}")
