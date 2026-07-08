number = 10

if number > 0:
    print("Positive")
elif number < 0:
    print("Negative")
else:
    print("Zero")

if number % 2 == 0:
    print("Even")
else:
    print("Odd")

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for n in numbers:
    print(n)

def calculate_average(m1, m2, m3):
    return (m1 + m2 + m3) / 3

print("Average:", calculate_average(80, 90, 85))

def grade_student(marks):
    if marks >= 90:
        print("Grade: A")
    elif marks >= 75:
        print("Grade: B")
    elif marks >= 60:
        print("Grade: C")
    else:
        print("Grade: D")

grade_student(85)