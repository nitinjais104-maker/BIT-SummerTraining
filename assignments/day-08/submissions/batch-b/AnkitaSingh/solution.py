
import numpy as np

### Question 1: Create a NumPy Array
arr = np.array([85, 90, 78, 92, 88])
print(arr)

### Question 2: Array Shape and Size
print("Shape:", arr.shape)
print("Size:", arr.size)


### Question 3: Basic Calculations
print("Total:",np.sum(arr))
print("Average:",np.mean(arr))
print("Maximum:",np.max(arr))
print("Minimum:",np.min(arr))

### Question 4: Create a 2D Array
arr_2nd = np.array([[10, 20, 30],
 [40, 50, 60]])
print(arr_2nd)

### Question 5: Indexing and Slicing
print(arr_2nd[1][1]) 
print(arr_2nd[0])

### Question 6: Element-Wise Operations
numbers = np.array([1, 2, 3, 4, 5])
print(numbers*10)

### Question 7: Filter Values
marks_array =np.array([67,87,90,75,92])
print(marks_array[marks_array >= 90])


### Question 8: Student Marks Matrix
matrix = np.array([[85, 78, 90],
 [92, 88, 95],
 [76, 82, 80]])
average_marks = np.mean(matrix, axis=1)
print(np.round(average_marks, 2))