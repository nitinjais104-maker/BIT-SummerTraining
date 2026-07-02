# 1. Write a program to check whether a number is positive, negative, or zero.
num = float(input("Enter a number: "))

if num > 0:
    print("The number is Positive.")
elif num < 0:
    print("The number is Negative.")
else:
    print("The number is Zero.")

# 2. Write a program to check whether a number is even or odd.
num = int(input("Enter a number: "))

if num % 2 == 0:
    print("The number is Even.")
else:
    print("The number is Odd.")


# 3. Create a list of 10 numbers and print each number using a loop.
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Print each number using a loop
for num in numbers:
    print(num)


# 4. Write a function named `calculate_average` that takes 3 marks and returns the average.
def calculate_average(mark1, mark2, mark3):
    average = (mark1 + mark2 + mark3) / 3
    return average

# Example usage
result = calculate_average(80, 90, 85)
print("Average marks:", result)

# 5. Write a function named `grade_student` that prints a grade based on marks.
def grade_student(marks):
    if marks >= 90:
        print("Grade: A")
    elif marks >= 75:
        print("Grade: B")
    elif marks >= 50:
        print("Grade: C")
    else:
        print("Grade: F")

# Take input from the user
marks = float(input("Enter your marks: "))

# Call the function
grade_student(marks)