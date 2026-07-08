import numpy as np

# Each row contains: [annual_income, spending_score]
customers = np.array([
    [15, 20],
    [80, 85],
    [45, 50],
    [18, 25],
    [75, 90],
    [48, 45],
])

# Question 1: Understand the Data
print("Customer Array:")
print(customers)
print("Shape:", customers.shape)
print("Total customers:", len(customers))
# This is unsupervised learning because no customer group labels are provided.
# The algorithm must find patterns and groupings on its own without any guidance.

# Question 2: Calculate a Centroid
group = np.array([
    [20, 30],
    [30, 40],
    [40, 50],
])
centroid = np.mean(group, axis=0)
print("\nCentroid:", centroid)

# Question 3: Initial Centroids and Customer P
centroid_a = np.array([20, 20])
centroid_b = np.array([80, 85])
customer_p = np.array([18, 25])
print("\nCentroid A:", centroid_a)
print("Centroid B:", centroid_b)
print("Customer P:", customer_p)

# Question 4: Euclidean Distance Function
def euclidean_distance(point_a, point_b):
    return np.sqrt(np.sum((point_a - point_b) ** 2))

dist_a = euclidean_distance(customer_p, centroid_a)
dist_b = euclidean_distance(customer_p, centroid_b)
print("\nDistance from Customer P to Centroid A:", round(dist_a, 2))
print("Distance from Customer P to Centroid B:", round(dist_b, 2))

# Question 5: Assign Customer P
if dist_a < dist_b:
    print("\nCustomer P belongs to Cluster A")
else:
    print("\nCustomer P belongs to Cluster B")

# Question 6: Assign Every Customer
cluster_a = []
cluster_b = []

for customer in customers:
    da = euclidean_distance(customer, centroid_a)
    db = euclidean_distance(customer, centroid_b)
    if da < db:
        cluster_a.append(customer)
    else:
        cluster_b.append(customer)

cluster_a = np.array(cluster_a)
cluster_b = np.array(cluster_b)
print("\nCluster A:")
print(cluster_a)
print("Cluster B:")
print(cluster_b)

# Question 7: Recalculate the Centroids
new_centroid_a = np.mean(cluster_a, axis=0)
new_centroid_b = np.mean(cluster_b, axis=0)
print("\nNew Centroid A:", np.round(new_centroid_a, 2))
print("New Centroid B:", np.round(new_centroid_b, 2))

# Question 8: Explain the K-Means Cycle
# Step 1: Find the nearest centroid - calculate distance from each point to all centroids
# Step 2: Assign points to groups - each point joins the group of its nearest centroid
# Step 3: Calculate each group's new average - find the mean of all points in each group
# Step 4: Move the centroids - update centroid positions to the new averages
# Step 5: Repeat until the groups stop changing - keep iterating until assignments are stable

print("\nThe algorithm may need several rounds because moving centroids changes cluster assignments, which then changes the centroids again, repeating until everything stabilizes.")