
import matplotlib.pyplot as plt
import pandas as pd
import kagglehub
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier


# Question 1: Download and Load Dataset
dataset_path = kagglehub.dataset_download("yasserh/titanic-dataset")
df = pd.read_csv(dataset_path + "/Titanic-Dataset.csv")
print("Dataset Path:")
print(dataset_path)
print("\nFirst Five Rows:")
print(df.head())
print("\nDataset Shape:")
print(df.shape)



# Question 2: Explore Dataset
print("\nColumn Names:")
print(df.columns)
print("\nData Types:")
print(df.dtypes)
print("\nDescriptive Statistics:")
print(df.describe())
print("\nMissing Values:")
print(df.isnull().sum())
print("\nSurvival Counts:")
print(df["Survived"].value_counts())
# Survived is the prediction label.
# This is a binary-classification problem because there are only two outcomes:
# 0 = Not Survived and 1 = Survived.



# Question 3: EDA Figure
fig, axes = plt.subplots(2, 2, figsize=(12, 8))
df["Survived"].value_counts().plot(
    kind="bar",
    ax=axes[0, 0]
)
axes[0, 0].set_title("Survival Count")
axes[0, 0].set_xlabel("Survived")
axes[0, 0].set_ylabel("Count")
df.groupby("Sex")["Survived"].mean().plot(
    kind="bar",
    ax=axes[0, 1]
)
axes[0, 1].set_title("Average Survival Rate by Sex")
axes[0, 1].set_xlabel("Sex")
axes[0, 1].set_ylabel("Survival Rate")
df.groupby("Pclass")["Survived"].mean().plot(
    kind="bar",
    ax=axes[1, 0]
)
axes[1, 0].set_title("Average Survival Rate by Pclass")
axes[1, 0].set_xlabel("Passenger Class")
axes[1, 0].set_ylabel("Survival Rate")
axes[1, 1].hist(
    df["Age"].dropna(),
    bins=20
)
axes[1, 1].set_title("Passenger Age Distribution")
axes[1, 1].set_xlabel("Age")
axes[1, 1].set_ylabel("Frequency")
plt.tight_layout()
plt.savefig("titanic_eda.png")
plt.close()



# Question 4: Prepare Data
data = df[
    [
        "Pclass",
        "Sex",
        "Age",
        "SibSp",
        "Parch",
        "Fare",
        "Embarked",
        "Survived",
    ]
].copy()
data["Age"] = data["Age"].fillna(
    data["Age"].median()
)
data["Embarked"] = data["Embarked"].fillna(
    data["Embarked"].mode()[0]
)
# Convert categorical values
data["Sex"] = data["Sex"].map(
    {
        "male": 0,
        "female": 1
    }
)
data["Embarked"] = data["Embarked"].map(
    {
        "S": 0,
        "C": 1,
        "Q": 2
    }
)
print("\nMissing Values After Preprocessing:")
print(data.isnull().sum())
print("\nData Types After Preprocessing:")
print(data.dtypes)



# Question 5: Select Features and Split Data
X = data[
    [
        "Pclass",
        "Sex",
        "Age",
        "SibSp",
        "Parch",
        "Fare",
        "Embarked"
    ]
]
y = data["Survived"]
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42,
    stratify=y,
)
print("\nTraining Rows:", len(X_train))
print("Testing Rows:", len(X_test))
# stratify=y keeps the same survival class proportion
# in both training and testing datasets.

# Question 6: Decision Tree Model
decision_tree = DecisionTreeClassifier(
    random_state=42
)
decision_tree.fit(
    X_train,
    y_train
)
dt_prediction = decision_tree.predict(X_test)
dt_accuracy = accuracy_score(
    y_test,
    dt_prediction
)
print("\nDecision Tree Results")
print("Accuracy:",
      round(dt_accuracy, 3))
print("\nConfusion Matrix:")
print(confusion_matrix(y_test, dt_prediction))
print("\nClassification Report:")
print(classification_report(y_test, dt_prediction))



# Question 7: Random Forest Model
random_forest = RandomForestClassifier(
    n_estimators=100,
    random_state=42
)
random_forest.fit(
    X_train,
    y_train
)
rf_prediction = random_forest.predict(X_test)
rf_accuracy = accuracy_score(
    y_test,
    rf_prediction
)
print("\nRandom Forest Results")
print("Accuracy:",
      round(rf_accuracy, 3))
print("\nConfusion Matrix:")
print(confusion_matrix(y_test, rf_prediction))
print("\nClassification Report:")
print(classification_report(y_test, rf_prediction))



# Question 8: Compare Models
comparison = pd.DataFrame(
    {
        "Model": [
            "Decision Tree",
            "Random Forest"
        ],
        "Accuracy": [
            dt_accuracy,
            rf_accuracy
        ]
    }
)
print("\nModel Comparison:")
print(comparison)
plt.figure(figsize=(6, 4))
plt.bar(
    comparison["Model"],
    comparison["Accuracy"]
)
plt.ylim(0, 1)
plt.xlabel("Model")
plt.ylabel("Accuracy")
plt.title("Model Accuracy Comparison")
plt.tight_layout()
plt.savefig("model_accuracy.png")
plt.close()
if dt_accuracy > rf_accuracy:
    print("\nHigher Accuracy Model: Decision Tree")
elif rf_accuracy > dt_accuracy:
    print("\nHigher Accuracy Model: Random Forest")
else:
    print("\nBoth Models Have Equal Accuracy")



# Question 9: Feature Importance
importance_df = pd.DataFrame(
    {
        "Feature": X.columns,
        "Importance": random_forest.feature_importances_
    }
)
importance_df = importance_df.sort_values(
    by="Importance",
    ascending=False
)
print("\nFeature Importance:")
print(importance_df)
plt.figure(figsize=(8, 5))
plt.bar(
    importance_df["Feature"],
    importance_df["Importance"]
)
plt.xticks(rotation=45)
plt.xlabel("Feature")
plt.ylabel("Importance")
plt.title("Random Forest Feature Importance")
plt.tight_layout()
plt.savefig("feature_importance.png")
plt.close()


# Question 10: Predict New Passenger
new_passenger = pd.DataFrame(
    {
        "Pclass": [3],
        "Sex": [0],
        "Age": [25],
        "SibSp": [1],
        "Parch": [0],
        "Fare": [8.0],
        "Embarked": [0],
    }
)
prediction = random_forest.predict(
    new_passenger
)
probability = random_forest.predict_proba(
    new_passenger
)
if prediction[0] == 1:
    print("\nPrediction: Survived")
else:
    print("\nPrediction: Not Survived")
print(
    "Probability of Not Surviving:",
    round(probability[0][0], 3)
)
print(
    "Probability of Surviving:",
    round(probability[0][1], 3)
)
# Model probability is only an estimate based on learned patterns.
# It is not a guarantee of the actual outcome.