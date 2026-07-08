# Day 12 Assignment - Machine Learning Fundamentals

# Question 1: Main Types of Machine Learning
print("=== Question 1: Main Types of Machine Learning ===")

# Supervised Learning: Model learns from labeled data (input-output pairs).
print("Supervised Learning: Model learns from labeled data where inputs and correct outputs are provided.")

# Unsupervised Learning: Model finds patterns in data without labels.
print("Unsupervised Learning: Model finds hidden patterns or groupings in data without any labels.")

# Reinforcement Learning: Agent learns by interacting with environment using rewards and penalties.
print("Reinforcement Learning: Agent learns to make decisions by receiving rewards for correct actions and penalties for wrong ones.")


# Question 2: Supervised or Unsupervised?
print("\n=== Question 2: Supervised or Unsupervised? ===")

print("Predicting house price from previously sold houses: Supervised Learning")
print("Grouping customers by shopping behaviour without labels: Unsupervised Learning")
print("Detecting spam using labeled emails: Supervised Learning")
print("Grouping news articles by topic without labels: Unsupervised Learning")


# Question 3: Regression or Classification?
print("\n=== Question 3: Regression or Classification? ===")

print("Predicting tomorrow's temperature: Regression")
print("Predicting whether a student will pass or fail: Classification")
print("Predicting the price of a second-hand bike: Regression")
print("Identifying whether an image contains a cat or a dog: Classification")


# Question 4: Loan Application
print("\n=== Question 4: Loan Application ===")

print("Learning Type: Supervised Learning")
print("Problem Type: Classification")
print("Explanation: The model is trained on labeled data (approved/rejected) to predict one of two categories for a new application.")


# Question 5: Customer Segmentation
print("\n=== Question 5: Customer Segmentation ===")

print("Learning Type: Unsupervised Learning")
print("Problem Type: Clustering")
print("Explanation: Labels are not required because the model discovers natural groups in the data on its own without predefined categories.")


# Question 6: Reinforcement Learning
print("\n=== Question 6: Reinforcement Learning ===")

print("Teaching a robot to walk is reinforcement learning because the robot receives a reward for correct movement and a penalty for falling. Over time, the robot learns to maximise rewards and avoid penalties to improve its walking behaviour.")


# Question 7: Training and Prediction
print("\n=== Question 7: Training and Prediction ===")

print("fit(): fit() trains the model on the given data, just like a student studies before an exam. The model learns patterns and relationships from the training data.")
print("predict(): predict() uses the trained model to give output for new data, just like a student answers exam questions using what they studied.")


# Question 8: Underfitting and Overfitting
print("\n=== Question 8: Underfitting and Overfitting ===")

print("Model A: Training accuracy = 50%, Testing accuracy = 48% -> Underfit: The model has not learned enough from the training data.")
print("Model B: Training accuracy = 88%, Testing accuracy = 85% -> Right Fit: The model performs well on both training and testing data.")
print("Model C: Training accuracy = 99%, Testing accuracy = 60% -> Overfit: The model memorised training data but fails on new data.")