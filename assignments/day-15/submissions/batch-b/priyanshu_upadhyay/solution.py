# Day 15 Assignment - Applied K-Means Customer Segmentation

import joblib
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score

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
df = pd.DataFrame(customer_data)
print("=== Question 1 ===")
print(df.head())
print("Shape:", df.shape)
print("Columns:", list(df.columns))
print("Missing values:\n", df.isnull().sum())

# Question 2: Select the Clustering Features
# customer_id is just an identifier, not a meaningful feature.
# Using it would mislead the model into treating ID numbers as data.
X = df[["annual_income", "spending_score"]]
print("\n=== Question 2 ===")
print(X.head())

# Question 3: Use the Elbow Method
print("\n=== Question 3 ===")
inertias = []
for k in range(1, 8):
    km = KMeans(n_clusters=k, random_state=42, n_init=10)
    km.fit(X)
    inertias.append(km.inertia_)
    print(f"k={k}, Inertia: {round(km.inertia_, 2)}")

plt.plot(range(1, 8), inertias, marker="o")
plt.xlabel("Number of Clusters (k)")
plt.ylabel("Inertia")
plt.title("Elbow Curve")
plt.grid(True)
plt.tight_layout()
plt.savefig("elbow_curve.png")
plt.close()
print("elbow_curve.png saved")

# Question 4: Train the Final K-Means Model
# Cluster numbers 0, 1, 2 are just identifiers, not rankings.
# Cluster 2 is not better than cluster 0.
print("\n=== Question 4 ===")
model = KMeans(n_clusters=3, random_state=42, n_init=10)
df["cluster"] = model.fit_predict(X)
print(df)
print("\nCustomers per cluster:")
print(df["cluster"].value_counts().sort_index())

# Question 5: Inspect the Centroids
print("\n=== Question 5 ===")
centroids = model.cluster_centers_
for i, c in enumerate(centroids):
    print(f"Cluster {i}: Income = {round(c[0], 2)}, Spending = {round(c[1], 2)}")

# Question 6: Visualize Clusters and Centroids
print("\n=== Question 6 ===")
scatter = plt.scatter(df["annual_income"], df["spending_score"],
                      c=df["cluster"], cmap="viridis")
plt.scatter(centroids[:, 0], centroids[:, 1],
            c="red", marker="X", s=200, label="Centroids")
plt.xlabel("Annual Income")
plt.ylabel("Spending Score")
plt.title("Customer Clusters")
plt.colorbar(scatter, label="Cluster")
plt.legend()
plt.tight_layout()
plt.savefig("customer_clusters.png")
plt.close()
print("customer_clusters.png saved")

# Question 7: Calculate the Silhouette Score
# A higher silhouette score means points are closer to their own cluster
# and farther from other clusters - indicating better-defined clusters.
print("\n=== Question 7 ===")
score = silhouette_score(X, df["cluster"])
print("Silhouette Score:", round(score, 3))

# Question 8: Business Insights
print("\n=== Question 8 ===")
summary = df.groupby("cluster")[["annual_income", "spending_score"]].mean()
print(summary)

high_spend_cluster = summary["spending_score"].idxmax()
high_income_cluster = summary["annual_income"].idxmax()
low_spend_cluster = summary["spending_score"].idxmin()

print(f"\nHighest spending cluster: {high_spend_cluster} - These customers spend the most.")
print(f"Highest income cluster: {high_income_cluster} - These customers earn the most.")
print(f"Discount offers cluster: {low_spend_cluster} - Low spenders may respond well to discounts.")
print(f"Premium membership cluster: {high_spend_cluster} - High spenders are ideal for premium offers.")

# Question 9: Export the Model
print("\n=== Question 9 ===")
joblib.dump(model, "kmeans_model.pkl")
print("Model saved as kmeans_model.pkl")