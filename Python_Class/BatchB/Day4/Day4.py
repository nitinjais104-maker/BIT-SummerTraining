# 1. LIST (a.k.a array)

# LIST = Ordered collection of items
# 
# Properties - Ordered, Mutable, 
# allows duplicates, Index Available
# 
# 
#  

# fruits = ["apple", "Banana", "Mango"]

# print(fruits[0])
# print(fruits[1])
# fruits = ["apple", "Banana", "Mango"]
# fruits.append("Orange")
# print(fruits)
# fruits.pop()
# print(fruits)
# fruits.insert(1, "Grapes")
# print(fruits)
# fruits.remove("apple")
# print(fruits)

# print(len(fruits))

# nums = [1,1,1,2,3]
# print(nums.count())

# nums = [5,2,1,8]
# nums.sort()
# print(nums)

# Edge case 

# items = []
# print(len(items))

# items = [1,2]
# print(items[5]) #-> INDEXERROR
# items.remove(10) #-> ValueError
# print(items)


# marks = [78, 90, 45, 88]
# append, pop, insert, remove, sort, len, count
# max, min, sum
# marks.append(60)
# print(marks)
# print(marks.pop())
# marks.insert(4,90)
# print(marks)
# marks.remove(90)
# print(marks)
# print(len(marks))
# marks.sort()
# print(marks)
# print(marks.count(90))
# print(max(marks))
# print(min(marks))
# print(sum(marks))

#Tuple -> Fixed LIst
# point = (10, 20)
# Properties -> Orderred, Faster, 
# Immutable, Duplicates allowed

# data = (10, 20, 30)
# print(data[0])

# nums = (1,1,2,3)
# print(nums.count(1))

# print(nums.index(2))

#Methods - count(), index()

#edge case 

# data = (10, 20)
# data[0] = 100 #-> typeerror

# x = (10)
# print(type(x))
# x = (10,)
# print(type(x))

# x = (10, 11, [1,2])
# print(x[2])
# x[2].append(3)
# print(x)

# 3. Set 
# students = {"Rahul", "Amit", "Rahul"}
# Properties - > Fast Search 

# add()

# students = {"Rahul", "Amit"}
# print(students)
# students.add("Priya")
# print(students)
# students.remove("Rahul")
# print(students)

# students = {"Amit", "Rahul", "Priya"}

# students.discard("Unknown")

# print(students)

# a = {1,2}
# b = {2,3}
# print(a.union(b))
# print(a.intersection(b))

# cities = ["Delhi", "Mumbai", "Delhi"]

# print(set(cities))

# 1. Remove duplicate marks
# marks = [80, 90, 80, 70, 90, 100]
# unique_marks = set(marks)
# print(unique_marks)

# 2. Find common players
# team_a = {"Virat", "Rohit", "Dhoni"}
# team_b = {"Rohit", "Hardik", "Dhoni"}
# common_players = team_a.intersection(team_b)
# print(common_players)

# 3. Find all unique products
# shop_1 = {"Tea", "Coffee", "Biscuit"}
# shop_2 = {"Coffee", "Juice", "Samosa"}
# all_products = shop_1.union(shop_2)
# print(all_products)


# Dictionary - > Stores key-values pair

# student = {
#     "name": "Rahul",
#     "age": 20
#     }

#properties -> Key->Value,
#  Fast Lookup, Mutable
# student = {
#     "name": "Rahul",
#     "age": 20
#     }
# print(student["name"])
# print(student.get("name"))

# print(student.keys())
# print(student.values())

# print(student.items())

# student.update({
#     "city": "Gorakhpur"
# })

# print(student)

# student.pop("age")

# print(student)

#Edge Case 
# student = {
#     "name": "Rahul",
#     "age": 20
# }

# print(student["salary"]) # -> Keyerror

# print(student.get("salary"))

# data = {
#     "name": "Rahul",
#     "name": "amit"
# }

# print(data)

# student = {
#     "name": "Priya",
#     "age": 21,
#     "course": "python"
# }

# for key in student:
#     print(key, ":", student[key])

# for key, value in student.items():
#     print(key, ":", value)

# marks = {
#     "Math": 80,
#     "English": 78,
#     "Python": 99
# }

# total = 0

# for s, i in marks.items():
#     total = total + i

# print("total marks:", total)
# print("Average marks:", total / len(marks))



cart = {
    "Tea": 2,
    "Coffee": 1,
    "Samosa": 4
}
prices = {
    "Tea": 10,
    "Coffee": 20,
    "Samosa": 15
}

total_bill = 0

for item, quantity in cart.items():
    price = prices[item]
    total = price * quantity
    total_bill = total_bill + total

print("total Bill:", total_bill)