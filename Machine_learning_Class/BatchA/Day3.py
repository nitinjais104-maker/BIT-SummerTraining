# SUPERVISED - Data + Answer 

# UNSUPERVISED = Sirf DATA


# Customer        Annual Income       Spending Score
# 1                   15                  20
# 2                   80                  85
# 3                   45                  50
# 4                   18                  25
# 5                   75                  90
# 6                   48                  45


# (income, Spending)

# (20,30)
# (30,40)
# (40,50)

# Centroid - (30,40)

# Income Avg = (20 + 30 + 40) / 3 = 30
# Spending Avg = ( 30 + 40 + 50) / 3 = 40


# Nearest centroid dhoondo
#         ↓
# Groups update karo
#         ↓
# New average nikalo
#         ↓
# Centroids shift karo
#         ↓
# Repeat


# Centroid A = (20, 20)
# Centroid B = (80, 85)
# Customer P = ( 18, 25)


# Simple Comparison: 

# P se A : 
# Income differnce - 18 - 20 = 2
# Spending difference = 25 - 20 = 5


# Euclidean distance 

# Distance from A = 