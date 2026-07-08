## Day 12 Assignment
#==========================================================>>>
# Machine Learning Fundamentals
# Question 1: Main Types of Machine Learning

#                            MACHINE LEARNING 
#                                   |
#             -------------------------------------------- 
#             |                     |                    | 
#       Supervised             Unsupervised          Reinforcement 
#        Learning                Learning              Learning 
#             |                     |                    |
#       Data+Answer              Only Data           Reward/Penalty
#        |       |                  |                    | 
#  Regression   Classification   Clustering          Trial and Error
    
# Supervised Learning :
# Data + Answer = Rules 
# Machine learns from old labelled data and predicts output for new data.
print("1. Supervised Learning") 
print("Data + Answer = Rules") 
print("Learns from labelled examples and predicts output for unseen data.\n") 

# Unsupervised Learning : 
# Only Data is provided. 
# Machine automatically discovers hidden patterns.
print("2. Unsupervised Learning") 
print("Only data is provided.") 
print("Machine identifies patterns and groups similar data points.\n") 

# Reinforcement Learning
# Agent learns by reward and penalty.
print("3. Reinforcement Learning")
print("Learning through reward and penalty.")
print("Agent improves decisions through trial and error.\n")
print("="*50)
#Question2: Supervised or Unsupervised
#=========================================================>>>
# Predicting a new house's price from previously sold houses:
print("House price prediction -> Supervised Learning(Regression)")
# Grouping customers by their shopping behaviour without predefined labels:
print("Customer grouping without labels -> Unsupervised Learning")
# Detecting spam using emails already labelled `spam` or `not spam`:
print("Spam detection with labelled emails -> Supervised Learning(Classification)")
# Grouping news articles by topic without topic labels:
print("Grouping news articles without labels -> Unsupervised Learning\n")
print("="*50)
#=========================================================>>>
# (Ques 3) Regression or Classification
print("Predicting tomorrow's temperature -> Regression")
print("Predicting whether a student will pass or fail -> Classification")
print("Predicting second-hand bike price -> Regression")
print("Identifying whether an image contains a cat or a dog -> Classification\n")
print("="*50)
#=========================================================>>>
# (Ques 4) Loan Application

learning_type = "Supervised Learning"
problem_type = "Classification"

print("Learning Type:", learning_type)
print("Problem Type:", problem_type)

print(
    "Explanation: Historical loan data contains labels such as approved "
    "or rejected, therefore it is supervised learning and classification.\n"
)

print("="*50)
#=========================================================>>>
# (Ques 5) Customer Segmentation

learning_type = "Unsupervised Learning"
problem_type = "Clustering"

print("Learning Type:", learning_type)
print("Problem Type:", problem_type)

print(
    "Explanation: Customer categories are unknown, so the algorithm "
    "creates groups automatically without requiring labels.\n"
)

print("="*50)
#========================================================>>>
# (Ques 6) Reinforcement Learning
print(
    "A robot learns to walk through trial and error. "
    "Correct movements provide a reward, while falling gives a penalty. "
    "Over time the robot improves its actions to maximize rewards.\n"
)
print("="*50)
# (Ques 7) fit() and predict()
#=========================================================>>>
print(
    "fit(): Similar to studying before an exam. "
    "The model learns patterns and relationships from training data."
)
print(
    "predict(): Similar to attempting an exam after studying. "
    "The model uses learned knowledge to give answers for unseen data.\n"
)
print("="*50)
# (Ques 8) Underfitting and Overfitting
#=========================================================>>>
print("Model A -> Underfit")
print("Reason: Training and testing accuracies are both low.")
print()
print("Model B -> Right Fit")
print("Reason: Training and testing accuracies are high and close to each other.")
print()
print("Model C -> Overfit")
print("Reason: Training accuracy is very high but testing accuracy is much lower.\n")
