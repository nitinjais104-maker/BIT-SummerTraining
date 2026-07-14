import numpy as np

# Question 1: Create a NumPy Array
marks = np.array([85, 90, 78, 92, 88])
print("Question 1:")
print(marks)

# Question 2: Array Shape and Size
print("\nQuestion 2:")
print("Shape:", marks.shape)
print("Size:", marks.size)

# Question 3: Basic Calculations
print("\nQuestion 3:")
print("Total:", np.sum(marks))
print("Average:", np.mean(marks))
print("Maximum:", np.max(marks))
print("Minimum:", np.min(marks))

# Question 4: Create a 2D Array
arr2d = np.array([
    [10, 20, 30],
    [40, 50, 60]
])

print("\nQuestion 4:")
print(arr2d)

# Question 5: Indexing and Slicing
print("\nQuestion 5:")
print(arr2d[1, 1])      # 50
print(arr2d[0])         # First row

# Question 6: Element-Wise Operations
numbers = np.array([1, 2, 3, 4, 5])

print("\nQuestion 6:")
print(numbers * 10)

# Question 7: Filter Values
print("\nQuestion 7:")
print(marks[marks >= 90])

# Question 8: Student Marks Matrix
students = np.array([
    [85, 78, 90],
    [92, 88, 95],
    [76, 82, 80]
])

print("\nQuestion 8:")
print(np.round(np.mean(students, axis=1), 2))