
# 1->   This program takes user input for name, age, and college name and prints them out.  
NAME=input("Enter your name: ")
age=int(input("Enter your age: "))
college_name=input("Enter your college name: ")
print(f"your name :{NAME}")
print(f"your age :{age}")
print(f"your college name :{college_name}")

# 2->   This program takes user input for name, age, marks, and city and prints them out.
name=input("Enter your name: ")
age=int(input("Enter your age: "))
marks=int(input("Enter your marks: "))
city=input("Enter your city: ")

print(f"your name :{name}")
print(f"your age :{age}")
print(f"your marks :{marks}")
print(f"your city :{city}")

# 3->   This program use string , integer, float, and boolean data types to take user input and print its types.
a=input("Enter your name: ")
b=int(input("Enter your ID NUMBER: "))
c=float(input("Enter your age: "))
d=bool(input("Are you a student? (True/False): "))
print(type(a))
print(type(b))
print(type(c))
print(type(d))

# 4->   This program creates a list of numbers based on user input and prints the list.
list=[2,3,6,5,8]
print(list)

# 5->   This program creates a dictionary with user input for name, course, city, and batch and prints the dictionary.
name=input("Enter your name: ") 
course=input("Enter your course: ")
city=input("Enter your city: ") 
batch=input("Enter your batch: ")
student_info={
    "name": name,
    "course": course,
    "city": city,
    "batch": batch
}

print(student_info)
