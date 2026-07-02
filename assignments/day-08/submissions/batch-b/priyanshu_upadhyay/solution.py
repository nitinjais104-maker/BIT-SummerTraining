# Day 8 Assignment - NumPy Fundamentals

import numpy as np

# Question 1: Create a NumPy Array
marks = np.array([85, 90, 78, 92, 88])
print(marks)

# Question 2: Array Shape and Size
print("Shape:", marks.shape)
print("Size:", marks.size)

# Question 3: Basic Calculations
print("Total:", np.sum(marks))
print("Average:", np.mean(marks))
print("Maximum:", np.max(marks))
print("Minimum:", np.min(marks))

# Question 4: Create a 2D Array
array_2d = np.array([[10, 20, 30], [40, 50, 60]])
print(array_2d)

# Question 5: Indexing and Slicing
print(array_2d[1, 1])
print(array_2d[0])

# Question 6: Element-Wise Operations
numbers = np.array([1, 2, 3, 4, 5])
print(numbers * 10)

# Question 7: Filter Values
filtered = marks[marks >= 90]
print(filtered)

# Question 8: Student Marks Matrix
matrix = np.array([[85, 78, 90], [92, 88, 95], [76, 82, 80]])
avg = np.round(np.mean(matrix, axis=1), 2)
print(avg)