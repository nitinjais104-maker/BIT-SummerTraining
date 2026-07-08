# Day 13 Assignment
#==========================================================>>>
import pandas as pd
from sklearn.linear_model import LinearRegression, LogisticRegression
from sklearn.metrics import mean_absolute_error, r2_score
from sklearn.model_selection import train_test_split
#Use this student data:
student_data = {
    "study_hours": [2, 5, 7, 3, 6, 8, 4, 1, 9, 5],
    "attendance": [65, 78, 88, 70, 82, 90, 75, 60, 95, 80],
    "previous_mark": [55, 64, 75, 58, 70, 85, 62, 50, 92, 68],
    "final_marks": [58, 72, 84, 62, 78, 90, 68, 52, 95, 74],
}
#=========================================================>>>
# Question 1: Create and Inspect the DataFrame
# Create a DataFrame named `df` from `student_data`.
df = pd.DataFrame(student_data)
print("Complete DataFrame:")
print(df)
print("\nFirst five rows:")
print(df.head())
print("\nShape of the DataFrame:")
print(df.shape)
print("\nDescriptive statistics:")
print(df.describe())
print("="*50)
#=========================================================>>>
# Question 2: Select Features and Label
X = df[["study_hours", "attendance", "previous_mark"]]
y  = df["final_marks"]
print("\nFeatures (X):")
print(X.head())
print("\nLabel (y):")
print(y.head())
# X contains features because it stores the input variables (study hours, attendance, and previous marks) used by the model to learn patterns and make predictions.
# y contains the label because it represents the target value (final marks) that the machine learning model tries to predict.
print("="*50)
#=========================================================>>>
# Question 3: Train a Linear Regression Model
# Create a `LinearRegression` model and train it using `fit(X, y)`.
model = LinearRegression()
model.fit(X,y)
print('Model Ready')
print("="*50)
#=========================================================>>>
# Question 4: Predict a New Student's Marks
# Predict the final mark for this student:
naya_student = pd.DataFrame({
    "study_hours": [6],
    "attendance": [82],
    "previous_mark": [70]
})
predicted_mark = model.predict(naya_student)
print(f"Predicted final mark for the new student: {predicted_mark[0]:.1f}")
print("="*50)
#=========================================================>>>
# Question 5: Inspect Model Coefficients
# Print the model's coefficients using `model.coef_`.
# Add a comment explaining that a coefficient shows how strongly a feature affects the prediction.
print(f"Model coefficients: {model.coef_}")
"""Comment """
# A coefficient indicates the strength and direction of the relationship between a feature and the predicted outcome. A positive coefficient means that as the feature increases, the predicted outcome also increases, while a negative coefficient means that as the feature increases, the predicted outcome decreases.  
print("="*50)
#========================================================>>>
# # Question 6: Create and Predict a Pass/Fail Result
# Create a new column named `result`:
# Train a `LogisticRegression(max_iter=1000)` model using the same three features and `result` as the label. Predict whether the new student from Question 4 will pass or fail, then print both the number and its meaning.
df["result"] = (df["final_marks"] >= 70).astype(int)
logistic_model = LogisticRegression(max_iter=1000)
logistic_model.fit(X, df["result"])
predicted_result = logistic_model.predict(naya_student)
print(f"Predicted result for the new student: {predicted_result[0]}")
if predicted_result[0] == 1:
    print("Predicted result: Pass")
else:
    print("Predicted result: Fail")
print("="*50)
#========================================================>>>
## Question 7: Split Training and Testing Data

# Use:

# ```python
# X_train, X_test, y_train, y_test = train_test_split(
#     X,
#     y,
#     test_size=0.3,
#     random_state=42,
# )
# ```

# Print the number of training rows and testing rows.

# In a comment, explain why a model should be tested on data that it did not use for training.
X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.3,random_state=42)
print(f"Number of training rows: {X_train.shape[0]}")
print(f"Number of testing rows: {X_test.shape[0]}")
# A model should be tested on data that it did not use for training to evaluate its performance on unseen data. This helps to assess how well the model generalizes to new situations and prevents overfitting, where the model performs well on training data but poorly on new data.  
print("="*50)
#=========================================================>>>
# Question 8: Evaluate the Regression Model
# Create a new `LinearRegression` model. Train it with `X_train` and `y_train`, then predict `X_test`.
linear_model = LinearRegression()
linear_model.fit(X_train, y_train)
y_pred = linear_model.predict(X_test)
print("Actual test values:")
print(y_test.values)
print("Predicted values:")
print(y_pred)
mae = mean_absolute_error(y_test, y_pred)
print(f"Mean Absolute Error (MAE): {mae:.2f}")
r2 = r2_score(y_test, y_pred)
print(f"R² score: {r2:.2f}")
# A lower MAE indicates that the model's predictions are closer to the actual values, which means better performance. An R² value closer to 1 indicates that the model explains a higher proportion of the variance in the target variable, which also signifies better performance.    
print("="*50)
#=========================================================>>>
