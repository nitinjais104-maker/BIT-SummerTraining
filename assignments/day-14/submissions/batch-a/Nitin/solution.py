import numpy as np

# Customer Data
customers = np.array([
    [15, 20],
    [80, 85],
    [45, 50],
    [18, 25],
    [75, 90],
    [48, 45],
])

# ===========================
# Question 1
# ===========================
print("Question 1")
print(customers)
print("Shape:", customers.shape)
print("Total customers:", len(customers))

# This is an unsupervised learning problem because no customer group labels are given.

# ===========================
# Question 2
# ===========================
print("\nQuestion 2")

group = np.array([
    [20, 30],
    [30, 40],
    [40, 50],
])

centroid = np.mean(group, axis=0)
print("Centroid:", centroid)

# ===========================
# Question 3
# ===========================
print("\nQuestion 3")

centroid_a = np.array([20, 20])
centroid_b = np.array([80, 85])
customer_p = np.array([18, 25])

print("Centroid A:", centroid_a)
print("Centroid B:", centroid_b)
print("Customer P:", customer_p)

# ===========================
# Question 4
# ===========================
print("\nQuestion 4")

def euclidean_distance(point_a, point_b):
    return np.sqrt(np.sum((point_a - point_b) ** 2))

distance_a = euclidean_distance(customer_p, centroid_a)
distance_b = euclidean_distance(customer_p, centroid_b)

print("Distance to Cluster A:", round(distance_a, 2))
print("Distance to Cluster B:", round(distance_b, 2))

# ===========================
# Question 5
# ===========================
print("\nQuestion 5")

if distance_a < distance_b:
    print("Customer P belongs to Cluster A")
else:
    print("Customer P belongs to Cluster B")

# ===========================
# Question 6
# ===========================
print("\nQuestion 6")

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

print("Cluster B:")
print(cluster_b)

# ===========================
# Question 7
# ===========================
print("\nQuestion 7")

new_centroid_a = np.mean(cluster_a, axis=0)
new_centroid_b = np.mean(cluster_b, axis=0)

print("New Centroid A:", np.round(new_centroid_a, 2))
print("New Centroid B:", np.round(new_centroid_b, 2))

# ===========================
# Question 8
# ===========================
print("\nQuestion 8")

print("K-Means repeats the process until the clusters stop changing.")

# Step 1: Find the nearest centroid.
# Step 2: Assign each point to the nearest group.
# Step 3: Calculate the new average (centroid) of each group.
# Step 4: Move the centroids to the new positions.
# Step 5: Repeat until the clusters no longer change.