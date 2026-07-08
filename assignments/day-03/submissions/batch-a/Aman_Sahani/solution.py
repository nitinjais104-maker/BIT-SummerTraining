
# 1. Create a list of 5 student names and print all names.

bacche = ["Arjun","Bheem","Nakul","Sahadev","Yudhistir"]
print(bacche)

# 2. Add one new student name to the list.
bacche = ["Arjun","Bheem","Nakul","Sahadev","Yudhistir"]
bacche.append("Karna")
print(bacche)


# 3. Create a tuple of 5 city names and print the second city.
city = ("Gorakhpur","Basti","Ayidhya","Lucknow","Goa")
print(city[1])

# 4. Create a set of 5 course names and add one new course.

course = {"B.Tech", "MBA", "BCA", "BBA", "MCA"}
course.add("BA")
print(course)

# 5. Create a dictionary for one student with name, branch, batch, and marks.
student = {
    "Name" : "pappu",
    "Branch" : "CSE",
    "Batch" : "Z",
    "Marks" : 75 }
print("Name:",student["name"])
print("Branch:",student["branch"])
print("Batch:",student["batch"])
print("Marks:",student["marks"])

# 6. Print the student dictionary in a readable format.
student = {
    "Name" : "pappu",
    "Branch" : "CSE",
    "Batch" : "Z",
    "Marks" : 75
}
for key,value in student.items():
    print(f"{key.capitalize()}:{value}")
