# Day 16 Assignment - Titanic Classification Project

import matplotlib.pyplot as plt
import pandas as pd
import kagglehub
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier

# Question 1: Download and Load the Dataset
print("=== Question 1 ===")
dataset_path = kagglehub.dataset_download("yasserh/titanic-dataset")
df = pd.read_csv(dataset_path + "/Titanic-Dataset.csv")
print("Dataset path:", dataset_path)
print(df.head())
print("Shape:", df.shape)

# Question 2: Explore the Dataset

print("\n=== Question 2 ===")
print("Columns:", list(df.columns))
print("\nData types:\n", df.dtypes)
print("\nDescriptive statistics:\n", df.describe())
print("\nMissing values:\n", df.isnull().sum())
print("\nSurvival counts:\n", df["Survived"].value_counts())

# Question 3: EDA Figure
print("\n=== Question 3 ===")
fig, axes = plt.subplots(2, 2, figsize=(12, 10))

df["Survived"].value_counts().plot(kind="bar", ax=axes[0, 0], color=["salmon", "steelblue"])
axes[0, 0].set_title("Survival Counts")
axes[0, 0].set_xlabel("Survived")
axes[0, 0].set_ylabel("Count")

df.groupby("Sex")["Survived"].mean().plot(kind="bar", ax=axes[0, 1], color=["steelblue", "salmon"])
axes[0, 1].set_title("Survival Rate by Sex")
axes[0, 1].set_xlabel("Sex")
axes[0, 1].set_ylabel("Survival Rate")

df.groupby("Pclass")["Survived"].mean().plot(kind="bar", ax=axes[1, 0], color=["green", "orange", "red"])
axes[1, 0].set_title("Survival Rate by Pclass")
axes[1, 0].set_xlabel("Pclass")
axes[1, 0].set_ylabel("Survival Rate")

axes[1, 1].hist(df["Age"].dropna(), bins=20, color="purple", edgecolor="black")
axes[1, 1].set_title("Age Distribution")
axes[1, 1].set_xlabel("Age")
axes[1, 1].set_ylabel("Frequency")

plt.tight_layout()
plt.savefig("titanic_eda.png")
plt.close()
print("titanic_eda.png saved")

# Question 4: Prepare the Data
print("\n=== Question 4 ===")
data = df[["Pclass", "Sex", "Age", "SibSp", "Parch", "Fare", "Embarked", "Survived"]].copy()
data["Age"].fillna(data["Age"].median(), inplace=True)
data["Embarked"].fillna(data["Embarked"].mode()[0], inplace=True)
data["Sex"] = data["Sex"].map({"male": 0, "female": 1})
data["Embarked"] = data["Embarked"].map({"S": 0, "C": 1, "Q": 2})
print("Missing values after preprocessing:\n", data.isnull().sum())
print("\nData types after preprocessing:\n", data.dtypes)

# Question 5: Select Features and Split

print("\n=== Question 5 ===")
X = data[["Pclass", "Sex", "Age", "SibSp", "Parch", "Fare", "Embarked"]]
y = data["Survived"]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)
print("Training rows:", len(X_train))
print("Testing rows:", len(X_test))

# Question 6: Decision Tree

print("\n=== Question 6 ===")
decision_tree = DecisionTreeClassifier(random_state=42)
decision_tree.fit(X_train, y_train)
dt_pred = decision_tree.predict(X_test)
dt_accuracy = accuracy_score(y_test, dt_pred)
print("Decision Tree Accuracy:", round(dt_accuracy, 3))
print("Confusion Matrix:\n", confusion_matrix(y_test, dt_pred))
print("Classification Report:\n", classification_report(y_test, dt_pred))

# Question 7: Random Forest
print("\n=== Question 7 ===")
random_forest = RandomForestClassifier(n_estimators=100, random_state=42)
random_forest.fit(X_train, y_train)
rf_pred = random_forest.predict(X_test)
rf_accuracy = accuracy_score(y_test, rf_pred)
print("Random Forest Accuracy:", round(rf_accuracy, 3))
print("Confusion Matrix:\n", confusion_matrix(y_test, rf_pred))
print("Classification Report:\n", classification_report(y_test, rf_pred))

# Question 8: Compare Models
print("\n=== Question 8 ===")
comparison = pd.DataFrame({
    "Model": ["Decision Tree", "Random Forest"],
    "Accuracy": [round(dt_accuracy, 3), round(rf_accuracy, 3)]
})
print(comparison)

plt.bar(comparison["Model"], comparison["Accuracy"], color=["steelblue", "green"])
plt.ylim(0, 1)
plt.title("Model Accuracy Comparison")
plt.xlabel("Model")
plt.ylabel("Accuracy")
plt.tight_layout()
plt.savefig("model_accuracy.png")
plt.close()
print("model_accuracy.png saved")

if dt_accuracy > rf_accuracy:
    print("Better model: Decision Tree")
elif rf_accuracy > dt_accuracy:
    print("Better model: Random Forest")
else:
    print("Both models are tied in accuracy")

# Question 9: Feature Importance
print("\n=== Question 9 ===")
importance_df = pd.DataFrame({
    "Feature": X.columns,
    "Importance": random_forest.feature_importances_
}).sort_values("Importance", ascending=False)
print(importance_df)

plt.bar(importance_df["Feature"], importance_df["Importance"], color="teal")
plt.title("Feature Importance")
plt.xlabel("Feature")
plt.ylabel("Importance")
plt.tight_layout()
plt.savefig("feature_importance.png")
plt.close()
print("feature_importance.png saved")

# Question 10: Predict a New Passenger

print("\n=== Question 10 ===")
new_passenger = pd.DataFrame({
    "Pclass": [3], "Sex": [0], "Age": [25],
    "SibSp": [1], "Parch": [0], "Fare": [8.0], "Embarked": [0],
})
result = random_forest.predict(new_passenger)
proba = random_forest.predict_proba(new_passenger)
print("Prediction:", "Survived" if result[0] == 1 else "Not Survived")
print("Probability of Not Surviving:", round(float(proba[0][0]), 3))
print("Probability of Surviving:", round(float(proba[0][1]), 3))