import pandas as pd
from sklearn.linear_model import LinearRegression, LogisticRegression
from sklearn.metrics import mean_absolute_error, r2_score
from sklearn.model_selection import train_test_split

# Student Data
student_data = {
    "study_hours": [2, 5, 7, 3, 6, 8, 4, 1, 9, 5],
    "attendance": [65, 78, 88, 70, 82, 90, 75, 60, 95, 80],
    "previous_mark": [55, 64, 75, 58, 70, 85, 62, 50, 92, 68],
    "final_marks": [58, 72, 84, 62, 78, 90, 68, 52, 95, 74],
}

# ==================================================
# Question 1: Create and Inspect the DataFrame
# ==================================================

df = pd.DataFrame(student_data)

print("Complete DataFrame:")
print(df)

print("\nFirst Five Rows:")
print(df.head())

print("\nShape:")
print(df.shape)

print("\nDescriptive Statistics:")
print(df.describe())

# ==================================================
# Question 2: Select Features and Label
# ==================================================

X = df[["study_hours", "attendance", "previous_mark"]]
y = df["final_marks"]

print("\nFeatures (X):")
print(X.head())

print("\nLabel (y):")
print(y.head())

# X contains the input features used to make predictions.
# y contains the target value (label) that the model learns to predict.

# ==================================================
# Question 3: Train a Linear Regression Model
# ==================================================

model = LinearRegression()
model.fit(X, y)

print("\nLinear regression model trained")

# ==================================================
# Question 4: Predict a New Student's Marks
# ==================================================

new_student = pd.DataFrame({
    "study_hours": [6],
    "attendance": [82],
    "previous_mark": [70]
})

prediction = model.predict(new_student)

print("\nPredicted Final Marks:")
print(round(prediction[0], 1))

# ==================================================
# Question 5: Inspect Model Coefficients
# ==================================================

print("\nModel Coefficients:")
print(model.coef_)

# A coefficient shows how strongly a feature affects the prediction.
# A larger positive coefficient means that feature has a greater positive impact.

# ==================================================
# Question 6: Pass / Fail Prediction
# ==================================================

df["result"] = (df["final_marks"] >= 70).astype(int)

X_class = df[["study_hours", "attendance", "previous_mark"]]
y_class = df["result"]

log_model = LogisticRegression(max_iter=1000)
log_model.fit(X_class, y_class)

result_prediction = log_model.predict(new_student)[0]

print("\nPass/Fail Prediction:")
print(result_prediction)

if result_prediction == 1:
    print("Meaning: Pass")
else:
    print("Meaning: Fail")

# ==================================================
# Question 7: Train-Test Split
# ==================================================

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.3,
    random_state=42,
)

print("\nTraining Rows:", len(X_train))
print("Testing Rows:", len(X_test))

# A model should be tested on unseen data to check how well it performs
# on new data instead of only memorizing the training data.

# ==================================================
# Question 8: Evaluate the Regression Model
# ==================================================

model2 = LinearRegression()
model2.fit(X_train, y_train)

y_pred = model2.predict(X_test)

print("\nActual Test Values:")
print(y_test.values)

print("\nPredicted Values:")
print(y_pred)

mae = mean_absolute_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print("\nMean Absolute Error (MAE):", round(mae, 2))
print("R2 Score:", round(r2, 2))

# Lower MAE is better because it means predictions are closer to actual values.
# An R² value closer to 1 is better because it means the model explains more variation in the data.