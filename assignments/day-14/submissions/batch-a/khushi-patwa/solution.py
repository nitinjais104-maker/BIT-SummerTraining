# Topic: Unsupervised Learning and K-Means Fundamentals

import numpy as np
customers = np.array([
    [15, 20],
    [80, 85],
    [45, 50],
    [18, 25],
    [75, 90],
    [48, 45],
])

# (Ques 1) Understand the Data

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

# (Ques 2) Calculate a Centroid

group = np.array([
    [20, 30],
    [30, 40],
    [40, 50],
])

centroid = np.mean(group, axis=0)

print("\nCentroid of the Group:")
print(centroid) 

print("=" * 50)

# (Ques 3) Initial Centroids and Customer P
centroid_a = np.array([20, 20])

centroid_b = np.array([80, 85])

customer_p = np.array([18, 25])

print("\nCentroid A:")
print(centroid_a)

print("\nCentroid B:")
print(centroid_b)

print("\nCustomer P:")
print(customer_p)

print("=" * 50)

# (Ques 4) Euclidean Distance Function

def euclidean_distance(point_a, point_b):
    return np.sqrt(np.sum((point_a - point_b) ** 2))


distance_a = euclidean_distance(
    customer_p,
    centroid_a
)

distance_b = euclidean_distance(
    customer_p,
    centroid_b
)

print("\nDistance from Centroid A:")
print(round(distance_a, 2))

print("\nDistance from Centroid B:")
print(round(distance_b, 2))

print("=" * 50)

# (Ques 5) Assign Customer P

if distance_a < distance_b:

    print("\nCustomer P belongs to Cluster A")

else:

    print("\nCustomer P belongs to Cluster B")

print("=" * 50)

# (Ques 6) Assign Every Customer

cluster_a = []
cluster_b = []
for customer in customers:

    d1 = euclidean_distance(
        customer,
        centroid_a
    )

    d2 = euclidean_distance(
        customer,
        centroid_b
    )

    if d1 < d2:

        cluster_a.append(customer)

    else:

        cluster_b.append(customer)

cluster_a = np.array(cluster_a)
cluster_b = np.array(cluster_b)
print("\nCluster A:")
print(cluster_a)
print("\nCluster B:")
print(cluster_b)

print("=" * 50)

# (Ques 7) Recalculate the Centroids

new_centroid_a = np.mean(
    cluster_a,
    axis=0
)
new_centroid_b = np.mean(
    cluster_b,
    axis=0
)
print("\nNew Centroid A:")
print(np.round(new_centroid_a, 2))
print("\nNew Centroid B:")
print(np.round(new_centroid_b, 2))

print("=" * 50)

# (Ques 8) K-Means Cycle

# K-Means Flowchart
#
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

# Step 1
# Find the nearest centroid for every customer.

# Step 2
# Assign each customer to the closest cluster.

# Step 3
# Calculate the new average position of every cluster.

# Step 4
# Move the centroid to its updated location.

# Step 5
# Repeat the process until cluster assignments stop changing.

print(
    "K-Means may require several iterations because centroids keep updating until stable clusters are formed."
)
