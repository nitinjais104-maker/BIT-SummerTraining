# Day 8 Assignment
#==========================================================>>>
import numpy as np
# Question 1: Create a NumPy Array
# Create a one-dimensional NumPy array containing these marks and print it:
marks = np.array([85, 90, 78, 92, 88])
print("NumPy array of marks:", marks)
print("="*50)
#==========================================================>>>
# Question 2: Array Shape and Size
# Print the shape and total number of elements in the array from Question 1.
marks = np.array([85, 90, 78, 92, 88])
print("Shape of the array:", marks.shape)
print("Total number of elements :", marks.size)
print("="*50)
#==========================================================>>>
# Question 3: Basic Calculations
# Using the marks array, print the total, average, maximum, and minimum.
marks = np.array([85, 90, 78, 92, 88])
total = np.sum(marks)
average = np.mean(marks)
maximum = np.max(marks)
minimum = np.min(marks)
print("Total:", total)
print("Average:", average)
print("Maximum:", maximum)
print("Minimum:", minimum)
print("="*50)
#========================================================>>>
# Question 4: Create a 2D Array
# Create this 2D NumPy array and print it
array = np.array([[10,20,30], [40,50,60]])
print("2D NumPy array:\n", array)
print("="*50)
#========================================================>>>
## Question 5: Indexing and Slicing
# From the 2D array in Question 4, print the value `50` and then print the first row.
array = np.array([[10,20,30], [40,50,60]])
print("Value at (1, 1):", array[1, 1])  
print("First row:", array[0])  
print("="*50)
#========================================================>>>
### Question 6: Element-Wise Operations
# Create `numbers = np.array([1, 2, 3, 4, 5])`. Print the result of multiplying every element by 10.
numbers = np.array([1, 2, 3, 4, 5])
result = numbers * 10
print("Multiplying every element by 10:", result)
print("="*50)
#========================================================>>>
## Question 7: Filter Values
# Using the marks array, create and print a new array containing marks greater than or equal to 90.
marks = np.array([85, 90, 78, 92, 88])
for mark in marks:
    if mark >= 90:
        filtered_marks = marks[marks >= 90]
print("Marks greater than or equal to 90:", filtered_marks)
print("="*50)
#========================================================>>>
## Question 8: Student Marks Matrix
# Create this matrix, where each row represents Python, Data Analytics, and AI marks for one student:
student_marks = np.array([[85, 78, 90], [92, 88, 95], [76, 82, 80]])
print("Student Marks Matrix:\n", student_marks)
print("="*50)
#=========================================================>>>