### Question 1: Main Types of Machine Learning
# Write one or two lines explaining each type:
# 1. Supervised learning
# 2. Unsupervised learning
# 3. Reinforcement learning
print("Supervised learning: Uses labelled data to learn from input and output(Data + Answer).")
print("Unsupervised learning: Uses unlabelled data to find hidden patterns or clusters(Only Data).")
print("Reinforcement learning: From Data learn and give rewards and penalties based on its actions.")


# ### Question 2: Supervised or Unsupervised?
# Write whether each task uses supervised or unsupervised learning:
# 1. Predicting a new house's price from previously sold houses
print("House Price Prediction: Supervised Learning")
# 2. Grouping customers by their shopping behaviour without predefined labels
print("Customer Grouping: Unsupervised Learning")
# 3. Detecting spam using emails already labelled `spam` or `not spam`
print("Spam Emails Detection: Supervised Learning")
# 4. Grouping news articles by topic without topic labels
print("News Article Grouping: Unsupervised Learning")


# ### Question 3: Regression or Classification?
# Identify each task as regression or classification:
# 1. Predicting tomorrow's temperature
print("Predicting tomorrow's temperature: Regression")
# 2. Predicting whether a student will pass or fail
print("Predicting whether a student will pass or fail: Classification")
# 3. Predicting the price of a second-hand bike
print("Predicting the price of a second-hand bike: Regression")
# 4. Identifying whether an image contains a cat or a dog
print("Identifying whether an image contains a cat or a dog: Classification")


# ### Question 4: Loan Application
# A loan application uses income, credit score, age, employment type, and previous loan history to decide whether a loan should be `approved` or `rejected`.
# Print:
# - the learning type: supervised or unsupervised;
print("the learning type: Supervised learning")
# - the problem type: regression or classification;
print("the problem type: Classification")
# - one sentence explaining your answer.
print("It is a supervised classification problem because the model learns from labelled data to predict whether a loan should be approved or rejected.")


# ### Question 5: Customer Segmentation
# A company has customer age, city, total purchases, application usage time, and service preference. It wants to discover customer groups, but it has no labels such as `premium` or `regular`.
# Print:
# - the learning type;
print("the learning type: Unsupervised learning")
# - the problem type;
print("the problem type: Clustering")
# - one sentence explaining why labels are not required.
print("It is unsupervised clusttering problem because the model has no labels, so the model discover customer groups based on similar data by using clustering.")


# ### Question 6: Reinforcement Learning
# Explain why teaching a robot to walk by giving positive points for correct movement and negative points for falling is reinforcement learning.
# Include the words `reward` and `penalty` in your answer.
print("It is reinforcement learning because the robot learns by receiving positive points(reward) for correct movements and negative points(penalty) for falling.")


# ### Question 7: Training and Prediction
# In your own words, explain:
# 1. What does `fit()` do?
print("fit(): Trains the model using training data, like studying before an exam.")
# 2. What does `predict()` do?
print("predict(): Makes predictions on new data, like answering questions in an exam.")


# Use the classroom comparison of studying and taking an exam.
# ### Question 8: Underfitting and Overfitting
# Identify each model as `underfit`, `right fit`, or `overfit`:
# ```text
# Model A: Training accuracy = 50%, Testing accuracy = 48%
print("Model A: Underfit")
print("Reason: Both training and testing accuracy are low.")
# Model B: Training accuracy = 88%, Testing accuracy = 85%
print("Model B: Right Fit")
print("Reason: Training and testing accuracy are both high and nearly equal.")
# Model C: Training accuracy = 99%, Testing accuracy = 60%
print("Model C: Overfit")
print("Reason: Training accuracy is very high, but testing accuracy is much lower.")