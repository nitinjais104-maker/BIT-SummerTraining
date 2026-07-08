#1.Write a program to check whether a number is positive, negative, or zero.
num = float(input("give the number"))
if num >0:
    print("number is positive",num)
elif num <0:
    print("number is negative")
else:
    print("number is zero")



#2. Write a program to check whether a number is even or odd.
num = float(input("give a number to checkeven odd"))
if num%2 == 0:
    print("the given number is even")
else:
    print("given number is odd number")



# Create a list of 10 numbers and print each number using a loop.
list1 = [1,2,3,4,5,6,7,55,66,77]
for item in list1:
    print(item,end=" ")


# Write a function named `calculate_average` that takes 3 marks and returns the average.
def calculator_average(mark1,mark2,mark3):
    average = (mark1+mark2+mark3)/3
    return average
avg = calculator_average(90,57,78)
print("Average =",avg)


# Write a function named `grade_student` that prints a grade based on marks.
def grade_student(mark1):
    if mark1>=90:
        return "A"
    elif mark1>=75:
        return "B"
    elif mark1>=60:
        return "C"
    elif mark1>=40:
        return "D"
    else:
        return "F"
grade = grade_student(89)
print("Grade:",grade)
