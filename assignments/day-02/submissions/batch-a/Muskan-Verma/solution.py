# 1. Write a program to check whether a number is positive, negative, or zero.
num=int(input("enter a num : "))
if num>0:
    print("positive")
elif num<0:
    print("negative")
else:
    print("zero")
# 2. Write a program to check whether a number is even or odd.
n=int(input("enter n : "))
if n%2==0:
    print("even")
else:
    print("odd")
# 3. Create a list of 10 numbers and print each number using a loop.
list=[1,2,3,4,5,6,7,8,9,10]
for i in list:
    print(i)
# 4. Write a function named `calculate_average` that takes 3 marks and returns the average.
def calculate_average(mark1,mark2,mark3):
    return (mark1+mark2+mark3)/3
print(calculate_average(80,90,85))

# 5. Write a function named `grade_student` that prints a grade based on marks.
def grade_student(marks):
    if marks>=90:
        print("A")
    elif marks>=75:
        print("B")
    elif marks>=60:
        print("C")
    elif marks>=40:
        print("D")
    else:
        print("Fail")
grade_student(85)
