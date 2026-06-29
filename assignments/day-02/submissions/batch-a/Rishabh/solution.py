# Question 1: Check whether a number is positive, negative, or zero

number = int(input("Enter a number: "))

if number > 0:
    print("Positive")
elif number < 0:
    print("Negative")
else:
    print("Zero")


# Question 2: Check whether a number is even or odd

number = int(input("Enter another number: "))

if number % 2 == 0:
    print("Even")
else:
    print("Odd")


# Question 3: Print a list of 10 numbers using a loop

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print("List of numbers:")
for num in numbers:
    print(num)


# Question 4: Function to calculate average

def calculate_average(mark1, mark2, mark3):
    return (mark1 + mark2 + mark3) / 3


average = calculate_average(80, 90, 85)
print("Average:", average)


# Question 5: Function to print grade

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


grade_student(average)