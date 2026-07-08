# Day 15 Assignment

## Topic: Applied K-Means Customer Segmentation

Complete all questions in one file named `solution.py`.

Day 14 covered the K-means cycle manually. This assignment uses scikit-learn to apply that cycle to a complete customer-segmentation problem.

Install the required libraries if needed:

```bash
python3 -m pip install pandas numpy matplotlib scikit-learn joblib
```

Start your program with:

```python
import joblib
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score
```

Use this dataset:

```python
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
```

## Questions

### Question 1: Load and Inspect the Data

Create a DataFrame named `df` from `customer_data`.

Print:

1. the first five rows;
2. the DataFrame shape;
3. the column names;
4. the missing-value count for each column.

### Question 2: Select the Clustering Features

Create:

```python
X = df[["annual_income", "spending_score"]]
```

Print the first five rows of `X`.

In a comment, explain why `customer_id` should not be used as a clustering feature.

### Question 3: Use the Elbow Method

For every value of `k` from `1` to `7`:

1. create `KMeans(n_clusters=k, random_state=42, n_init=10)`;
2. train it with `X`;
3. add its `inertia_` value to a list named `inertias`.

Print each `k` and inertia value rounded to two decimal places.

Plot the inertia values against `k` using markers, axis labels, a title, and a grid. Save the chart as:

```text
elbow_curve.png
```

Use `plt.tight_layout()` and `plt.close()` after saving.

### Question 4: Train the Final K-Means Model

Use three clusters:

```python
model = KMeans(n_clusters=3, random_state=42, n_init=10)
df["cluster"] = model.fit_predict(X)
```

Print the complete DataFrame and the number of customers in each cluster.

Add a comment explaining why cluster numbers such as `0`, `1`, and `2` are identifiers rather than rankings.

### Question 5: Inspect the Centroids

Get the cluster centres using:

```python
centroids = model.cluster_centers_
```

Print the centroids rounded to two decimal places. Clearly label the income and spending values in your output.

### Question 6: Visualize Clusters and Centroids

Create a scatter plot with:

- annual income on the x-axis;
- spending score on the y-axis;
- customer points coloured by cluster;
- centroids shown as large red `X` markers;
- a title, axis labels, colour bar, and centroid legend.

Save it as:

```text
customer_clusters.png
```

Use `plt.tight_layout()` and `plt.close()` after saving.

### Question 7: Calculate the Silhouette Score

Calculate:

```python
score = silhouette_score(X, df["cluster"])
```

Print the score rounded to three decimal places.

In a comment, explain that a higher silhouette score generally means points are closer to their own cluster and farther from other clusters.

### Question 8: Produce Business Insights

Group the DataFrame by `cluster` and calculate the average annual income and spending score for each cluster.

Print the summary table, then identify:

1. the cluster with the highest average spending score;
2. the cluster with the highest average income;
3. a cluster that could receive discount offers;
4. a cluster that could receive premium-membership offers.

Print one short reason for each marketing choice. Derive the cluster numbers from the summary instead of assuming a fixed label.

### Question 9: Export the Model

Save the trained model:

```python
joblib.dump(model, "kmeans_model.pkl")
```

Print:

```text
Model saved as kmeans_model.pkl
```

## Submission

Submit exactly these four files:

```text
assignments/day-15/submissions/batch-a/your-name/solution.py
assignments/day-15/submissions/batch-a/your-name/elbow_curve.png
assignments/day-15/submissions/batch-a/your-name/customer_clusters.png
assignments/day-15/submissions/batch-a/your-name/kmeans_model.pkl
```

Use the same structure with `batch-b` when applicable.

Run your program from your submission folder so generated files are saved in the correct place:

```bash
cd assignments/day-15/submissions/batch-a/your-name
python3 solution.py
```
