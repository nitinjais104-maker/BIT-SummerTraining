# Day 3 Assignment
#===========================================================>>>
#Q.1. Create a list of 5 student names and print all names.
student_names = ["Saniya", "Amit", "Shalu", "Ansh", "Aman"]
print(student_names)                                                        # Printing the list of student names
print("="*50)
#==========================================================>>>
#Q.2. Add one new student name to the list.
student_names = ["Saniya", "Amit", "Shalu", "Ansh", "Aman"]
new_student = "Riya"
student_names.append(new_student)
print(student_names)                                                        # Adding a new student name to the list
print("="*50)
#==========================================================>>>
#Q.3. Create a tuple of 5 city names and print the second city.
cities = ("Gorakhpur", "Maharajganj", "Lucknow", "Siddharthnagar", "Deoria")
print(cities[1])                                                           # Printing the second city from the tuple
print("="*50)
#=========================================================>>>
#Q.4. Create a set of 5 course names and add one new course.
courses = {"Data Science", "Machine Learning", "Python", "Deep Learning", "AI"}
new_course = "Data Analytics"
courses.add(new_course)
print(courses)                                                             # Adding a new course to the set
print("="*50)
#========================================================>>>
#Q.5. Create a dictionary for one student with name, branch, batch, and marks.
student_info = {
    "name": "Saniya",
    "branch": "Data Science",
    "batch": "A",
    "marks": 85
}
print(student_info)                                                        # Printing the dictionary for one student
print("="*50)
#=======================================================>>>
#Q.6. Print the student dictionary in a readable format.
student_info = {
    "name": "Saniya",
    "branch": "Data Science",
    "batch": "A",
    "marks": 85
}
print("Student Name:", student_info["name"])
print("Branch:", student_info["branch"])
print("Batch:", student_info["batch"])
print("Marks:", student_info["marks"])                                      # Printing the student dictionary in a readable format
print("="*50)
#=======================================================>>>
