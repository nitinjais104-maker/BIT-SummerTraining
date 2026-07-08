# ==========================
# Day 12 Assignment
# Topic: Machine Learning Fundamentals
# ==========================

# --------------------------
# Question 1: Main Types of Machine Learning
# --------------------------

# Supervised Learning:
# In supervised learning, the model learns from labelled data to make predictions.
print("1. Supervised Learning: The model learns from labelled data to predict outputs.")

# Unsupervised Learning:
# In unsupervised learning, the model finds hidden patterns or groups in unlabelled data.
print("2. Unsupervised Learning: The model finds patterns or groups in data without labels.")

# Reinforcement Learning:
# In reinforcement learning, an agent learns by interacting with the environment using rewards and penalties.
print("3. Reinforcement Learning: The agent learns through rewards and penalties while interacting with the environment.")

print("\n" + "="*60)

# --------------------------
# Question 2: Supervised or Unsupervised?
# --------------------------

# Predicting house price from previous data -> Supervised
print("1. House price prediction: Supervised Learning")

# Grouping customers without labels -> Unsupervised
print("2. Customer grouping: Unsupervised Learning")

# Spam detection using labelled emails -> Supervised
print("3. Spam detection: Supervised Learning")

# Grouping news articles without labels -> Unsupervised
print("4. News article grouping: Unsupervised Learning")

print("\n" + "="*60)

# --------------------------
# Question 3: Regression or Classification?
# --------------------------

# Predicting tomorrow's temperature -> Regression
print("1. Tomorrow's temperature: Regression")

# Predicting pass or fail -> Classification
print("2. Student pass/fail: Classification")

# Predicting bike price -> Regression
print("3. Second-hand bike price: Regression")

# Cat or dog image -> Classification
print("4. Cat or Dog image: Classification")

print("\n" + "="*60)

# --------------------------
# Question 4: Loan Application
# --------------------------

# Loan approval uses labelled data (approved/rejected)
print("Learning Type: Supervised Learning")
print("Problem Type: Classification")
print("Explanation: The model learns from labelled loan data and predicts whether a loan will be approved or rejected.")

print("\n" + "="*60)

# --------------------------
# Question 5: Customer Segmentation
# --------------------------

# No labels are available
print("Learning Type: Unsupervised Learning")
print("Problem Type: Clustering")
print("Explanation: Labels are not required because the model automatically discovers similar customer groups.")

print("\n" + "="*60)

# --------------------------
# Question 6: Reinforcement Learning
# --------------------------

# Robot learns using rewards and penalties
print("A robot learns through reward for correct movements and penalty for falling, so it improves its actions over time. This is Reinforcement Learning.")

print("\n" + "="*60)

# --------------------------
# Question 7: Training and Prediction
# --------------------------

# fit()
print("1. fit(): It is like studying before an exam. The model learns from the training data.")

# predict()
print("2. predict(): It is like taking the exam. The model uses what it learned to make predictions on new data.")

print("\n" + "="*60)

# --------------------------
# Question 8: Underfitting and Overfitting
# --------------------------

# Model A
print("Model A: Underfit")
print("Reason: Both training and testing accuracy are low.")

print()

# Model B
print("Model B: Right Fit")
print("Reason: Training and testing accuracy are both high and very close.")

print()

# Model C
print("Model C: Overfit")
print("Reason: Training accuracy is very high, but testing accuracy is much lower.")