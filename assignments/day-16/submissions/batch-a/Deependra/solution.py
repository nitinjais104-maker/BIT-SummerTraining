import matplotlib.pyplot as plt
import pandas as pd
import kagglehub
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
# Question 1: Download and Load the Dataset
# Download and load the public dataset:
# dataset_path = kagglehub.dataset_download("yasserh/titanic-dataset")
# df = pd.read_csv(dataset_path + "/Titanic-Dataset.csv")
# Print:
# the dataset path;
# the first five rows;
# the DataFrame shape.
dataset_path = kagglehub.dataset_download("yasserh/titanic-dataset")

df = pd.read_csv(dataset_path + "/Titanic-Dataset.csv")
print("Dataset Path:")
print(dataset_path)
print("\nFirst Five Rows:")
print(df.head())
print("\nDataFrame Shape:")
print(df.shape)

# Question 2: Explore the Dataset
# Print:
# the column names;
# each column's data type;
# descriptive statistics;
# the missing-value count for every column;
# the survival counts from df["Survived"].value_counts().
# In comments, identify the prediction label and state why this is a binary-classification problem.

print("\nColumn Names:")
print(df.columns.tolist())
print("\nData Types:")
print(df.dtypes)
print("\nDescriptive Statistics:")
print(df.describe(include="all"))
print("\nMissing Values:")
print(df.isnull().sum())
print("\nSurvival Counts:")
print(df["Survived"].value_counts())
# Prediction label:
# Survived
# This is a binary classification problem because the target
# variable has only two possible values:
# 0 = Not Survived
# 1 = Survived

# Question 3: Create an EDA Figure
# Create one figure containing four subplots:survival counts as a bar chart;
# average survival rate by Sex;
# average survival rate by Pclass;
# passenger age as a histogram with 20 bins.
# Give every subplot a title and axis labels. Save the complete figure as:
# titanic_eda.png
# Use plt.tight_layout() and plt.close() after saving.
fig, axes = plt.subplots(2, 2, figsize=(12, 10))

# Survival counts
df["Survived"].value_counts().plot(
    kind="bar",
    ax=axes[0, 0],
    color=["tomato", "steelblue"]
)
axes[0, 0].set_title("Survival Counts")
axes[0, 0].set_xlabel("Survived")
axes[0, 0].set_ylabel("Number of Passengers")

# Survival rate by Sex
df.groupby("Sex")["Survived"].mean().plot(
    kind="bar",
    ax=axes[0, 1],
    color=["orange", "green"]
)
axes[0, 1].set_title("Average Survival Rate by Sex")
axes[0, 1].set_xlabel("Sex")
axes[0, 1].set_ylabel("Average Survival Rate")

# Survival rate by Passenger Class
df.groupby("Pclass")["Survived"].mean().plot(
    kind="bar",
    ax=axes[1, 0],
    color="purple"
)
axes[1, 0].set_title("Average Survival Rate by Passenger Class")
axes[1, 0].set_xlabel("Passenger Class")
axes[1, 0].set_ylabel("Average Survival Rate")

# Age distribution
axes[1, 1].hist(
    df["Age"].dropna(),
    bins=20,
    color="skyblue",
    edgecolor="black"
)
axes[1, 1].set_title("Passenger Age Distribution")
axes[1, 1].set_xlabel("Age")
axes[1, 1].set_ylabel("Frequency")
plt.tight_layout()
plt.savefig("titanic_eda.png")
plt.close()

# Question 4: Prepare the Data
# Create an independent copy with only these columns:
# data = df[
#     ["Pclass", "Sex", "Age", "SibSp", "Parch", "Fare", "Embarked", "Survived"]
# ].copy()
# Then:
# fill missing Age values with the median age;
# fill missing Embarked values with its mode;
# map Sex using {"male": 0, "female": 1};
# map Embarked using {"S": 0, "C": 1, "Q": 2}.
# Print the missing-value counts and data types after preprocessing. The final feature data must contain no missing or text values.
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

# Fill missing values
data["Age"].fillna(data["Age"].median(), inplace=True)
data["Embarked"].fillna(data["Embarked"].mode()[0], inplace=True)

# Convert text columns into numbers
data["Sex"] = data["Sex"].map({"male": 0, "female": 1})
data["Embarked"] = data["Embarked"].map({"S": 0, "C": 1, "Q": 2})
print("\nMissing Values After Preprocessing:")
print(data.isnull().sum())
print("\nData Types After Preprocessing:")
print(data.dtypes)

