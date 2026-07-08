# Day 16 Assignment

## Topic: Titanic Classification Project

Complete all questions in one file named `solution.py`.

This project uses a public Titanic dataset from Kaggle. It introduces tree-based classification and uses classification metrics; do not use R² for this assignment.

Install the required libraries if needed:

```bash
python3 -m pip install kagglehub pandas matplotlib scikit-learn
```

Start your program with:

```python
import matplotlib.pyplot as plt
import pandas as pd
import kagglehub
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
```

## Questions

### Question 1: Download and Load the Dataset

Download and load the public dataset:

```python
dataset_path = kagglehub.dataset_download("yasserh/titanic-dataset")
df = pd.read_csv(dataset_path + "/Titanic-Dataset.csv")
```

Print:

1. the dataset path;
2. the first five rows;
3. the DataFrame shape.

### Question 2: Explore the Dataset

Print:

1. the column names;
2. each column's data type;
3. descriptive statistics;
4. the missing-value count for every column;
5. the survival counts from `df["Survived"].value_counts()`.

In comments, identify the prediction label and state why this is a binary-classification problem.

### Question 3: Create an EDA Figure

Create one figure containing four subplots:

1. survival counts as a bar chart;
2. average survival rate by `Sex`;
3. average survival rate by `Pclass`;
4. passenger age as a histogram with 20 bins.

Give every subplot a title and axis labels. Save the complete figure as:

```text
titanic_eda.png
```

Use `plt.tight_layout()` and `plt.close()` after saving.

### Question 4: Prepare the Data

Create an independent copy with only these columns:

```python
data = df[
    ["Pclass", "Sex", "Age", "SibSp", "Parch", "Fare", "Embarked", "Survived"]
].copy()
```

Then:

1. fill missing `Age` values with the median age;
2. fill missing `Embarked` values with its mode;
3. map `Sex` using `{"male": 0, "female": 1}`;
4. map `Embarked` using `{"S": 0, "C": 1, "Q": 2}`.

Print the missing-value counts and data types after preprocessing. The final feature data must contain no missing or text values.

### Question 5: Select Features and Split the Data

Create:

```python
X = data[["Pclass", "Sex", "Age", "SibSp", "Parch", "Fare", "Embarked"]]
y = data["Survived"]
```

Split the data:

```python
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42,
    stratify=y,
)
```

Print the number of training and testing rows. Explain in a comment why `stratify=y` helps preserve the class proportions.

### Question 6: Train and Evaluate a Decision Tree

Train:

```python
decision_tree = DecisionTreeClassifier(random_state=42)
```

Predict the test data and print:

1. accuracy rounded to three decimal places;
2. the confusion matrix;
3. the classification report.

### Question 7: Train and Evaluate a Random Forest

Train:

```python
random_forest = RandomForestClassifier(
    n_estimators=100,
    random_state=42,
)
```

Predict the test data and print the same three evaluation results as Question 6.

### Question 8: Compare the Models

Create and print a DataFrame with two columns:

```text
Model
Accuracy
```

It must contain one row for the Decision Tree and one for the Random Forest.

Plot their accuracies as a bar chart with a y-axis range from `0` to `1`. Save it as:

```text
model_accuracy.png
```

Print the name of the model with the higher test accuracy. If the accuracies are equal, print that they are tied.

### Question 9: Analyze Feature Importance

Create a DataFrame containing each feature and its importance from:

```python
random_forest.feature_importances_
```

Sort it from highest to lowest and print it.

Create a bar chart of the sorted values and save it as:

```text
feature_importance.png
```

### Question 10: Predict a New Passenger

Use:

```python
new_passenger = pd.DataFrame({
    "Pclass": [3],
    "Sex": [0],
    "Age": [25],
    "SibSp": [1],
    "Parch": [0],
    "Fare": [8.0],
    "Embarked": [0],
})
```

Use the Random Forest to print:

1. `Survived` or `Not Survived`;
2. the probability of not surviving;
3. the probability of surviving.

Round both probabilities to three decimal places. Add a comment explaining that a model probability is an estimate, not a guarantee.

## Submission

Submit exactly these four files:

```text
assignments/day-16/submissions/batch-a/your-name/solution.py
assignments/day-16/submissions/batch-a/your-name/titanic_eda.png
assignments/day-16/submissions/batch-a/your-name/model_accuracy.png
assignments/day-16/submissions/batch-a/your-name/feature_importance.png
```

Use the same structure with `batch-b` when applicable.

Run your program from your submission folder:

```bash
cd assignments/day-16/submissions/batch-a/your-name
python3 solution.py
```

The first run downloads the dataset and therefore requires an internet connection.
