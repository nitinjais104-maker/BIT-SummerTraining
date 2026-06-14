#day2

#1 check a number is positive, negative, or zero.

no=int(input("enter the no:"))
if no > 0:
    print("+ve no")
elif no < 0:
    print("-ve no")
else:
    print("zero")


# 2 check whether a number is even or odd.
no=int(input("enter the no:"))
if no%2==0:
    print("even no")
else:
    print("odd no.")


# 3. Create a list of 10 numbers and print each number using a loop.
l=[1,2,3,4,5,6,7,8,9,10]
for i in l:
    print(i,end=",")
print()


#4 calsute avg by function
def calculate_average(m1, m2, m3):
    avg = (m1 + m2 + m3) / 3
    return avg
print("Average:", calculate_average(65, 70, 95))


#5 grade_student that prints a grade based on marks
def grade_student(marks):
    if marks>=90:
        print("grade A")
    elif marks>=80:
        print("grade B")
    elif marks>=70:
        print("grade C")
    elif marks>=60:
        print("grade D")
    elif marks>=50:
        print("grade E")
    else:
        print("fail")
    return marks
marks=int(input("enter the marks"))
print((marks))