import numpy as np

# Use this customer data:
# # Each row contains: [annual_income, spending_score]
customers = np.array([
    [15, 20],
    [80, 85],
    [45, 50],
    [18, 25],
    [75, 90],
    [48, 45],
])

# ### Question 1: Understand the Data
# Print the customer array, its shape, and the total number of customers.
print(customers)
print("Shape:", customers.shape)
print("Total Customers:", customers.shape[0])

# In a comment, explain why this is an unsupervised-learning problem when no customer group labels are supplied.
# This is an unsupervised learning problem because no customer group labels are provided. The algorithm finds similar groups based on the data itself.



# ### Question 2: Calculate a Centroid
# Use this group:
group = np.array([
    [20, 30],
    [30, 40],
    [40, 50],
])
# Calculate its centroid using the mean of each column. Print the centroid.
centroid = np.mean(group, axis=0)
# Expected value:
print(centroid)


# ### Question 3: Initial Centroids and Customer P
# Create:
centroid_a = np.array([20, 20])
centroid_b = np.array([80, 85])
customer_p = np.array([18, 25])

# Print all three arrays.
print("Centroid A:", centroid_a)
print("Centroid B:", centroid_b)
print("Customer P:", customer_p)

# ### Question 4: Euclidean Distance Function
# Write this function:
def euclidean_distance(point_a, point_b):
    return np.sqrt(np.sum((point_a - point_b) ** 2))

# Use it to calculate the distance from `customer_p` to `centroid_a` and `centroid_b`. Print both distances rounded to two decimal places.
distance_a = euclidean_distance(customer_p, centroid_a)
distance_b = euclidean_distance(customer_p, centroid_b)
print("Distance from Centroid A:", round(distance_a, 2))
print("Distance from Centroid B:", round(distance_b, 2))


# ### Question 5: Assign Customer P
# Compare the two distances from Question 4.
# Print:
# Customer P belongs to Cluster A
# or:
# Customer P belongs to Cluster B
# Use an `if` statement instead of writing the answer directly.
if distance_a < distance_b:
    print("Customer P belongs to Cluster A")
else:
    print("Customer P belongs to Cluster B")


# ### Question 6: Assign Every Customer
# For every row in `customers`:
cluster_a = []
cluster_b = []

# 1. calculate its distance from `centroid_a`;
# 2. calculate its distance from `centroid_b`;
# 3. add it to `cluster_a` or `cluster_b`, depending on the smaller distance.
for customer in customers:
    distance_a = euclidean_distance(customer, centroid_a)
    distance_b = euclidean_distance(customer, centroid_b)

    if distance_a < distance_b:
        cluster_a.append(customer)
    else:
        cluster_b.append(customer)
# Convert both cluster lists to NumPy arrays and print them.
cluster_a = np.array(cluster_a)
cluster_b = np.array(cluster_b)

print("Cluster A:", cluster_a)
print("Cluster B:", cluster_b)


# ### Question 7: Recalculate the Centroids
# Calculate and print the new centroid of `cluster_a` and `cluster_b` using:
new_centroid_a = np.mean(cluster_a, axis=0)
new_centroid_b = np.mean(cluster_b, axis=0)

# Print each new centroid rounded to two decimal places.
print("New Centroid A:", np.round(new_centroid_a, 2))
print("New Centroid B:", np.round(new_centroid_b, 2))



# ### Question 8: Explain the K-Means Cycle
# At the bottom of `solution.py`, add comments explaining these steps in your own words:

# ```text
# Find the nearest centroid
# Assign points to groups
# Calculate each group's new average
# Move the centroids
# Repeat until the groups stop changing
# ```
# Step 1: Find the nearest centroid.
# Step 2: Assign each data point to the nearest cluster.
# Step 3: Calculate the new centroid using the average of each cluster.
# Step 4: Move the centroids to the new positions.
# Step 5: Repeat the process until the clusters stop changing.

# Also print one sentence explaining why the algorithm may need several rounds.
print("K-Means may need several rounds because the centroids keep changing until the clusters become stable.")
