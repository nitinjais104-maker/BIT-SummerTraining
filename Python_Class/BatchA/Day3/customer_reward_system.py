# Rahul Tea Stall gives reward points.
# 1 tea - 10 points
# if points >= 100 -> Free Tea Coupon
# if points >= 150 -> Premium Coupon

# customers = [
#     {"name": "AMan", "tea_count": 5},
#     {"name": "Priya", "tea_count": 12},
#     {"name": "Rohit", "tea_count": 8},
#     {"name": "Simran", "tea_count": 15}
# ]

# for customer in customers:
#     points = customer["tea_count"] * 10

#     print("Customer:", customer["name"])
#     print("Tea Count:", customer["tea_count"])
#     print("Reward Points:", points)

#     if points >= 100:
#         print( " Status: Free Tea Coupon")
#     else:
#         print("Status: Not Eligible Yet")
    
#     print("-" * 45)


#Output
# Customer: Aman
# Tea Count: 5
# Reward Points: 50
# Status: Not Eligible Yet
# --------------------
# Customer: Priya
# Tea Count: 12
# Reward Points: 120
# Status: Free Tea Coupon
# --------------------

# Role + 
# Task + 
# Context + 
# Constraints + 
# Output Format + 
# Examples

# write assingment on AI

# Act as a college student

# Write an assignment on artifical intelligence

# context: 
# I am a Btech 2nd year pass out student and this is for my computer scicen subject 

# constrainsts: 
# - use simple english 
# - avoid very advanced words 
# - add real life example 
# -keep it around 500 words 
# - do not add em dash

# output format: 
# 1. Introduction
# 2. Defination of ai
# 3. uses of ai 


shop_info = (
    "Rahul Tea Stall", "GST1234", "Gurgaon"
)

# print(shop_info[0])

# shop_info[0] = "New Shop" -> shows error

# t = (10)
# s= ("val")
# print(type(s))

# t = (10,)
# s = ("val",)
# print(type(s))


# t = (1,2,[3,4])

# t[2].append(5)

# print(t)

# Cup3
# Cup2
# Cup1 - > First

# LIFO -> Last in First Out

# stack = []

# stack.append("Cup1")
# stack.append("Cup2")
# stack.append("Cup3")

# print(stack)

# print(stack.pop())

# stack = []
# if stack:
#     stack.pop()

# append = push 
# pop = remove last


# Aman
# Priya 
#Rohit
# Tea Stall Line 

# Aman Came first.
# Aman gets tea first

# FIFO -> First In First Out

# from collections import deque

# queue = deque()

# queue.append("Aman")
# queue.append("Priya")
# queue.append("Rohit")

# print(queue)

# queue.popleft()

# print(queue)

# queue = deque()

# if queue:
#     queue.popleft()


# Min Heap -> Smallest Element always on Top

# import heapq

# numbers = [50, 20, 80, 10]

# heapq.heapify(numbers)

# print(numbers)

# Sort = [10, 20, 50, 80]
# Heap => [10, 20, 80, 50]

#import heapq#

# numbers = [50, 20, 80, 10]

# heapq.heapify(numbers)

# print(numbers)

# print(heapq.heappop(numbers))

# points = [120, 300, 80, 500]

# heapq.heapify(points) #80

# print(heapq.heappop(points)) #80

# heapq.heappush(points, 50)


#nlargest() -> Useful Function

# import heapq 
# points = [120, 300, 80, 500, 200]
# top3 = heapq.nlargest(3, points)
# print(top3)

#nsmallest() -> Bootom Perfomers

import heapq 
points = [120, 300, 80, 500, 200]
last2 = heapq.nsmallest(2, points)
print(last2)