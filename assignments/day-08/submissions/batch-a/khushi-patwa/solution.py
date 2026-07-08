# Topic: NumPy Fundamentals
import numpy as np

# Question 1: Create Marks Array
marks = np.array([85, 90, 78, 92, 88])
print(marks)

print("="*45)

# Question 2: Shape and Size
print("Shape:", marks.shape)
print("Size:", marks.size)

print("="*45)

# Question 3: Basic Calculations
print("Total:", np.sum(marks))
print("Average:", np.mean(marks))
print("Maximum:", np.max(marks))
print("Minimum:", np.min(marks))

print("="*45)

# Question 4: Create 2D Array
student_scores = np.array([
    [10, 20, 30],
    [40, 50, 60]
])
print(student_scores)

print("="*45)

# Question 5: Indexing and Slicing
print(student_scores[1, 1])
print(student_scores[0])

print("="*45)

# Question 6: Element-Wise Operations
numbers = np.array([1, 2, 3, 4, 5])
print(numbers * 10)

print("="*45)

# Question 7: Filter Values
high_marks = marks[marks >= 90]
print(high_marks)

print("="*45)

# Question 8: Student Marks Matrix
student_marks = np.array([
    [85, 78, 90],
    [92, 88, 95],
    [76, 82, 80]
])
average_marks = np.round(np.mean(student_marks, axis=1), 2)
print(average_marks)
