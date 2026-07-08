import numpy as np

# -----------------------------------------------------------
# Question 1: Create a NumPy Array
# -----------------------------------------------------------
marks = np.array([85, 90, 78, 92, 88])
print("Question 1:")
print(marks)
print()

# -----------------------------------------------------------
# Question 2: Array Shape and Size
# -----------------------------------------------------------
print("Question 2:")
print("Shape:", marks.shape)
print("Size:", marks.size)
print()

# -----------------------------------------------------------
# Question 3: Basic Calculations
# -----------------------------------------------------------
print("Question 3:")
print("Total:", marks.sum())
print("Average:", marks.mean())
print("Maximum:", marks.max())
print("Minimum:", marks.min())
print()

# -----------------------------------------------------------
# Question 4: Create a 2D Array
# -----------------------------------------------------------
arr_2d = np.array([[10, 20, 30],
                    [40, 50, 60]])
print("Question 4:")
print(arr_2d)
print()

# -----------------------------------------------------------
# Question 5: Indexing and Slicing
# -----------------------------------------------------------
print("Question 5:")
print(arr_2d[1, 1])   # value 50 -> row index 1, column index 1
print(arr_2d[0])       # first row
print()

# -----------------------------------------------------------
# Question 6: Element-Wise Operations
# -----------------------------------------------------------
numbers = np.array([1, 2, 3, 4, 5])
print("Question 6:")
print(numbers * 10)
print()

# -----------------------------------------------------------
# Question 7: Filter Values
# -----------------------------------------------------------
high_marks = marks[marks >= 90]
print("Question 7:")
print(high_marks)
print()

# -----------------------------------------------------------
# Question 8: Student Marks Matrix
# -----------------------------------------------------------
student_marks = np.array([[85, 78, 90],
                           [92, 88, 95],
                           [76, 82, 80]])

# axis=1 -> average across each row (i.e., per student)
student_avg = student_marks.mean(axis=1)
print("Question 8:")
print(np.round(student_avg, 2))
