import numpy as np

# Question 1: Create array
marks = np.array([85, 90, 78, 92, 88])
print(marks)

# Question 2: Shape and size
print("Shape:", marks.shape)
print("Size:", marks.size)

# Question 3: Calculations
print("Total:", np.sum(marks))
print("Average:", np.mean(marks))
print("Maximum:", np.max(marks))
print("Minimum:", np.min(marks))

# Question 4: 2D array
matrix = np.array([
    [10, 20, 30],
    [40, 50, 60]
])
print(matrix)

# Question 5: Indexing and slicing
print(matrix[1, 1])   # 50
print(matrix[0])      # [10 20 30]

# Question 6: Element-wise operation
numbers = np.array([1, 2, 3, 4, 5])
print(numbers * 10)

# Question 7: Filter values
filtered = marks[marks >= 90]
print(filtered)

# Question 8: Student marks matrix
students = np.array([
    [85, 78, 90],
    [92, 88, 95],
    [76, 82, 80]
])

avg = np.mean(students, axis=1)
print(np.round(avg, 2))