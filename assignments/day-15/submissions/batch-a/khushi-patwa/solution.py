## Topic: Applied K-Means Customer Segmentation

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

### Question 1: Load and Inspect the Data
df = pd.DataFrame(customer_data)
print("First Five Rows:")
print(df.head(5))

print("\nDataFrame Shape:")
print(df.shape)

print("\nColumn Names:")
print(df.columns.tolist())

print("\nMissing Values:")
print(df.isnull().sum())


print("="*45)

### Question 2: Select the Clustering Features

X = df[["annual_income", "spending_score"]]
print("First Five Rows of X :")
print(X.head())

# customer_id is only a unique identifier.
# It does not represent customer behaviour,
# therefore it should not be used for clustering.

print("="*45)

### Question 3: Use the Elbow Method

print("Elbow Method :")

inertias = []

for k in range(1, 8):
    model = KMeans(
        n_clusters=k,
        random_state=42,
        n_init=10
    )

    model.fit(X)
    inertias.append(model.inertia_)

plt.figure(figsize=(7, 5))
plt.plot(range(1, 8), inertias, marker="o", linewidth=2)
plt.title("Elbow Method")
plt.xlabel("Number of Clusters (k)")
plt.ylabel("Inertia")
plt.grid(True)

plt.tight_layout()
plt.savefig("elbow_curve.png")
plt.close()

print("="*45)

### Question 4: Train the Final K-Means Model

print("Final KMeans Model")
model = KMeans(
    n_clusters=3,
    random_state=42,
    n_init=10
)

df["cluster"] = model.fit_predict(X)

print(df)

print("\nCustomers in each Cluster")
print(df["cluster"].value_counts())

# Cluster numbers (0,1,2) are only labels assigned by KMeans.
# They are identifiers and NOT rankings.

print("="*45)

### Question 5: Inspect the Centroids

print("Cluster Centroids")
centroids = model.cluster_centers_

for i, centroid in enumerate(centroids):
    print(
        f"Cluster {i}: "
        f"Income = {centroid[0]:.2f}, "
        f"Spending = {centroid[1]:.2f}"
    )

print("="*45)

### Question 6: Visualize Clusters and Centroids

plt.figure(figsize=(8, 6))

scatter = plt.scatter(
    df["annual_income"],
    df["spending_score"],
    c=df["cluster"],
    cmap="viridis",
    s=80
)

plt.scatter(
    centroids[:, 0],
    centroids[:, 1],
    color="red",
    marker="X",
    s=250,
    label="Centroids"
)

plt.title("Customer Segmentation using KMeans")
plt.xlabel("Annual Income")
plt.ylabel("Spending Score")
plt.colorbar(scatter, label="Cluster")
plt.legend()

plt.tight_layout()
plt.savefig("customer_clusters.png")
plt.close()

print("="*45)

### Question 7: Calculate the Silhouette Score

score = silhouette_score(X, df["cluster"])
print("Silhouette Score :", score)

# A higher silhouette score generally means that data points
# are closer to their own cluster and farther from other clusters.
print("="*45)

### Question 8: Produce Business Insights

print("Business Insights:")

summary = (
    df.groupby("cluster")[["annual_income", "spending_score"]]
    .mean()
    .round(2)
)

print(summary)

highest_spending_cluster = summary["spending_score"].idxmax()
highest_income_cluster = summary["annual_income"].idxmax()
discount_cluster = summary["spending_score"].idxmin()
premium_cluster = highest_spending_cluster

print("\nHighest Average Spending Cluster:")
print(highest_spending_cluster)

print(
    "Reason: Customers in this cluster spend the most, "
    "making them valuable for premium products."
)

print("\nHighest Average Income Cluster:")
print(highest_income_cluster)

print(
    "Reason: Customers have the highest purchasing power."
)

print("\nDiscount Offer Cluster:")
print(discount_cluster)

print(
    "Reason: This cluster has the lowest average spending score, "
    "so discounts may encourage more purchases."
)

print("\nPremium Membership Cluster:")
print(premium_cluster)

print(
    "Reason: Customers already spend more and are likely to "
    "benefit from exclusive premium memberships."
)

print("="*45)

### Question 9: Export the Model

joblib.dump(model, "kmeans_model.pkl")

print("\nModel saved as kmeans_model.pkl")

print("="*45)
