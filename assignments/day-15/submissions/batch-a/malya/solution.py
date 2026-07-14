#day15
import joblib
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score
# Dataset
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
print("First five rows:")
print(df.head())
print("\nDataFrame Shape:")
print(df.shape)
print("\nColumn Names:")
print(df.columns)
print("\nMissing Values:")
print(df.isnull().sum())


# Question 2: Select Clustering Features
X = df[["annual_income", "spending_score"]]
print("\nClustering Features:")
print(X.head())
# customer_id should not be used because it is only an identifier.
# It does not represent customer behaviour or similarity.


# Question 3: Elbow Method
inertias = []
print("\nElbow Method Values:")
for k in range(1, 8):
    kmeans = KMeans(
        n_clusters=k,
        random_state=42,
        n_init=10
    )
    kmeans.fit(X)
    inertias.append(kmeans.inertia_)
    print(f"k={k}, Inertia={kmeans.inertia_:.2f}")
plt.figure(figsize=(8, 5))
plt.plot(
    range(1, 8),
    inertias,
    marker="o"
)
plt.xlabel("Number of Clusters (k)")
plt.ylabel("Inertia")
plt.title("Elbow Curve for K-Means")
plt.grid(True)
plt.tight_layout()
plt.savefig("elbow_curve.png")
plt.close()


# Question 4: Train Final K-Means Model
model = KMeans(
    n_clusters=3,
    random_state=42,
    n_init=10
)
df["cluster"] = model.fit_predict(X)
print("\nComplete DataFrame:")
print(df)
print("\nNumber of Customers in Each Cluster:")
print(df["cluster"].value_counts())
# Cluster numbers like 0, 1, and 2 are only labels assigned by the algorithm.
# They do not represent better/worse ranking.

# Question 5: Inspect the Centroids
centroids = model.cluster_centers_
print("\nCluster Centroids:")
for i, centroid in enumerate(centroids):
    print(
        f"Cluster {i}: "
        f"Income = {centroid[0]:.2f}, "
        f"Spending Score = {centroid[1]:.2f}"
    )
# Question 6: Visualize Clusters and Centroids
plt.figure(figsize=(8, 5))
scatter = plt.scatter(
    X["annual_income"],
    X["spending_score"],
    c=df["cluster"],
    s=80
)
plt.scatter(
    centroids[:, 0],
    centroids[:, 1],
    marker="X",
    s=250,
    label="Centroids"
)
plt.xlabel("Annual Income")
plt.ylabel("Spending Score")
plt.title("Customer Segments Using K-Means")
plt.colorbar(scatter, label="Cluster")
plt.legend()
plt.tight_layout()
plt.savefig("customer_clusters.png")
plt.close()


# Question 7: Silhouette Score
score = silhouette_score(
    X,
    df["cluster"]
)
print(
    "\nSilhouette Score:",
    round(score, 3)
)
# A higher silhouette score generally means that points are closer
# to their own cluster and farther away from other clusters.


# Question 8: Business Insights
summary = df.groupby("cluster")[[
    "annual_income",
    "spending_score"
]].mean()
print("\nCluster Summary:")
print(summary)
highest_spending_cluster = (
    summary["spending_score"]
    .idxmax()
)
highest_income_cluster = (
    summary["annual_income"]
    .idxmax()
)
low_spending_cluster = (
    summary["spending_score"]
    .idxmin()
)
premium_cluster = highest_spending_cluster
print(
    f"\nCluster with highest average spending score: "
    f"Cluster {highest_spending_cluster}"
)
print(
    f"Cluster with highest average income: "
    f"Cluster {highest_income_cluster}"
)
print(
    f"\nDiscount Offers: Cluster {low_spending_cluster}"
)
print(
    "Reason: This group has lower spending behaviour, "
    "so discounts can encourage more purchases."
)
print(
    f"\nPremium Membership Offers: Cluster {premium_cluster}"
)
print(
    "Reason: This group has the highest spending score, "
    "showing strong customer engagement."
)


# Question 9: Export the Model
joblib.dump(
    model,
    "kmeans_model.pkl"
)
print("\nModel saved as kmeans_model.pkl")