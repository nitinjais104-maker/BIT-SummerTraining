#1. Positive, Negative, or Zero
num = int(input("Enter a number: "))

if num > 0:
    print("Positive")
elif num < 0:
    print("Negative")
else:
    print("Zero")

#2. Even or Odd
num = int(input("Enter a number: "))

if num % 2 == 0:
    print("Even")
else:
    print("Odd")

#3. Print 10 Numbers Using a Loop
numbers = [1,2,3,4,5,6,7,8,9,10]

for n in numbers:
    print(n)

#4. Average of 3 Marks
mark1 = float(input("Enter the first mark: "))
mark2 = float(input("Enter the second mark: "))
mark3 = float(input("Enter the third mark: "))

average = (mark1 + mark2 + mark3) / 3
print("The average of the three marks is:", average)

#5. Grade Students
if average >= 80:
    print("Grade: A")
elif average >= 60:
    print("Grade: B")
else:
    print("Grade: C")