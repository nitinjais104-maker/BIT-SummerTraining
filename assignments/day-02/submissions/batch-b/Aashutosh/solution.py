
# 1. Check whether a number is positive, negative, or zero

number = -7

if number > 0:
    print("The number is positive")
elif number < 0:
    print("The number is negative")
else:
    print("The number is zero")
print("="*30)

# 2. Check whether a number is even or odd
num = 15

if num % 2 == 0:
    print("\nThe number is even")
else:
    print("\nThe number is odd")
print("="*30)

# 3. List of 10 numbers, printed using a loop
numbers = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

print("\nNumbers in the list:")
for n in numbers:
    print(n)
print("="*30)

# 4. Function to calculate average of 3 marks
def calculate_average(marks1, marks2, marks3):
    average = (marks1 + marks2 + marks3) / 3
    return average


avg = calculate_average(85, 90, 78)
print("\nAverage of marks:", avg)
print("="*30)

# 5. Function to print grade based on marks
def grade_student(marks):
    if marks >= 90:
        print("Grade: A")
    elif marks >= 75:
        print("Grade: B")
    elif marks >= 60:
        print("Grade: C")
    elif marks >= 40:
        print("Grade: D")
    else:
        print("Grade: F")


print("\nGrade for the average marks:")
grade_student(avg)