# # Day 2 Assignment

# ## Topic: Conditions, Loops, and Functions

# Complete the questions below in one file named `solution.py`.

# ## Questions

# 1. Write a program to check whether a number is positive, negative, or zero.


num = int(input("Enter the number: "))
if num>0:
    print(f"{num} is positive number.")
elif num<0:
    print(f"{num} is negative number.")
else:
    print(f"{num} is zero.")





# 2. Write a program to check whether a number is even or odd.

num = int(input("Enter a number: "))
if num%2 ==0:
    print(f"{num} is even number.")
else:
    print(f"{num} is odd number.")



# 3. Create a list of 10 numbers and print each number using a loop.


list = [1,2,3,4,5,6,7,8,9,10]
print("Elements in the list are:")
for i in range(len(list)):
    print(list[i])


# 4. Write a function named `calculate_average` that takes 3 marks and returns the average.

def calculate_average(marks1, marks2, marks3):

    d=(marks1 + marks2 + marks3)/3
print(calculate_average(10,20,30))


#  5. Write a function named `grade_student` that prints a grade based on marks.

def subjects(phy, chem, maths, eng, hindi, comp):
    total_marks = phy + chem + maths + eng + hindi + comp
    num_percent = (total_marks/600)*100
    if num_percent >= 90:
        print("Grade A")
    elif num_percent >= 80 and num_percent < 90:
        print("Grade B")
    elif num_percent >= 70 and num_percent < 80:
        print("Grade C")
    elif num_percent >= 60 and num_percent < 70:
        print("Grade D")
    elif num_percent >= 40 and num_percent < 60:
        print("Grade E")
    else:
        print("Fail")
    return num_percent
phy = int(input("Enter Physics marks: "))   
chem = int(input("Enter Chemistry marks: "))
maths = int(input("Enter Maths marks: "))
eng = int(input("Enter English marks: "))
hindi = int(input("Enter Hindi marks: "))
comp = int(input("Enter Computer marks: "))
print(subjects(phy, chem, maths, eng, hindi, comp))


# ## Submission

# Create your solution here:

# ```txt
# assignments/day-02/submissions/batch-a/your-name/solution.py
# ```

# or

# ```txt
# assignments/day-02/submissions/batch-b/your-name/solution.py
# ```
