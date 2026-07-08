## Day 3 Assignment

## Topic: Python Data Structures

## Question.1
# Print("Create a list of 5 student names and print all names.")
student = ["Ritu","Ankita","Anjali","Anmol","Atul"] # List of 5 student names

for student in student:
    print(student) # Print all names

    ## Question.2
    # Print("Add one new student name to the list.")
students = ["Ritu","Ankita","Anjali","Anmol","Atul"] # List of student names
students.append("Laxmi") # Add a new student
print(students) #Print updated list    

## Question.3
# Print("Create a tuple of 5 city names and print the second city.")
cities = ("Gorkhpur","Salempur","Deoria","Lar","Mau") # Create a tuple of 5 city names
print(cities[1]) # Print the second city

## Question.4
# Print("Create a set of 5 coures names and add one new course.")
course ={"HTML","C","C++","Java","SQL"} # Create a set of 5 course names
course.add("Python") # Use add() to Add a new course
print(course) # Print the  updated set

## Question.5
# Print("Create a dictionary for one student with name,branch, batch,and marks.")
student = {
    "name": "Ritu",
    "branch": "Master Of Computer Applications",
    "batch": "2025",
    "marks": 80
}
print(student) # print the dictionary for one student

## Question.6
# Print("Print the student dictionary in a readable format")
student = { # student dictionary
    "name": "Ritu",
    "branch": "Master Of Computer Applications",
    "batch": "2025",
    "marks": 80
}
print("Name:", student["name"]) # print in readable format
print("Branch:", student["branch"])
print("Batch:", student["batch"])
print("Marks:",student["marks"])
    
