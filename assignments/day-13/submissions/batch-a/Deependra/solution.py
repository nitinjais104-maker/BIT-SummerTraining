
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
# Create a DataFrame named df from student_data.
# Print:the complete DataFrame;
# the first five rows;
# its shape;
# its descriptive statistics using describe().
df = pd.DataFrame(student_data)
print("Complete DataFrame:")
print(df)
print("\nFirst Five Rows:")
print(df.head())
print("\nShape:")
print(df.shape)
print("\nDescriptive Statistics:")
print(df.describe())

# Question 2: Select Features and Label
# Create:
# X = df[["study_hours", "attendance", "previous_mark"]]
# y = df["final_marks"]
# Print the first five rows of X and y.
# In a comment, explain why X contains features and y contains the label.
X = df[["study_hours", "attendance", "previous_mark"]]
y = df["final_marks"]
print("\nFeatures:--> (First Five Rows):")
print(X.head())
print("\nLabel:--> (First Five Rows):")
print(y.head())
# X contains the input features used for prediction.
# y contains the target (label) that the model learns to predict.

# Question 3: Train a Linear Regression Model
# Create a LinearRegression model and train it using fit(X, y).
# Print:Linear regression model trained
model = LinearRegression()
model.fit(X, y)
print("\nLinear regression model trained")

# Question 4: Predict a New Student's Marks
# Predict the final mark for this student:
# study_hours = 6
# attendance = 82
# previous_mark = 70
# Create the new student as a one-row DataFrame with the same feature column names as X. Print the predicted mark rounded to one decimal place.

new_student = pd.DataFrame({
    "study_hours": [6],
    "attendance": [82],
    "previous_mark": [70]
})
predicted_mark = model.predict(new_student)
print("\nPredicted Final Mark:")
print(round(predicted_mark[0], 1))

# Question 5: Inspect Model Coefficients
# Print the model's coefficients using model.coef_.
# Add a comment explaining that a coefficient shows how strongly a feature affects the prediction.
print("\nModel Coefficients:")
print(model.coef_)
# A coefficient shows how strongly each feature influences
# the predicted final marks.


# Question 6: Create and Predict a Pass/Fail Result
# Create a new column named result:
# df["result"] = (df["final_marks"] >= 70).astype(int)
# Here:
# 1 means pass;
# 0 means fail.
# Train a LogisticRegression(max_iter=1000) model using the same three features and result as the label. Predict whether the new student from Question 4 will pass or fail, then print both the number and its meaning.
df["result"] = (df["final_marks"] >= 70).astype(int)

X_class = df[["study_hours", "attendance", "previous_mark"]]
y_class = df["result"]

log_model = LogisticRegression(max_iter=1000)
log_model.fit(X_class, y_class)

prediction = log_model.predict(new_student)[0]

print("\nPass/Fail Prediction:")
print("Prediction:", prediction)

if prediction == 1:
    print("Meaning: Pass")
else:
    print("Meaning: Fail")

# Question 7: Split Training and Testing Data
# Use:X_train, X_test, y_train, y_test = train_test_split(
#     X,
#     y,
#     test_size=0.3,
#     random_state=42,
# )
# Print the number of training rows and testing rows.
# In a comment, explain why a model should be tested on data that it did not use for training.
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.3,
    random_state=42,
)

print("\nTraining Rows:", len(X_train))
print("Testing Rows:", len(X_test))

# Testing on unseen data helps measure how well the model
# generalizes to new data instead of memorizing the training data.

# Question 8: Evaluate the Regression Model
# Create a new LinearRegression model. Train it with X_train and y_train, then predict X_test.
# Print:
# the actual test values;
# the predicted values;
# MAE rounded to two decimal places;
# R² rounded to two decimal places.
# Add comments explaining:
# a lower MAE is better;
# an R² value closer to 1 is better.
test_model = LinearRegression()
test_model.fit(X_train, y_train)
y_pred = test_model.predict(X_test)
print("\nActual Test Values:")
print(y_test.values)
print("\nPredicted Values:")
print(y_pred)
mae = mean_absolute_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)
print("\nMean Absolute Error (MAE):", round(mae, 2))
print("R² Score:", round(r2, 2))

# A lower MAE indicates that predictions are closer to the actual values.
# An R² value closer to 1 indicates a better fit between predictions and actual values.