# Question 5: Select Features and Split the Data
# Create:
# X = data[["Pclass", "Sex", "Age", "SibSp", "Parch", "Fare", "Embarked"]]
# y = data["Survived"]
# Split the data:
# X_train, X_test, y_train, y_test = train_test_split(
#     X,
#     y,
#     test_size=0.2,
#     random_state=42,
#     stratify=y,
# )
# Print the number of training and testing rows. Explain in a comment why stratify=y helps preserve the class proportions.
X = data[
    [
        "Pclass",
        "Sex",
        "Age",
        "SibSp",
        "Parch",
        "Fare",
        "Embarked",
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
# Using stratify=y keeps the same proportion of survived
# and not-survived passengers in both the training and testing sets.

# Question 6: Train and Evaluate a Decision Tree
# Train:
# decision_tree = DecisionTreeClassifier(random_state=42)
# Predict the test data and print:
# accuracy rounded to three decimal places;
# the confusion matrix;
# the classification report.
decision_tree = DecisionTreeClassifier(random_state=42)
decision_tree.fit(X_train, y_train)
dt_predictions = decision_tree.predict(X_test)
dt_accuracy = accuracy_score(y_test, dt_predictions)
print("\nDecision Tree Results")
print(f"Accuracy: {dt_accuracy:.3f}")
print("\nConfusion Matrix:")
print(confusion_matrix(y_test, dt_predictions))
print("\nClassification Report:")
print(classification_report(y_test, dt_predictions))

# Question 7: Train and Evaluate a Random Forest
# Train:
# random_forest = RandomForestClassifier(
#     n_estimators=100,
#     random_state=42,
# )
# Predict the test data and print the same three evaluation results as Question 6.
random_forest = RandomForestClassifier(
    n_estimators=100,
    random_state=42,
)
random_forest.fit(X_train, y_train)
rf_predictions = random_forest.predict(X_test)
rf_accuracy = accuracy_score(y_test, rf_predictions)
print("\nRandom Forest Results")
print(f"Accuracy: {rf_accuracy:.3f}")
print("\nConfusion Matrix:")
print(confusion_matrix(y_test, rf_predictions))
print("\nClassification Report:")
print(classification_report(y_test, rf_predictions))

# Question 8: Compare the Models
# Create and print a DataFrame with two columns:
# Model
# Accuracy
# It must contain one row for the Decision Tree and one for the Random Forest.
# Plot their accuracies as a bar chart with a y-axis range from 0 to 1. Save it as:
# model_accuracy.png
# Print the name of the model with the higher test accuracy. If the accuracies are equal, print that they are tied.
comparison = pd.DataFrame({
    "Model": [
        "Decision Tree",
        "Random Forest",
    ],
    "Accuracy": [
        dt_accuracy,
        rf_accuracy,
    ],
})

print("\nModel Comparison")
print(comparison)
plt.figure(figsize=(6, 5))
plt.bar(
    comparison["Model"],
    comparison["Accuracy"],
    color=["orange", "green"],
)
plt.title("Model Accuracy Comparison")
plt.xlabel("Model")
plt.ylabel("Accuracy")
plt.ylim(0, 1)
plt.tight_layout()
plt.savefig("model_accuracy.png")
plt.close()
if rf_accuracy > dt_accuracy:
    print("\nHigher Accuracy Model: Random Forest")
elif dt_accuracy > rf_accuracy:
    print("\nHigher Accuracy Model: Decision Tree")
else:
    print("\nBoth models have the same accuracy.")

# Question 9: Analyze Feature Importance
# Create a DataFrame containing each feature and its importance from:
# random_forest.feature_importances_
# Sort it from highest to lowest and print it.
# Create a bar chart of the sorted values and save it as:
# feature_importance.png
importance = pd.DataFrame({
    "Feature": X.columns,
    "Importance": random_forest.feature_importances_,
})

importance = importance.sort_values(
    by="Importance",
    ascending=False,
)
print("\nFeature Importance")
print(importance)

plt.figure(figsize=(8, 5))

plt.bar(
    importance["Feature"],
    importance["Importance"],
    color="steelblue",
)
plt.title("Random Forest Feature Importance")
plt.xlabel("Feature")
plt.ylabel("Importance")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("feature_importance.png")
plt.close()

# Question 10: Predict a New Passenger
# Use:
# new_passenger = pd.DataFrame({
#     "Pclass": [3],
#     "Sex": [0],
#     "Age": [25],
#     "SibSp": [1],
#     "Parch": [0],
#     "Fare": [8.0],
#     "Embarked": [0],
# })
# Use the Random Forest to print:
# Survived or Not Survived;
# the probability of not surviving;
# the probability of surviving.
# Round both probabilities to three decimal places. 
# Add a comment explaining that a model probability is an estimate, not a guarantee.
new_passenger = pd.DataFrame({
    "Pclass": [3],
    "Sex": [0],
    "Age": [25],
    "SibSp": [1],
    "Parch": [0],
    "Fare": [8.0],
    "Embarked": [0],
})
prediction = random_forest.predict(new_passenger)[0]
probabilities = random_forest.predict_proba(new_passenger)[0]
print("\nPrediction for New Passenger")
if prediction == 1:
    print("Prediction: Survived")
else:
    print("Prediction: Not Survived")
print(f"Probability of Not Surviving: {probabilities[0]:.3f}")
print(f"Probability of Surviving: {probabilities[1]:.3f}")

# A model probability is an estimate based on patterns learned
# from the training data. It is not a guarantee of the actual outcome.