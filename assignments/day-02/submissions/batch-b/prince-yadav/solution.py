# 1. Write a program to check whether a number is positive, negative, or zero.

number=int(input("Enter a number to check negative or positive : "))

if number >=0:
    print(number ," is positive number")
else:
    print(number,"is Negative number ")


# 2. Write a program to check whether a number is even or odd.


number=int(input("Enter a number to check even or Odd : "))
if number%2==0:
    print(number,"is a Even number ")
else:
    print(number,"is a Odd number")


# 3. Create a list of 10 numbers and print each number using a loop.

lst = [1,2,3,4,5,6,7]
for i in lst:
    print(i)

# 4. Write a function named `calculate_average` that takes 3 marks and returns the average.

def calculate_average(mark1,mark2,mark3):
    average=(mark1+mark2+mark3)/3
    return average

result=calculate_average(34,76,79)
print("Average of marks : ",result)



# 5. Write a function named `grade_student` that prints a grade based on marks.
def grade_student(marks):
    if marks>= 90:
          return "grade = A+"
    elif marks >= 80:
        return "grade = A"
    elif marks >= 70 :
        return "grade = B"
    elif marks>= 60:
        return "grade = C"
    elif marks>= 50:
        return "grade = D"
    else:
        return "grade= F"


marks=int(input("Enter your marks :"))

result=grade_student(marks)
print(result)