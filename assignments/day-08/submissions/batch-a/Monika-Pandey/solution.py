# # Day 8 Assignment

# ## Questions

# ### Question 1: Create a NumPy Array

# Create a one-dimensional NumPy array containing these marks and print it:

# ```python
# [85, 90, 78, 92, 88]
# ```
import numpy as np

marks = np.array([85, 90, 78, 92, 88])

print(marks)

# ### Question 2: Array Shape and Size

# Print the shape and total number of elements in the array from Question 1.

# ```python
# # Expected Output:
# # Shape: (5,)
# # Size: 5
# ```
import numpy as np

marks = np.array([85, 90, 78, 92, 88])

print("Shape:", marks.shape)
print("Size:", marks.size)

# ### Question 3: Basic Calculations

# Using the marks array, print the total, average, maximum, and minimum.

# ```python
# # Expected Output:
# # Total: 433
# # Average: 86.6
# # Maximum: 92
# # Minimum: 78
# ```
import numpy as np

marks = np.array([85, 90, 78, 92, 88])

print("Total:", marks.sum())
print("Average:", marks.mean())
print("Maximum:", marks.max())
print("Minimum:", marks.min())


# ### Question 4: Create a 2D Array

# Create this 2D NumPy array and print it:

# ```python
# [[10, 20, 30],
#  [40, 50, 60]]
# ```
import numpy as np

array_2d = np.array([
    [10, 20, 30],
    [40, 50, 60]
])

print(array_2d)

# ### Question 5: Indexing and Slicing

# From the 2D array in Question 4, print the value `50` and then print the first row.

# ```python
# # Expected Output:
# # 50
# # [10 20 30]
# ```
import numpy as np

array_2d = np.array([
    [10, 20, 30],
    [40, 50, 60]
])

print(array_2d[1, 1])
print(array_2d[0])

# ### Question 6: Element-Wise Operations

# Create `numbers = np.array([1, 2, 3, 4, 5])`. Print the result of multiplying every element by 10.

# ```python
# # Expected Output:
# # [10 20 30 40 50]
# ```
import numpy as np

numbers = np.array([1, 2, 3, 4, 5])

print(numbers * 10)

# ### Question 7: Filter Values

# Using the marks array, create and print a new array containing marks greater than or equal to 90.

# ```python
# # Expected Output:
# # [90 92]
# ```
import numpy as np

marks = np.array([85, 90, 78, 92, 88])

result = marks[marks >= 90]

print(result)

# ### Question 8: Student Marks Matrix

# Create this matrix, where each row represents Python, Data Analytics, and AI marks for one student:

# ```python
# [[85, 78, 90],
#  [92, 88, 95],
#  [76, 82, 80]]
# ```


# Print the average mark for each student using NumPy.

# ```python
# # Expected Output:
# # [84.33 91.67 79.33]
# ```
import numpy as np

student_marks = np.array([
    [85, 78, 90],
    [92, 88, 95],
    [76, 82, 80]
])

average_marks = student_marks.mean(axis=1)

print(np.round(average_marks, 2))


