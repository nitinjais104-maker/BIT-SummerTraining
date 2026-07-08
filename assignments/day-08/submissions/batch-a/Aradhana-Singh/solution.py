# ### Question 1: Create a NumPy Array
# Create a one-dimensional NumPy array containing these marks and print it: [85, 90, 78, 92, 88]
import numpy as np
num_array = np.array([85, 90, 78,92, 88])
print(num_array)


# ### Question 2: Array Shape and Size
# Print the shape and total number of elements in the array from Question 1.
# # Expected Output:
# # Shape: (5,)
# # Size: 5
print("Shape:",num_array.shape)
print("Size:", num_array.size)


# ### Question 3: Basic Calculations
# Using the marks array, print the total, average, maximum, and minimum
# # Expected Output:
# # Total: 433
# # Average: 86.6
# # Maximum: 92
# # Minimum: 78
total_num = np.sum(num_array)
avg_num = np.mean(num_array)
max_num = np.max(num_array)
min_array = np.min(num_array)
print("Total:", total_num)
print("Average:", avg_num)
print("Maximum:", max_num)
print("Minimum:", min_array)


# ### Question 4: Create a 2D Array
# Create this 2D NumPy array and print it:
# [[10, 20, 30],
#  [40, 50, 60]]
arr = np.array([[10,20,30],[40,50,60]])
print(arr)


# ### Question 5: Indexing and Slicing
# From the 2D array in Question 4, print the value `50` and then print the first row.
# # Expected Output:
# # 50
# # [10 20 30]
print(arr[1][1])
print(arr[0])


# ### Question 6: Element-Wise Operations
# Create `numbers = np.array([1, 2, 3, 4, 5])`. Print the result of multiplying every element by 10.
# # Expected Output:  [10 20 30 40 50]
numbers = np.array([1, 2, 3 , 4 , 5])
print(10*numbers)


# ### Question 7: Filter Values
# Using the marks array, create and print a new array containing marks greater than or equal to 90.
# # Expected Output:  [90 92]
filtered_marks = num_array[num_array >= 90]
print(filtered_marks)


# ### Question 8: Student Marks Matrix
# Create this matrix, where each row represents Python, Data Analytics, and AI marks for one student:
# [[85, 78, 90],
#  [92, 88, 95],
#  [76, 82, 80]]
marks = np.array([[85, 78, 90],[92, 88, 95],[76, 82, 80]])
print(marks)


# Print the average mark for each student using NumPy.
# # Expected Output:  [84.33 91.67 79.33]
avg_marks = np.round(np.mean(marks, axis =1),2)
print(avg_marks)

