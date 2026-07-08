#1 Write a program to check whether a number is positive, negative, or zero.

number = float(input("Enter a number: "))     #input a number from user
if number > 0:    #check if the number is greater than zero
    print("The number is positive.")
elif number < 0:  #check if the number is less than zero
    print("The number is negative.")
else:
    print("The number is zero.")
print("_"*45)


#2 Write a program to check whether a number is even or odd.

number = int(input("Enter a number: "))         #input a number from user
if number % 2 == 0:   #check if the number is divisible by 2
    print("The number is even.")
else:
    print("The number is odd.")
print("_"*45)


#3. Create a list of 10 numbers and print each number using a loop.

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]     #list of 10 numbers
for n in numbers:
    print(n)
print("_"*45)

#4. Write a function named `calculate_average` that takes 3 marks and returns the average.

def calculate_average(mark1, mark2, mark3):   #function definition with three parameters
    #calculating total marks and average of the marks
    total_marks=mark1+mark2+mark3
    average=total_marks/3
    return total_marks,average    #returning total marks and average of the marks

#calling the function and storing the returnes values
total, average = calculate_average(85, 90, 78)
print("Total Marks:", total)
print("Average Marks:", average)
print("_"*45)


#5 Write a function named `grade_student` that prints a grade based on marks.

def grade_student(marks): #function with marks as parameter
    
    average=total/5
    percentage=(total*100)/500

    #printing the informations
    print(name)
    print("age:=",age)
    print("total marks:",total)
    print("average marks:",average)
    print("percentage marks:",percentage)
    print("__"*45)

    ##checking the marks based on condition for printing grades
    if percentage>=90:
        grade="grade a"
    elif percentage>=75:
        grade="grade b"
    elif percentage>=40:
        grade="grade c"
    elif percentage<40:
        grade="grade f"
    if percentage>=40:
        status="pass"
    else:
        status="fail"
    return grade,status      #returning grade and status of the student
    
    print("="*45)

#input name age and marks
name=input("Enter your name: ")
age=int(input("Enter your age: "))
maths=float(input("Enter your maths: "))
physics=float(input("Enter your physics: "))
chemistry=float(input("Enter your chemistry: "))
english=float(input("Enter your english: "))
hindi=float(input("Enter your hindi: "))
print("_"*45)

#calcutating the total, average, percentage of marks
total=maths+physics+chemistry+english+hindi

#callling the function
grade = grade_student(total) #passing total marks as argument.

print("grade:",grade)   #printing the grade of the student
