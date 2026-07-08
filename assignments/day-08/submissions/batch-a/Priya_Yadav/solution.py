import numpy as np
# 1. Creating a array
arr=np.array([[85, 90, 78, 92, 88]])
# 2. Printing shape and size
print("Shape:",arr.shape)
print("Size:",arr.size)
# 3. Printing total, average, maximum, and minimum.
print("Total:",arr.sum())
print("Average::",arr.mean())
print("Maximum:",arr.max())
print("Minimum:",arr.min())
# 4. Creating 2D arrray
arr2=np.array([[10, 20, 30],
             [40, 50, 60]])
print(arr2)
# 5. Slicing in 2D array
print(arr2[1][1])
print(arr2[0])
# 6. Element-Wise Operations
numbers = np.array([1, 2, 3, 4, 5])
print(numbers*10)
# 7. Filter Values
marks_array=np.array([80,90,67,92,45])
list1=[]
for i in marks_array:
    if i>=90:   
       list1.append(i)
new_mark=np.array(list1)
print(new_mark)
# 8. Student Marks Matrix
student_mark_matrix=np.array([
    [85, 78, 90],
    [92, 88, 95],
    [76, 82, 80]])
print(student_mark_matrix)

average=np.round(np.mean(student_mark_matrix,axis=1),2)
print(average)