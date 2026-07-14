import numpy as np
# Use this customer data --
# Each row contains: [annual_income, spending_score]
customers = np.array([
    [15, 20],
    [80, 85],
    [45, 50],
    [18, 25],
    [75, 90],
    [48, 45],
])

### Question 1: Understand the Data

"""Print the customer array, its shape, and the total number of customers.

In a comment, explain why this is an unsupervised-learning problem when no customer group labels are supplied."""
print(customers)
print("Shape:", customers.shape)
print("Total Customers:", len(customers))
# This is an unsupervised learning problem because no customer group labels are provided. The algorithm must discover groups by itself.

### Question 2: Calculate a Centroid

"""Use this group:

```python
group = np.array([
    [20, 30],
    [30, 40],
    [40, 50],
])
```

Calculate its centroid using the mean of each column. Print the centroid.

Expected value:

```text
[30. 40.]
```"""
group = np.array([
    [20, 30],
    [30, 40],
    [40, 50],
])

centroid = np.mean(group, axis=0)

print("Centroid of Group:")
print(centroid)

### Question 3: Initial Centroids and Customer P

"""Create:

```python
centroid_a = np.array([20, 20])
centroid_b = np.array([80, 85])
customer_p = np.array([18, 25])
```

Print all three arrays."""
centroid_a = np.array([20, 20])
centroid_b = np.array([80, 85])
customer_p = np.array([18, 25])

print("Centroid A:", centroid_a)
print("Centroid B:", centroid_b)
print("Customer P:", customer_p)

### Question 4: Euclidean Distance Function

"""Write this function:

```python
def euclidean_distance(point_a, point_b):
    return np.sqrt(np.sum((point_a - point_b) ** 2))
```

Use it to calculate the distance from `customer_p` to `centroid_a` and `centroid_b`. Print both distances rounded to two decimal places."""
def euclidean_distance(point_a, point_b):
    return np.sqrt(np.sum((point_a - point_b) ** 2))

distance_a = euclidean_distance(customer_p, centroid_a)
distance_b = euclidean_distance(customer_p, centroid_b)

print("Distance to Cluster A:", round(distance_a, 2))
print("Distance to Cluster B:", round(distance_b, 2))

### Question 5: Assign Customer P

"""Compare the two distances from Question 4.

Print:

```text
Customer P belongs to Cluster A
```

or:

```text
Customer P belongs to Cluster B"""
if distance_a < distance_b:
    print("Customer P belongs to Cluster A")
else:
    print("Customer P belongs to Cluster B")

### Question 6: Assign Every Customer

"""For every row in `customers`:

1. calculate its distance from `centroid_a`;
2. calculate its distance from `centroid_b`;
3. add it to `cluster_a` or `cluster_b`, depending on the smaller distance.

Convert both cluster lists to NumPy arrays and print them."""
cluster_a = []
cluster_b = []

for customer in customers:
    d1 = euclidean_distance(customer, centroid_a)
    d2 = euclidean_distance(customer, centroid_b)

    if d1 < d2:
        cluster_a.append(customer)
    else:
        cluster_b.append(customer)

cluster_a = np.array(cluster_a)
cluster_b = np.array(cluster_b)

print("Cluster A:")
print(cluster_a)

print("\nCluster B:")
print(cluster_b)

### Question 7: Recalculate the Centroids

"""Calculate and print the new centroid of `cluster_a` and `cluster_b` using:

```python
new_centroid_a = np.mean(cluster_a, axis=0)
new_centroid_b = np.mean(cluster_b, axis=0)
```

Print each new centroid rounded to two decimal places."""
new_centroid_a = np.mean(cluster_a, axis=0)
new_centroid_b = np.mean(cluster_b, axis=0)

print("New Centroid A:", np.round(new_centroid_a, 2))
print("New Centroid B:", np.round(new_centroid_b, 2))

### Question 8: Explain the K-Means Cycle

"""At the bottom of `solution.py`, add comments explaining these steps in your own words:

```text
Find the nearest centroid--
# Calculate the distance from each data point to every centroid.
Assign points to groups--
# Put each data point into the cluster with the nearest centroid.
Calculate each group's new average--
# Find the average of all points in each cluster. This average becomes the new centroid.
Move the centroids--
# Update the centroid positions to these new averages.
Repeat until the groups stop changing--
# Keep repeating the above steps until no data points change clusters.
```

Also print one sentence explaining why the algorithm may need several rounds."""
print("K-Means may need several rounds because the centroids keep moving until the clusters become stable.")


