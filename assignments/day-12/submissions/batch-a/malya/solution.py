#day 12
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
------------------------------------------------
|                  |                           |
Supervised     Unsupervised            Reinforcement
    |               |                        |
Labelled       No Labels          Reward & Penalty
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


# Question 2: Supervised or Unsupervised?
# Write whether each task uses supervised or unsupervised learning:
# Predicting a new house's price from previously sold houses
# Grouping customers by their shopping behaviour without predefined labels
# Detecting spam using emails already labelled spam or not spam
# Grouping news articles by topic without topic labels
print("SUPERVISED OR UNSUPERVISED")
print("-" * 65)
print("""
                    Machine Learning
                           |
              ----------------------------
              |                          |
      Label Available?             No Labels?
              |                          |
         Supervised              Unsupervised
""")
print()
print("1. Predicting a new house's price")
print("   Answer : Supervised Learning")
print("   Reason : Previous house prices are already available as labelled data.")
print()
print("2. Grouping customers by shopping behaviour")
print("   Answer : Unsupervised Learning")
print("   Reason : There are no predefined customer labels.")
print()
print("3. Detecting spam using labelled emails")
print("   Answer : Supervised Learning")
print("   Reason : Emails are already labelled as Spam or Not Spam.")
print()
print("4. Grouping news articles by topic")
print("   Answer : Unsupervised Learning")
print("   Reason : The articles have no topic labels.")
print()


# Question 3: Regression or Classification?
# Identify each task as regression or classification.
print("REGRESSION OR CLASSIFICATION")
print("-" * 65)

print("""
                Machine Learning Problems
                        |
             -------------------------
             |                       |
        Regression             Classification
             |                       |
     Continuous Value          Fixed Category
""")

print()

print("1. Predicting tomorrow's temperature")
print("   Answer : Regression")

print()

print("2. Predicting whether a student will pass or fail")
print("   Answer : Classification")

print()

print("3. Predicting the price of a second-hand bike")
print("   Answer : Regression")

print()

print("4. Identifying whether an image contains a cat or a dog")
print("   Answer : Classification")

print()


# Question 4: Loan Application

print("LOAN APPLICATION")

print("-" * 65)

print("""
                Loan Approval System

                     Applicant
                         |
                         v
      Income | Credit Score | Age
      Employment | Loan History
                         |
                         v
          Supervised Classification
                         |
                         v
             Approved / Rejected
""")

print()

print("Learning Type : Supervised Learning")

print()

print("Problem Type : Classification")

print()

print("Explanation")
print("The previous loan applications are already labelled as")
print("Approved or Rejected.")
print("The model learns from this labelled data and predicts")
print("whether a new loan application should be approved or rejected.")

print()


# Question 5: Customer Segmentation

print("CUSTOMER SEGMENTATION")

print("-" * 65)

print("""
                Customer Information
                         |
                         v
       Age | City | Purchases | App Usage
                         |
                         v
                No Labels Available
                         |
                         v
                  Clustering Model
                         |
                         v
             Similar Customer Groups
""")

print()

print("Learning Type : Unsupervised Learning")

print()

print("Problem Type : Clustering")

print()

print("Explanation")
print("No labels such as Premium or Regular are available.")
print("The algorithm automatically finds similar customers")
print("and creates different customer groups.")

print()


# Question 6: Reinforcement Learning

print("REINFORCEMENT LEARNING")

print("-" * 65)

print("""
                    Robot Learning

                      Robot Moves
                           |
                           v
                Environment Response
                   /               \\
                  /                 \\
             Reward             Penalty
                  \\                 /
                   \\               /
                      Learn Better
                           |
                           v
                    Improved Action
""")

print()

print("Teaching a robot to walk is Reinforcement Learning.")
print("The robot receives a reward for correct movement")
print("and a penalty whenever it falls.")
print("After many attempts it learns the best way to walk.")

print()


# Question 7: Training and Prediction

print("FIT() AND PREDICT()")

print("-" * 65)

print("""
                 Classroom Example

                  Student Studies
                         |
                         v
                       fit()
                  (Model Learns)
                         |
                         v
                  Student Gives Exam
                         |
                         v
                    predict()
                  (Model Answers)
""")

print()

print("fit()")
print("The fit() function trains the machine learning model.")
print("It is like a student studying before an examination.")

print()

print("predict()")
print("The predict() function makes predictions using")
print("the trained model.")
print("It is like a student answering questions in the exam.")

print()


# Question 8: Underfitting and Overfitting

print("UNDERFITTING AND OVERFITTING")

print("-" * 65)

print("""
            Model Performance Comparison

        Training Accuracy    Testing Accuracy

Model A       50%                 48%

Model B       88%                 85%

Model C       99%                 60%
""")

print()

print("Model A")
print("Answer : Underfit")
print("Reason : Both training and testing accuracy are low.")
print("The model has not learned enough from the training data.")

print()

print("Model B")
print("Answer : Right Fit")
print("Reason : Training and testing accuracy are high")
print("and almost equal, showing good generalization.")

print()

print("Model C")
print("Answer : Overfit")
print("Reason : Training accuracy is very high but testing")
print("accuracy is much lower because the model memorized")
print("the training data instead of learning general patterns.")