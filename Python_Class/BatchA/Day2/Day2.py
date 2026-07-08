# Variable name = label 
# Value = actual data 
# Type = value ka nature 

# age = "20"
# future_age = int(age) + 5
# print(future_age)


# a = 10 
# b = 10.0

# print(type(a))
# print(type(b))
# print(a == b)


# roll_no = "101"
# marks = "90"
# print(roll_no + marks)


# print(bool(1))
# print(bool(0))
# print(bool(""))
# print(bool("False)"))

#key Rules 
# False
# 0
# 0.0
# ""
# None


# result = None 
# print(result)
# print(type(result))


# result = 0.1 + 0.2
# print(round(result, 2))


# age = 20 
# has_id = True
# print(age >= 18 and has_id)


# print( True and True)
# print(True and False)
# print(False and True)
# print(False and False)


# has_cash = False
# has_upi = True
# print(has_cash or has_upi)


# is_absent = False
# print( not is_absent)
# = -> assignment 
# == -> Comparison


# if marks == 90:
#     print("Excellent")

# age = input("Enter your age: ")
# print(type(age))

# num1 = input("Enter first number: ")
# num2 = input("Enter second number: ")

# print(num1 + num2)

# num1 = int(input("Enter first number: "))
# num2 = int(input("Enter second number: "))

# print(num1 + num2)

# marks1 = float(input("Enter marks 1: "))
# marks2 = float(input("Enter marks 2: "))

# total = marks1 + marks2
# average = total / 2

# print(f"Total: {total}")
# print(f"Average: {average}")

# age = 20 
# has_license = True 

# if age >= 18:
#     if has_license:
#         print("You can drive")
#     else:
#         print("You cannot drive")
# else:
#     print("You cannot drive")

# if age >= 18 and has_license:
#     print("You can drive")
# else:
#     print("You cannot drive")


#Check if number is positive, negative, or zero.
# num = int(input("Enter number: "))

# if num > 0:
#     print("Positive")
# elif num < 0:
#     print("Negative")
# else:
#     print("Zero")

# Find largest of two numbers.
# a = int(input("Enter first number: "))
# b = int(input("Enter second number: "))

# if a > b:
#     print(f"{a} is larger")
# elif b > a:
#     print(f"{b} is larger")
# else:
#     print("Both are equal")


# for i in range(5):
#     print(i)

# for i in range(2,6):
#     print(i)

# for i in range(5,1,-1):
#     print(i)

# num = int(input("Enter number: "))

# for i in range(1, 11):
#     print(num * i)
# num = int(input("Enter number: "))

# for i in range(1, 11):
#     print(f"{num} x {i} = {num * i}")

# for num in range(2, 6):
#     print(f"Table of {num}")
#     for i in range(1, 11):
#         print(f"{num} x {i} = {num * i}")
#     print("-" * 20)

    # 2 x1 = 2 | 3 x 1 = 3 | 4 x 1 = 4 | 5x1 = 5
    # 2 x2 = 4 | 3 x 2 = 6 | 4 x 2 = 8 | 5x2 = 10
    # 2 x3 = 6 | 3 x 3 = 9 | 4 x 3    = 12 | 5x3 = 15

students = ["Priya", "Ravi", "Neha", "Ammit"]

# for student in students:
#     print(student)

# for index, student in enumerate(students):
#     print(f"{index}. {student}")

for i in range(1, 6):
    print(i)

count = 1

while count <= 5:
    print(count)
    count += 1