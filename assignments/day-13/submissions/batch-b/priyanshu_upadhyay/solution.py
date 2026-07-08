# Day 13 Assignment - Supervised Learning With Student Data

import pandas as pd
from sklearn.linear_model import LinearRegression, LogisticRegression
from sklearn.metrics import mean_absolute_error, r2_score
from sklearn.model_selection import train_test_split

student_data = {
    "study_hours": [2, 5, 7, 3, 6, 8, 4, 1, 9, 5],
    "attendance": [65, 78, 88, 70, 82, 90, 75, 60, 95, 80],
    "previous_mark": [55, 64, 75, 58, 70, 85, 62, 50, 92, 68],
    "final_marks": [58, 72, 84, 62, 78, 90, 68, 52, 95, 74],
}

# Question 1: Create and Inspect the DataFrame
df = pd.DataFrame(student_data)
print("=== Question 1 ===")
print(df)
print(df.head())
print("Shape:", df.shape)
print(df.describe())

# Question 2: Select Features and Label
# X contains features (inputs used to make prediction)
# y contains the label (the output we want to predict)
X = df[["study_hours", "attendance", "previous_mark"]]
y = df["final_marks"]
print("\n=== Question 2 ===")
print(X.head())
print(y.head())

# Question 3: Train a Linear Regression Model
print("\n=== Question 3 ===")
model = LinearRegression()
model.fit(X, y)
print("Linear regression model trained")

# Question 4: Predict a New Student's Marks
print("\n=== Question 4 ===")
new_student = pd.DataFrame([[6, 82, 70]], columns=["study_hours", "attendance", "previous_mark"])
predicted_mark = model.predict(new_student)
print("Predicted final mark:", round(float(predicted_mark[0]), 1))

# Question 5: Inspect Model Coefficients
# A coefficient shows how strongly a feature affects the prediction.
# A higher coefficient means that feature has more impact on the final mark.
print("\n=== Question 5 ===")
print("Model coefficients:", model.coef_)

# Question 6: Create and Predict a Pass/Fail Result
print("\n=== Question 6 ===")
df["result"] = (df["final_marks"] >= 70).astype(int)
log_model = LogisticRegression(max_iter=1000)
log_model.fit(X, df["result"])
predicted_result = log_model.predict(new_student)
print("Predicted result (0=Fail, 1=Pass):", predicted_result[0])
if predicted_result[0] == 1:
    print("The new student will Pass")
else:
    print("The new student will Fail")

# Question 7: Split Training and Testing Data
# A model should be tested on unseen data to check if it generalises well,
# not just memorises the training data.
print("\n=== Question 7 ===")
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)
print("Training rows:", len(X_train))
print("Testing rows:", len(X_test))

# Question 8: Evaluate the Regression Model
# Lower MAE means predictions are closer to actual values - better model.
# R² closer to 1 means model explains the data well - better model.
print("\n=== Question 8 ===")
model2 = LinearRegression()
model2.fit(X_train, y_train)
y_pred = model2.predict(X_test)
print("Actual test values:", list(y_test))
print("Predicted values:", [round(float(p), 1) for p in y_pred])
print("MAE:", round(mean_absolute_error(y_test, y_pred), 2))
print("R²:", round(r2_score(y_test, y_pred), 2))