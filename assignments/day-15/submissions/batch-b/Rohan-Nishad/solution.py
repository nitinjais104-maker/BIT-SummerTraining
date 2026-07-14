import joblib
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score
import os

BASE_DIR = os.path.dirname(__file__)

# Data
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
print()
print("Shape:", df.shape)
print("Columns:", list(df.columns))
print("Missing values per column:")
print(df.isna().sum())
print()

# Question 2: Select the Clustering Features
X = df[["annual_income", "spending_score"]]
print("First five rows of X:")
print(X.head())
print()
# customer_id should not be used as a clustering feature because it is an identifier with no
# numeric relationship to the customer's behaviour; using it would introduce meaningless distances.

# Question 3: Use the Elbow Method
inertias = []
ks = list(range(1, 8))
for k in ks:
    km = KMeans(n_clusters=k, random_state=42, n_init=10)
    km.fit(X)
    inertias.append(km.inertia_)
    print(f"k={k}, inertia={km.inertia_:.2f}")

# Plot elbow curve
plt.figure()
plt.plot(ks, inertias, marker='o')
plt.title('Elbow Method: Inertia vs k')
plt.xlabel('k')
plt.ylabel('Inertia')
plt.grid(True)
plt.tight_layout()
plt.savefig(os.path.join(BASE_DIR, 'elbow_curve.png'))
plt.close()

# Question 4: Train the Final K-Means Model
model = KMeans(n_clusters=3, random_state=42, n_init=10)
df['cluster'] = model.fit_predict(X)
print("Complete DataFrame with cluster:")
print(df)
print()
print("Customers per cluster:")
print(df['cluster'].value_counts().sort_index())
# Cluster labels 0,1,2 are identifiers only — they don't imply ordering or ranking.

# Question 5: Inspect the Centroids
centroids = model.cluster_centers_
print('\nCentroids (annual_income, spending_score):')
for i, c in enumerate(np.round(centroids, 2)):
    print(f"Cluster {i}: Income={c[0]}, Spending={c[1]}")

# Question 6: Visualize Clusters and Centroids
plt.figure()
scatter = plt.scatter(df['annual_income'], df['spending_score'], c=df['cluster'], cmap='tab10')
plt.scatter(centroids[:,0], centroids[:,1], s=200, c='red', marker='X', label='Centroids')
plt.title('Customer Clusters')
plt.xlabel('Annual Income')
plt.ylabel('Spending Score')
plt.legend()
plt.colorbar(scatter, label='Cluster')
plt.tight_layout()
plt.savefig(os.path.join(BASE_DIR, 'customer_clusters.png'))
plt.close()

# Question 7: Calculate the Silhouette Score
score = silhouette_score(X, df['cluster'])
print(f"Silhouette score: {score:.3f}")
# A higher silhouette score generally means points are closer to their own cluster and farther from others.

# Question 8: Produce Business Insights
summary = df.groupby('cluster')[['annual_income', 'spending_score']].mean().round(2)
print('\nCluster summary (average income and spending):')
print(summary)

# Derive clusters for marketing choices
highest_spending_cluster = summary['spending_score'].idxmax()
highest_income_cluster = summary['annual_income'].idxmax()
lowest_income_cluster = summary['annual_income'].idxmin()

print()
print(f"Cluster with highest average spending score: {highest_spending_cluster}")
print(f"Cluster with highest average income: {highest_income_cluster}")
print(f"Cluster recommended for discount offers: {lowest_income_cluster}")
print(f"Cluster recommended for premium-membership offers: {highest_income_cluster}")

print()
print("Reasons:")
print(f"- Cluster {highest_spending_cluster}: highest avg spending -> target with promotions for immediate revenue.")
print(f"- Cluster {highest_income_cluster}: highest avg income -> target for premium memberships.")
print(f"- Cluster {lowest_income_cluster}: lower avg income -> consider discount offers to increase purchases.")

# Question 9: Export the Model
model_path = os.path.join(BASE_DIR, 'kmeans_model.pkl')
joblib.dump(model, model_path)
print(f"Model saved as {os.path.basename(model_path)}")
