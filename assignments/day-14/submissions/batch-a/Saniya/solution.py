# Day 14 Assignment
#==========================================================>>>
import numpy as np
#Use this customer data:
# Each row contains: [annual_income, spending_score]
customers = np.array([
    [15, 20],
    [80, 85],
    [45, 50],
    [18, 25],
    [75, 90],
    [48, 45],
])
#=========================================================>>>
# Question 1: Understand the Data
# Print the customer array, its shape, and the total number of customers.
# In a comment, explain why this is an unsupervised-learning problem when no customer group labels are supplied.
print("\nCustomer Data:")
print(customers)
print("\nShape of Customer Data:")
print(customers.shape)
print("\nTotal Number of Customers")
print(len(customers))
# This is an unsupervised learning problem because
# customer group labels are not provided.
# The algorithm finds hidden patterns and creates
# clusters using only the available customer data.
print("=" * 50)
#=========================================================>>>
# ## Question 2: Calculate a Centroid
# Use this group:
group = np.array([
    [20, 30],
    [30, 40],
    [40, 50],
])
centroid = np.mean(group, axis=0)
print("\nCentroid of the Group:")
print(centroid)
print("=" * 50)
#========================================================>>>
# Question 3: Initial Centroids and Customer P
centroid_a = np.array([20, 20])
centroid_b = np.array([80, 85])
customer_p = np.array([18, 25])
print("Centroid A:", centroid_a)
print("Centroid B:", centroid_b)
print("Customer P:", customer_p)
print("=" * 50)
#========================================================>>>
# Question 4: Euclidean Distance Function
# Write this function:
# ```python
# def euclidean_distance(point_a, point_b):
#return np.sqrt(np.sum((point_a - point_b) ** 2))
# Use it to calculate the distance from `customer_p` to `centroid_a` and `centroid_b`. Print both distances rounded to two decimal places.
centroid_a = np.array([20, 20])
centroid_b = np.array([80, 85])
customer_p = np.array([18, 25])
def euclidean_distance(point_a, point_b):
    return np.sqrt(np.sum((point_a - point_b) ** 2))
d1 = euclidean_distance(customer_p, centroid_a)
d2 = euclidean_distance(customer_p, centroid_b)
print("Distance to Centroid A:", round(d1, 2))
print("Distance to Centroid B:", round(d2, 2))
print("=" * 50)
#=========================================================>>>
# Question 5: Assign Customer P
# Compare the two distances from Question 4.
if d1 < d2:
    print("Customer P belongs to Cluster A")
else:
    print("Customer P belongs to Cluster B")
print("=" * 50)
#=========================================================>>>
# Question 6: Assign Every Customer

# For every row in `customers`:

# 1. calculate its distance from `centroid_a`;
# 2. calculate its distance from `centroid_b`;
# 3. add it to `cluster_a` or `cluster_b`, depending on the smaller distance.

# Convert both cluster lists to NumPy arrays and print them.
cluster_a = []
cluster_b = []

for c in customers:
    d1 = euclidean_distance(c, centroid_a)
    d2 = euclidean_distance(c, centroid_b)

    if d1 < d2:
        cluster_a.append(c)
    else:
        cluster_b.append(c)

print("Cluster A:")
print(np.array(cluster_a))
print("Cluster B:")
print(np.array(cluster_b))
print("=" * 50)
#=========================================================>>>
# Question 7: Recalculate the Centroids
# Calculate and print the new centroid of `cluster_a` and `cluster_b` using:
# ```python
# new_centroid_a = np.mean(cluster_a, axis=0)
# new_centroid_b = np.mean(cluster_b, axis=0)
# Print each new centroid rounded to two decimal places.
new_centroid_a = np.mean(cluster_a, axis=0)
new_centroid_b = np.mean(cluster_b, axis=0)
print("New Centroid A:", np.round(new_centroid_a, 2))
print("New Centroid B:", np.round(new_centroid_b, 2))   
print("=" * 50)
#=========================================================>>>
# Question 8:
#  Explain the K-Means Cycle

# Customer Data
#       |
# Calculate Distances
#       |
# Find Nearest Centroid
#       |
# Assign Customers to Clusters
#       |
# Calculate New Average
#       |
# Update Centroids
#       |
# Repeat Process
#       |
# Stable Clusters Obtained

# K-Means Steps
#---------------------
# 1. Find the nearest centroid.
# 2. Assign points to the nearest group.
# 3. Calculate the new average of each group.
# 4. Move the centroids to the new averages.
# 5. Repeat until the groups do not change.


#Also print one sentence explaining why the algorithm may need several rounds.
print("K-Means may need several rounds because the centroids keep changing until they become stable.")
print("=" * 50)
#=========================================================>>>