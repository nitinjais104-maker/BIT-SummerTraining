
# Question 1: Main Types of Machine Learning
# Write one or two lines explaining each type:
# Supervised learning
# Unsupervised learning
# Reinforcement learning
print("MAIN TYPES OF MACHINE LEARNING")
print("-" * 65)
print("""
               MACHINE LEARNING
                      |
      --------------------------------
      |              |               |
 Supervised    Unsupervised   Reinforcement
      |              |               |
 Labelled      No Labels      Reward & Penalty
""")
print()
print("1. Supervised Learning")
print("   Learning from labelled data to predict known outputs.")
print()
print("2. Unsupervised Learning")
print("   Learning from unlabelled data to discover hidden patterns or groups.")
print()
print("3. Reinforcement Learning")
print("   Learning through interaction using rewards and penalties.")
print()


# Question 2: Supervised or Unsupervised?
# Write whether each task uses supervised or unsupervised learning:
# Predicting a new house's price from previously sold houses
# Grouping customers by their shopping behaviour without predefined labels
# Detecting spam using emails already labelled spam or not spam
# Grouping news articles by topic without topic labels
print("=" * 65)
print(" SUPERVISED OR UNSUPERVISED")
print("=" * 65)
print("House Price Prediction               : Supervised Learning")
print("Customer Behaviour Grouping          : Unsupervised Learning")
print("Spam Email Detection                 : Supervised Learning")
print("News Article Grouping                : Unsupervised Learning")
print()

# Question 3: Regression or Classification?
# Identify each task as regression or classification:
# Predicting tomorrow's temperature
# Predicting whether a student will pass or fail
# Predicting the price of a second-hand bike
# Identifying whether an image contains a cat or a dog
print("=" * 65)
print(" REGRESSION OR CLASSIFICATION")
print("=" * 65)
print("Tomorrow's Temperature              : Regression")
print("Student Pass or Fail                : Classification")
print("Second-hand Bike Price              : Regression")
print("Cat or Dog Identification           : Classification")
print()

# Question 4: Loan Application
# A loan application uses income, credit score, age, employment type, and previous loan history to decide whether a loan should be approved or rejected.
# Print:
# the learning type: supervised or unsupervised;
# the problem type: regression or classification;
# one sentence explaining your answer.
print("=" * 65)
print("LOAN APPLICATION")
print("=" * 65)
print("Learning Type : Supervised Learning")
print("Problem Type  : Classification")
print("Explanation   : The model learns from labelled loan records and predicts whether a new loan application should be approved or rejected.")
print()

# Question 5: Customer Segmentation
# A company has customer age, city, total purchases, application usage time, and service preference. It wants to discover customer groups, but it has no labels such as premium or regular.
# Print:
# the learning type;
# the problem type;
# one sentence explaining why labels are not required.
print("=" * 65)
print(" CUSTOMER SEGMENTATION")
print("=" * 65)
print("""
Customer Segmentation

 Customer Data
       |
       v
 No Labels
       |
       v
 Clustering
       |
       v
 Customer Groups
""")
print()
print("Learning Type : Unsupervised Learning")
print("Problem Type  : Clustering")
print("Explanation   : Labels are not required because the algorithm automatically discovers natural customer groups based on similarities in the data.")
print()

# Question 6: Reinforcement Learning
# Explain why teaching a robot to walk by giving positive points for correct movement and negative points for falling is reinforcement learning.
# Include the words reward and penalty in your answer.
print("=" * 65)
print("REINFORCEMENT LEARNING")
print("=" * 65)
print("""
Reinforcement Learning

   Robot
     |
     v
 Take Action
     |
     v
Reward / Penalty
     |
     v
Learn Better Action
     |
     +--------> Repeat
""")
print()
print("Teaching a robot to walk is Reinforcement Learning because")
print("it learns by trial and error, receiving a reward for correct")
print("movement and a penalty for falling, which helps improve")
print("future actions.")
print()

# Question 7: Training and Prediction
# In your own words, explain:
# What does fit() do?
# What does predict() do?
# Use the classroom comparison of studying and taking an exam.
print("=" * 65)
print("TRAINING AND PREDICTION")
print("=" * 65)
print("fit()")
print("Like studying before an exam, fit() trains the model")
print("using the training dataset so it can learn patterns.")
print()
print("predict()")
print("Like taking an exam, predict() uses the learned")
print("knowledge to make predictions on new unseen data.")
print()
print("""
Training and Prediction

 Training Data
       |
       v
     fit()
       |
       v
 Trained Model
       |
       v
   predict()
       |
       v
   Prediction
""") 
print()

# Question 8: Underfitting and Overfitting
# Identify each model as underfit, right fit, or overfit:
# Model A: Training accuracy = 50%, Testing accuracy = 48%
# Model B: Training accuracy = 88%, Testing accuracy = 85%
# Model C: Training accuracy = 99%, Testing accuracy = 60%
# Print one short reason for each answer.
print("=" * 65)
print("UNDERFITTING AND OVERFITTING")
print("=" * 65)
print("""
Model Performance

          Model
             |
    ----------------------
    |         |          |
Underfit  Right Fit  Overfit
    |         |          |
Train Low Train High Train Very High
Test Low  Test High  Test Low
""")
print()
print("Model A")
print("Result : Underfit")
print("Reason : Training accuracy (50%) and testing accuracy (48%)")
print("         are both low, showing the model has not learned")
print("         the important patterns.")
print()
print("Model B")
print("Result : Right Fit")
print("Reason : Training accuracy (88%) and testing accuracy (85%)")
print("         are both high and very close, showing good")
print("         generalization.")
print()
print("Model C")
print("Result : Overfit")
print("Reason : Training accuracy (99%) is extremely high while")
print("         testing accuracy (60%) is much lower, indicating")
print("         the model memorized the training data instead")
print("         of learning general patterns.")
print()