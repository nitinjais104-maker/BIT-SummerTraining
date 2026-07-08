students = ["Rahul", "Priya", "Amit", "Sneha", "Ravi"]
print("Students:", students)

students.append("Siddharth")
print("After adding:", students)

cities = ("Delhi", "Mumbai", "Lucknow", "Gorakhpur", "Jaipur")
print("Second city:", cities[1])

courses = {"BCA", "BTech", "MBA", "MCA", "BSc"}
courses.add("BBA")
print("Courses:", courses)

student = {
    "name": "Siddharth Pandey",
    "branch": "BCA",
    "batch": "B",
    "marks": 85.5
}

for key, value in student.items():
    print(key, ":", value)