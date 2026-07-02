# Day 2 Assignment
#===========================================================>>>
#Q.1. Write a program to check whether a number is positive, negative, or zero.
num = float(input("Enter a number: "))

if num > 0:
    print(f"The number is positive:{num}")
elif num < 0:
    print(f"The number is negative: {num}")
else:
    print(f"The number is zero: {num}")                                # Checking whether a number is positive, negative or zero
print("="*50)

#==========================================================>>>
#Q.2. Write a program to check whether a number is even or odd.
num = int(input("Enter a number: "))

if num % 2 == 0:
    print(f"The number is even: {num}")
else:
    print(f"The number is odd: {num}")                                  # Checking whether a number is even or odd
print("="*50)
#==========================================================>>>
#Q.3. Create a list of 10 numbers and print each number using a loop.
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print("The numbers in the list are:")
for num in numbers:
    print(num)                                                        # Printing each number in the list using a loop   
print("="*50)
#==========================================================>>>
#Q.4. Write a function named `calculate_average` that takes 3 marks and returns the average.
def calculate_average(mark1, mark2, mark3):
    average = (mark1 + mark2 + mark3) / 3
    return average
marks1 = float(input("Enter marks for subject 1: "))
marks2 = float(input("Enter marks for subject 2: "))
marks3 = float(input("Enter marks for subject 3: "))
average_marks = calculate_average(marks1, marks2, marks3)
print(f"The average marks are: {average_marks}")                            # Function to calculate the average of three marks
print("="*50)
#==========================================================>>>
#Q.5. Write a function named `grade_student` that prints a grade based on marks.
def grade_student(marks):
    if marks >= 90:
        return "A"
    elif marks >= 80:
        return "B"
    elif marks >= 70:
        return "C"
    elif marks >= 60:
        return "D"
    else:
        return "F"
marks = float(input("Enter the marks: "))
grade = grade_student(marks)
print(f"The grade is: {grade}")                                              # Function to print grade based on marks
print("="*50)
#==========================================================>>>