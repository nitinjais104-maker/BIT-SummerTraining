
import joblib
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score
# Use this dataset:
customer_data = {
    "customer_id": list(range(1, 22)),
    "annual_income": [
        15, 18, 16, 22, 19, 14, 20,
        44, 48, 46, 52, 49, 45, 50,
        78, 82, 80, 88, 85, 76, 90,
    ],
    "spending_score": [
        20, 25, 18, 30, 22, 15, 28,
        48, 52, 50, 58, 55, 46, 53,
        82, 88, 78, 90, 85, 80, 92,
    ],
}

# Question 1: Load and Inspect the Data
# Create a DataFrame named df from customer_data.
# Print:
# the first five rows;
# the DataFrame shape;
# the column names;
# the missing-value count for each column.
df = pd.DataFrame(customer_data)
print("First Five Rows")
print(df.head())
print("\nDataFrame Shape:")
print(df.shape)
print("\nColumn Names:")
print(df.columns.tolist())
print("\nMissing Values:")
print(df.isnull().sum()) 

# Question 2: Select the Clustering Features
# Create:
# X = df[["annual_income", "spending_score"]]
# Print the first five rows of X.
# In a comment, explain why customer_id should not be used as a clustering feature.
X = df[["annual_income", "spending_score"]]
print("\nFirst Five Rows of X")
print(X.head())
# customer_id is only a unique identifier.
# It does not describe customer behaviour, so it should not
# be included as a clustering feature.


# Question 3: Use the Elbow Method
# For every value of k from 1 to 7:
# create KMeans(n_clusters=k, random_state=42, n_init=10);
# train it with X;
# add its inertia_ value to a list named inertias.
# Print each k and inertia value rounded to two decimal places.
# Plot the inertia values against k using markers, axis labels, a title, and a grid. Save the chart as:
# elbow_curve.png
# Use plt.tight_layout() and plt.close() after saving.

inertias = []

print("\nElbow Method Results")

for k in range(1, 8):
    kmeans = KMeans(
        n_clusters=k,
        random_state=42,
        n_init=10
    )

    kmeans.fit(X)

    inertias.append(kmeans.inertia_)

    print(f"k = {k}, Inertia = {kmeans.inertia_:.2f}")

plt.figure(figsize=(7, 5))
plt.plot(range(1, 8), inertias, marker="o")
plt.title("Elbow Method")
plt.xlabel("Number of Clusters (k)")
plt.ylabel("Inertia")
plt.grid(True)
plt.tight_layout()
plt.savefig("elbow_curve.png")
plt.close()


# Question 4: Train the Final K-Means Model
# Use three clusters:
# model = KMeans(n_clusters=3, random_state=42, n_init=10)
# df["cluster"] = model.fit_predict(X)
# Print the complete DataFrame and the number of customers in each cluster.
# Add a comment explaining why cluster numbers such as 0, 1, and 2 are identifiers rather than rankings.

model = KMeans(
    n_clusters=3,
    random_state=42,
    n_init=10
)

df["cluster"] = model.fit_predict(X)
print("\nComplete DataFrame")
print(df)
print("\nCustomers in Each Cluster")
print(df["cluster"].value_counts().sort_index())
# Cluster numbers (0, 1, 2, etc.) are only labels assigned by
# the algorithm. They do not represent rankings or quality levels.

# Question 5: Inspect the Centroids
# Get the cluster centres using:
# centroids = model.cluster_centers_
# Print the centroids rounded to two decimal places. Clearly label the income and spending values in your output.
centroids = model.cluster_centers_

print("\nCluster Centroids")

for i, centroid in enumerate(centroids):
    print(
        f"Cluster {i}: "
        f"Annual Income = {centroid[0]:.2f}, "
        f"Spending Score = {centroid[1]:.2f}"
    )


# Question 6: Visualize Clusters and Centroids
# Create a scatter plot with:
# annual income on the x-axis;
# spending score on the y-axis;
# customer points coloured by cluster;
# centroids shown as large red X markers;
# a title, axis labels, colour bar, and centroid legend.
# Save it as:
# customer_clusters.png
# Use plt.tight_layout() and plt.close() after saving.
plt.figure(figsize=(8, 6))

scatter = plt.scatter(
    df["annual_income"],
    df["spending_score"],
    c=df["cluster"],
    cmap="viridis",
    s=70
)

plt.scatter(
    centroids[:, 0],
    centroids[:, 1],
    color="red",
    marker="X",
    s=250,
    label="Centroids"
)
plt.title("Customer Clusters")
plt.xlabel("Annual Income")
plt.ylabel("Spending Score")
plt.colorbar(scatter, label="Cluster")
plt.legend()
plt.tight_layout()
plt.savefig("customer_clusters.png")
plt.close()

# Question 7: Calculate the Silhouette Score
# Calculate:
# score = silhouette_score(X, df["cluster"])
# Print the score rounded to three decimal places.
# In a comment, explain that a higher silhouette score generally means points are closer to their own cluster and farther from other clusters.
score = silhouette_score(X, df["cluster"])
print(f"\nSilhouette Score: {score:.3f}")
# A higher silhouette score generally indicates that points are
# closer to their own cluster and farther away from other clusters.


# Question 8: Produce Business Insights
# Group the DataFrame by cluster and calculate the average annual income and spending score for each cluster.
# Print the summary table, then identify:
# the cluster with the highest average spending score;
# the cluster with the highest average income;
# a cluster that could receive discount offers;
# a cluster that could receive premium-membership offers.
# Print one short reason for each marketing choice. Derive the cluster numbers from the summary instead of assuming a fixed label.
summary = (
    df.groupby("cluster")[["annual_income", "spending_score"]]
    .mean()
    .round(2)
)

print("\nCluster Summary")
print(summary)

highest_spending_cluster = summary["spending_score"].idxmax()
highest_income_cluster = summary["annual_income"].idxmax()
lowest_spending_cluster = summary["spending_score"].idxmin()

print("\nBusiness Insights")

print(
    f"Cluster with highest average spending score: "
    f"{highest_spending_cluster}"
)

print(
    f"Cluster with highest average income: "
    f"{highest_income_cluster}"
)

print(
    f"Cluster recommended for discount offers: "
    f"{lowest_spending_cluster}"
)
print(
    "Reason: This group has the lowest average spending score, "
    "so discounts may encourage more purchases."
)

print(
    f"Cluster recommended for premium membership: "
    f"{highest_income_cluster}"
)
print(
    "Reason: This group has the highest average income and is "
    "more likely to purchase premium products or services."
)

# Question 9: Export the Model
# Save the trained model:
# joblib.dump(model, "kmeans_model.pkl")
# Print:
# Model saved as kmeans_model.pkl
joblib.dump(model, "kmeans_model.pkl")
print("\nModel saved as kmeans_model.pkl")