# 1. Write a program to check whether a number is positive, negative, or zero.


number = float(input("Enter a number: "))

if number > 0:
    print(" The number is Positive.")
elif number < 0:
    print(" The number is Negative.")
else:
    print(" The number is Zero.")


# 2. Write a program to check whether a number is even or odd.


number = int(input("Enter a number: "))

if number % 2 == 0:
    print( number, "is an Even number.")
else:
    print( number, "is an Odd number.")


# 3. Create a list of 10 numbers and print each number using a loop.


numbers = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50]

print("Printing all numbers in the list:")

for num in numbers:

    print( num)


# 4. Write a function named `calculate_average` that takes 3 marks and returns the average.


def calculate_average(mark1, mark2, mark3):
    return (mark1 + mark2 + mark3) / 3

m1 = float(input("Enter first mark: "))
m2 = float(input("Enter second mark: "))
m3 = float(input("Enter third mark: "))

print("Average Marks:", calculate_average(m1, m2, m3))


# 5. Write a function named `grade_student` that prints a grade based on marks.


def grade_student(physics, chemistry, maths, english, computer):
    average = (physics + chemistry + maths + english + computer) / 5

    print("\n----- Marksheet -----")
    print("Physics  :", physics)
    print("Chemistry:", chemistry)
    print("Maths    :", maths)
    print("English  :", english)
    print("Computer :", computer)
    print("Average  :", average)

    if average >= 90:
        print(" Grade A")
    elif average >= 75:
        print(" Grade B")
    elif average >= 60:
        print(" Grade C")
    elif average >= 40:
        print(" Grade D")
    else:
        print(" Grade F")

phy = int(input("Enter Physics marks: "))
chem = int(input("Enter Chemistry marks: "))
maths = int(input("Enter Maths marks: "))
eng = int(input("Enter English marks: "))
comp = int(input("Enter Computer marks: "))

grade_student(phy, chem, maths, eng, comp)
