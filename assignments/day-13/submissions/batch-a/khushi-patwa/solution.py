## Topic: Supervised Learning With Student Data

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

# (Ques 1) Create and Inspect the DataFrame
df = pd.DataFrame(student_data)

print("Complete DataFrame:\n")
print(df)

print("\nFirst Five Rows:\n")
print(df.head())

print("\nShape:")
print(df.shape)

print("\nDescriptive Statistics:\n")
print(df.describe())

print("="*50)

# (Ques 2) Select Features and Label
X = df[["study_hours", "attendance", "previous_mark"]]

y = df["final_marks"]

print("\nFeatures:\n")
print(X.head(5))

print("\nLabel:\n")
print(y.head(5))

# X contains features because it stores the input variables
# (study hours, attendance, and previous marks) used by the model
# to learn patterns and make predictions.

# y contains the label because it represents the target value
# (final marks) that the machine learning model tries to predict.

print("="*50)

#  (Ques 3) Train a Linear Regression Model
model = LinearRegression()

model.fit(X, y)

print("\nLinear regression model trained\n")

print("="*50)

# (Ques 4) Predict a New Student's Marks
new_student = pd.DataFrame({
    "study_hours": [6],
    "attendance": [82],
    "previous_mark": [70]
})

prediction = model.predict(new_student)

print("\nPredicted Final Marks:")
print(round(prediction[0],1))

print("="*50)

# (Ques 5) Inspect Model Coefficients
# A coefficient indicates how strongly a feature influences the prediction.
# A larger positive coefficient means the feature increases the predicted value more,
# while a negative coefficient means the feature decreases the predicted value.

print("Model Coefficients:")
print(model.coef_)

print("="*50) 

# (Ques 6) Create and Predict a Pass/Fail Result
df["result"] = (df["final_marks"] >= 70).astype(int)

y_class = df["result"]

log_model = LogisticRegression(max_iter=1000)

log_model.fit(X, y_class)

result = log_model.predict(new_student)

print("\nPass or Fail Prediction:")

print("Prediction:", result[0])

if result[0] == 1:
    print(" Pass")
else:
    print(" Fail")

print("1 means pass")
print("0 means fail")

print("="*50)

# (Ques 7) Split Training and Testing Data  

X_train, X_test, y_train, y_test = train_test_split(

X,y,test_size=0.3,random_state=42
)
print("Number of Training Rows:", len(X_train))
print("Number of Testing Rows:", len(X_test))
# Training data helps the model learn patterns,
# while testing data checks whether the model can
# perform well on new data that it has never seen before.

print("="*50)

# (Ques 8) Evaluate the Regression Model
model_2 = LinearRegression()

model_2.fit(X_train, y_train)

predictions = model_2.predict(X_test)

print("\nActual Values:")

print(y_test.values)

print("\nPredicted Values:")

print(predictions)

mae = mean_absolute_error(y_test, predictions)

r2 = r2_score(y_test, predictions)

print("\nMAE:")

print(round(mae,2))

print("\nR2 Score:")

print(round(r2,2))
