import numpy as np

# Question 1: Create a NumPy Array
marks = np.array([85, 90, 78, 92, 88])
print(marks)

# Question 2: Array Shape and Size
print(f"Shape: {marks.shape}")
print(f"Size: {marks.size}")

# Question 3: Basic Calculations
print(f"Total: {marks.sum()}")
print(f"Average: {marks.mean()}")
print(f"Maximum: {marks.max()}")
print(f"Minimum: {marks.min()}")

# Question 4: Create a 2D Array
arr_2d = np.array([[10, 20, 30], [40, 50, 60]])
print(arr_2d)

# Question 5: Indexing and Slicing
print(arr_2d[1, 1])
print(arr_2d[0])

# Question 6: Element-Wise Operations
numbers = np.array([1, 2, 3, 4, 5])
print(numbers * 10)

# Question 7: Filter Values
print(marks[marks >= 90])

# Question 8: Student Marks Matrix
student_marks = np.array([[85, 78, 90], [92, 88, 95], [76, 82, 80]])
print(np.round(student_marks.mean(axis=1), 2))
