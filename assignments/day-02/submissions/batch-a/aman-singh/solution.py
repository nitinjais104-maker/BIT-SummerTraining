# Question 1: Positive, Negative, or Zero
num = int(input("Enter a number: "))

if num > 0:
    print("Positive number")
elif num < 0:
    print("Negative number")
else:
    print("Zero")


# Question 2: Even or Odd
num2 = int(input("Enter another number: "))

if num2 % 2 == 0:
    print("Even number")
else:
    print("Odd number")


# Question 3: List of 10 numbers
numbers = [1,2,3,4,5,6,7,8,9,10]

print("Numbers in the list:")
for n in numbers:
    print(n)


# Question 4: Function to calculate average
def calculate_average(m1, m2, m3):
    return (m1 + m2 + m3) / 3

avg = calculate_average(80, 90, 100)
print("Average:", avg)


# Question 5: Grade student
def grade_student(marks):
    if marks >= 90:
        print("Grade: A")
    elif marks >= 75:
        print("Grade: B")
    elif marks >= 50:
        print("Grade: C")
    else:
        print("Fail")

grade_student(85)