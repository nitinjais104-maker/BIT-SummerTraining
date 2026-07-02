#program to check wheater the number is negative ,positive or zero
num=int(input("Enter a number:"))
if num > 0:
    print("num is positive")
elif num < 0:
    print("num is negative")
else:
    print("num is zero")
    
#program to check whether the number is even or odd
num=int(input("Enter a number:"))
if num%2==0:
    print("number is even")
else:
    print("number is odd")
    

#create a list of 10 number and print each using a loop
list=[10,20,30,40,50,60,70,80,90,100]
for i in list :
    print(i)
    
    
#function to calculate average of 3 number
def calculate_average(a,b,c):
    avg=(a+b+c)/3
    print("Average is:", avg)

num1=int(input("Enter first marks:"))
num2=int(input("Enter second marks:"))
num3=int(input("Enter third marks:"))

calculate_average(num1,num2,num3)

# fuction that print a grade based on marks
def grade_student(marks):
    if marks>= 90:
        print(" Grade A")
    elif marks>=80:
        print("Grade B")
    elif marks>=70:
        print("Grade C")
    elif marks>=60:
        print("Grade D")
    elif marks>=50:
        print("Grade E")
    else:
        print("Grade F")
    
marks=int(input("Enter the marks:"))
grade_student(marks)