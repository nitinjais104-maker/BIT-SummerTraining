
import numpy as np

### Question 1: Create a NumPy Array

marks = np.array([85, 90, 78, 92, 88])
print(marks)


### Question 2: Array Shape and Size

print(f"Sape:{marks.shape}")
print(f"Size:{marks.size}")

### Question 3: Basic Calculations
total = sum(marks)
average = total/ len(marks)
maximum = max(marks)
minimum = min(marks)
print("Total:",total)
print("Average:",average)
print("Maximum:",maximum)
print("Minimum:",minimum)


### Question 4: Create a 2D Array

arr = np.array([[10, 20, 30],
               [40, 50, 60]])
print(arr)

### Question 5: Indexing and Slicing

print(arr[1,1])
print(arr[0])

### Question 6: Element-Wise Operations

numbers = np.array([1, 2, 3, 4, 5])
print(numbers*10)


### Question 7: Filter Values

marks = np.array([50,55,60,65,72,77,80,66,90,92])
values = marks[marks>=90]
print(values)

### Question 8: Student Marks Matrix

marks = np.array([[85, 78, 90],
 [92, 88, 95],
 [76, 82, 80]])
average = np.round(np.mean(marks,axis=1),2)
print(average)