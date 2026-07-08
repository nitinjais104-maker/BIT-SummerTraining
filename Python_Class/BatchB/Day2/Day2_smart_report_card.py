student_name = input("Enter student name: ")
age = int(input("Enter age: "))

maths = float(input("Enter marks in Maths: "))
physics = float(input("Enter marks in Physics: "))
chemistry = float(input("Enter marks in Chemistry: "))
english = float(input("Enter marks in English: "))
computer = float(input("Enter marks in Computer: "))

total = maths + physics + chemistry + english + computer
average = total / 5
percentage = (total / 500) * 100

is_passed = (
    maths >= 40 and 
    physics >= 40 and 
    chemistry >= 40 and 
    english >= 40 and 
    computer >= 40 and 
    percentage >= 50
)

if percentage >= 90:
    grade = "A+"
elif percentage >= 80:
    grade = "A"
elif percentage >= 70:
    grade = "B"
elif percentage >= 60:   
    grade = "C"
elif percentage >= 50:
    grade = "D"
else:
    grade = "F"

status = "PASS" if is_passed else "FAIL"

print("=" * 45)
print("STUDENT REPORT CARD")
print("=" * 45)
print(f"Name: {student_name}")
print(f"Age: {age}")
print("-" * 45)
print(f"Maths: {maths}")
print(f"Physics: {physics}")
print(f"Chemistry: {chemistry}")
print(f"English: {english}")
print(f"Computer: {computer}")
print("-" * 45)
print(f"Total Marks: {total}/500")
print(f"Average Marks: {average:.2f}")
print(f"Percentage: {percentage:.2f}%")
print(f"Grade: {grade}")
print(f"Result: {status}")