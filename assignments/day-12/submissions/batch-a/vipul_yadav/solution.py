

### Question 1: Main Types of Machine Learning
print("\nQuestion 1:")
# 1. Supervised learning--
    # Supervised learning uses labeled data to make predictions.
    #  Data + Answers = Ruels
print("Supervised learning uses labeled data to make predictions.")
print("Data + Answers = Ruels")


# 2. Unsupervised learning--
# Unsupervised learning  uses data and superate into groups 
print(" Unsupervised learning  uses data and superate into groups ")


3. # Reinforcement learning--
# Reinforcement learning learns by trial and error using revords and penalities.
print(" Reinforcement learning learns by trial and error using rewards and penalities.")




### Question 2: Supervised or Unsupervised?
print("\nQuestion 2:")
# Write whether each task uses supervised or unsupervised learning:

# 1. Predicting a new house's price from previously sold houses
# 2. Grouping customers by their shopping behaviour without predefined labels
# 3. Detecting spam using emails already labelled `spam` or `not spam`
# 4. Grouping news articles by topic without topic labels

print("Predicting a new house's price --> Supervised learning.")
print("Grouping customers --> Unsupervised learning.")
print("Detecing spam using email-->Supervised learning.")
print("Grouping news articles--> Unsupervised learning.")



### Question 3: Regression or Classification?

# Identify each task as regression or classification:

# 1. Predicting tomorrow's temperature
# 2. Predicting whether a student will pass or fail
# 3. Predicting the price of a second-hand bike
# 4. Identifying whether an image contains a cat or a dog

print("Temperaure---> Regression.")
print("Student pass or fail---> Classification.")
print("Price of second-hand bike---> Regression .")
print("Identifying whether an image contains a cat or a dog---> Classification.")

print("Question 4:")
### Question 4: Loan Application

# A loan application uses income, credit score, age, employment type, 
# and previous loan history to decide whether a loan should be `approved` or `rejected`.
# the learning type: supervised or unsupervised;
# - the problem type: regression or classification;

print("Learning Type: Supervised Learning.")
print("Problem Type: Classification.")

### Question 5: Customer Segmentation
# A company has customer age, city, total purchases, application usage time, and service preference.
# It wants to discover customer groups, but it has no labels such as `premium` or `regular`.
print("Learning Type:  Unsupervised learning.")
print("Problem Type: Clustering.")
print("Explanation: Customer categories are unknown, so the algorithm creates groups automatically without requiring labels.")

### Question 6: Reinforcement Learning
# A robot learns to walk through trial and error. "
print("Correct movements provide a reward, while falling gives a penalty. " 
"Over time the robot improves its actions to maximize rewards.")

### Question 7: Training and Prediction
# 1. What does `fit()` do?
print("fit()--> Similar to studying before an exam. ")
print("The model learns patterns and relationships from training data.")

# 2. What does `predict()` do?
print("predict()--> Similar to attempting an exam after studying. ")
print("The model uses learned knowledge to give answers for unseen data.")

### Question 8: Underfitting and Overfitting
# Model A: Training accuracy = 50%, Testing accuracy = 48%
print("Model A: Underfitting")
# Model B: Training accuracy = 88%, Testing accuracy = 85%
print("Model A: Good fit.")
# Model C: Training accuracy = 99%, Testing accuracy = 60%
print("Model A: Overfitting")