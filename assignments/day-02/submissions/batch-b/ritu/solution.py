# Day 2 Assignment
## Topic: Conditions, Loops,and Functions

## Questions.1
# print("Write a program to check whether a number is positive,negative,or zero.")
number = float(input("Enter a number: "))  # prompt the user to input a number and convert it to a float

if number > 0 : 
    print("The number is positive.") # the number is greater than zero  
elif number < 0 :    
    print("The number is negative.") # the number is less than zero
else: 
    print("The number is zero.") # the number must be zero both condition above are false


## Question.2
# print("Write a program to check whether a number is even or odd.")
number = int(input("Enter a number:")) # the user to type an integer

if number % 2 == 0: # Modulo operator is divisible by 2 so it is even
    print(f"{number} is an even number.") # the number is even number
else:
    print(f"{number} is an odd number.") # the number is odd number

## Question.3
# print("Create a list of 10 numbers and print each number using a loop.")
numbers = [5,10,15,20,25,30,35,40,45,50] # create a list containing 10 numbers

for num in numbers: # usa a for loop to iterate and print each number
    print(num) # print the value of num


## Question.4
# print("Write a function named ` calculate_average ` that takes 3 marks and returns the averages.")
def calculate_average(marks1,marks2,marks3): # this is a key and the function
    """Takes three marks and returns their average.""" 
    total = marks1 + marks2 + marks3
    average = total/ 3
    return average
average=calculate_average(56,78,67)
print("Average of three marks:",average)

## Question.5
# print("Write a function named ` grade_student ` that prints a grade based on marks.")
def grade_student(marks):
    if marks >= 90:
        print("Grade A")
    elif marks >= 80:
        print("Grade B")
    elif marks >= 70:
        print("Grade C")
    elif marks >= 60:
        print("Grade D")
    else:
        print("Grade F")

grade_student(78)
        