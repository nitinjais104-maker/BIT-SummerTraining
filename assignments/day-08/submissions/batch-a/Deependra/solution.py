# Question 1: Create a NumPy Array
# Create a one-dimensional NumPy array containing these marks and print it:
# [85, 90, 78, 92, 88]
import numpy as np
marks = np.array([85, 90, 78, 92, 88])

print("Marks Array:")
print(marks)

# Question 2: Array Shape and Size
# Print the shape and total number of elements in the array from Question 1.
# Expected Output:
# Shape: (5,)
# Size: 5

print("\nShape:", marks.shape)
print("Size:", marks.size)

# Question 3: Basic Calculations
# Using the marks array, print the total, average, maximum, and minimum.
# Expected Output:
# Total: 433
# Average: 86.6
# Maximum: 92
# Minimum: 78
print("\nTotal:", np.sum(marks))
print("Average:", np.mean(marks))
print("Maximum:", np.max(marks))
print("Minimum:", np.min(marks))


# Question 4: Create a 2D Array
# Create this 2D NumPy array and print it:
# [[10, 20, 30],
#  [40, 50, 60]]

array_2d = np.array([
    [10, 20, 30],
    [40, 50, 60]
])

print("\n2D Array:")
print(array_2d)


# Question 5: Indexing and Slicing
# From the 2D array in Question 4, print the value 50 and then print the first row.
# Expected Output:
# 50
# [10 20 30]
print("\nValue 50:")
print(array_2d[1, 1])

print("First Row:")
print(array_2d[0])



# Question 6: Element-Wise Operations
# Create numbers = np.array([1, 2, 3, 4, 5]). 
# Print the result of multiplying every element by 10.
# Expected Output:
# [10 20 30 40 50]
numbers = np.array([1, 2, 3, 4, 5])

print("\nNumbers multiplied by 10:")
print(numbers * 10)

# Question 7: Filter Values
# Using the marks array, create and print a new array containing marks greater than 
# 90.
# Expected Output:
# [90 92]
high_marks = marks[marks >= 90]

print("\nMarks greater than or equal to 90:")
print(high_marks)


# Question 8: Student Marks Matrix
# Create this matrix, where each row represents Python, Data Analytics, and AI marks for one student:
#[[85, 78, 90],
#[92, 88, 95],
# [76, 82, 80]]
# Expected Output:
# [84.33 91.67 79.33]

student_marks = np.array([
    [85, 78, 90],
    [92, 88, 95],
    [76, 82, 80]
])

student_average = np.mean(student_marks, axis=1)

print("\nAverage marks of each student:")
print(np.round(student_average, 2))
