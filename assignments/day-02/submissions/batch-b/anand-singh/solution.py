# 1. Write a program to check whether a number is positive, negative, or zero.
number = float(input("enter a number: "))
if number > 0:
    print("positive number")
elif number < 0:
    print("negative number")
else:
    print("zero")    
# 2. Write a program to check whether a number is even or odd.
number = int(input("enter anumber:"))
if number%2 == 0:
    print("even number")
else:
    print("odd number")
# 3. Create a list of 10 numbers and print each number using a loop.
nums = ["1,2,3,4,5,6,7,8,9,10"]
for num in nums:
    print(num)
# 4. Write a function named `calculate_average` that takes 3 marks and returns the average.
print("enter 3 marks")
mark1 = float(input("enter mark 1: "))
mark2 = float(input("enter mark 2: "))
mark3 = float(input("enter mark 3: "))
average = (mark1 + mark2 + mark3)/3
print("average marks is:", average)
# 5. Write a function named `grade_student` that prints a grade based on marks.
print("enter marks to check grade:")
mark = float(input("enter mark: "))
if mark >= 80:
    print("Grade: A")
elif mark >= 70:
    print("Grade: B")
elif mark >= 60:
    print("Grade: C")
else:
    print("Grade: D")

