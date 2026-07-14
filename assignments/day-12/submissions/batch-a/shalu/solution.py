### Question 1: Main Types of Machine Learning

"""Write one or two lines explaining each type:

1. Supervised learning
2. Unsupervised learning
3. Reinforcement learning"""
# Supervised Learning -- Supervised Learning is type of machine learning where the model need features and label both to train .
print("Supervised Learning is a type of machine learning which need features and labels both to train a model.")
# Unsupervised learning -- It is a type of machine lerning where the model need only features and after that the it makes grouping and clustring to train the model.
print("Unsupervised learning -- It is a type of machine lerning where the model need only features and after that the it makes grouping and clustring to train the model.")
# Reinforcement learning -- A type of machine learning where the model learns from mistake , its a punishment and reward based learning .
print("# Reinforcement learning -- A type of machine learning where the model learns from mistake , its a punishment and reward based learning .")

### Question 2: Supervised or Unsupervised?

"""Write whether each task uses supervised or unsupervised learning:

1. Predicting a new house's price from previously sold houses -- Supervised (Regression) Learning.
2. Grouping customers by their shopping behaviour without predefined labels -- Unsupervised Learning.
3. Detecting spam using emails already labelled `spam` or `not spam` -- Supervised Learning (classification)
4. Grouping news articles by topic without topic labels -- Unsupervised learning. """ 
print("1. Predicting a new house's price from previously sold houses -- Supervised (Regression) Learning.")
print("2. Grouping customers by their shopping behaviour without predefined labels -- Unsupervised Learning.")
print("3. Detecting spam using emails already labelled `spam` or `not spam` -- Supervised Learning (classification)")
print("4. Grouping news articles by topic without topic labels -- Unsupervised learning.")

### Question 3: Regression or Classification?

"""Identify each task as regression or classification:

1. Predicting tomorrow's temperature -- Regression.
2. Predicting whether a student will pass or fail -- classification.
3. Predicting the price of a second-hand bike -- Regression
4. Identifying whether an image contains a cat or a dog -- classification. """
print("1. Predicting tomorrow's temperature -- Regression.")
print("2. Predicting whether a student will pass or fail -- classification.")
print("3. Predicting the price of a second-hand bike -- Regression.")
print("4. Identifying whether an image contains a cat or a dog -- classification.")

### Question 4: Loan Application

"""A loan application uses income, credit score, age, employment type, and previous loan history to decide whether a loan should be `approved` or `rejected`.

Print:

- the learning type: supervised or unsupervised;
- the problem type: regression or classification;
- one sentence explaining your answer."""
print("The Learning type is -- Supervised")
print("The Problem type is -- Classification")
print("In this question the labels and features both are given and as we are predicting category approved or not so that's why it is a classification type Supervised Learning")

### Question 5: Customer Segmentation

"""A company has customer age, city, total purchases, application usage time, and service preference. It wants to discover customer groups, but it has no labels such as `premium` or `regular`.

Print:

- the learning type;
- the problem type;
- one sentence explaining why labels are not required."""
print("Learning type is -- Unsupervised")
print("The problem type is -- Clustring ")
print("The problem have only features to understand patterns there is no labels and the company want to discover groups of customer so the type is Unsupervised clustring Learning ")

### Question 6: Reinforcement Learning

"""Explain why teaching a robot to walk by giving positive points for correct movement and negative points for falling is reinforcement learning.

Include the words `reward` and `penalty` in your answer."""
print("It is Reinforcement learning because recieving positive points for correct movement like a reward and negative points for falling as penalty . This helps the robot to learn its own through reward and penalty ")

### Question 7: Training and Prediction

"""In your own words, explain:

1. What does `fit()` do?
2. What does `predict()` do?

Use the classroom comparison of studying and taking an exam."""
print("fit()-- When a student preparing before exam same as ,The model learns from the given train data to make a prediction. ")
print("predict()-- After preparation student give the exam same as , The model give the prediction for the test data ")

### Question 8: Underfitting and Overfitting

"""Identify each model as `underfit`, `right fit`, or `overfit`:

```text
Model A: Training accuracy = 50%, Testing accuracy = 48%
Model B: Training accuracy = 88%, Testing accuracy = 85%
Model C: Training accuracy = 99%, Testing accuracy = 60%
```

Print one short reason for each answer."""

print("Model A: Training accuracy = 50%, Testing accuracy = 48% ===== Underfit \n Reason - The model is like a lazy student not good in tarining and testing both")
print("Model B: Training accuracy = 88%, Testing accuracy = 85% ===== Right fit \n Reason - The model train and test both are done good and are close to each other ")
print("Model C: Training accuracy = 99%, Testing accuracy = 60% ===== Overfit \n Reason - The model good in training but not good in testing , it learns the patterns with noise and other mixed data ")