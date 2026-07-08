# Day 6 Assignment
#==========================================================>>>
#Use this sales data in your program:
sales = [
    {"product": "Python Course", "category": "Online Course", "price": 999, "quantity": 2, "city": "Gorakhpur"},
    {"product": "Data Analytics Course", "category": "Online Course", "price": 1499, "quantity": 1, "city": "Lucknow"},
    {"product": "AI Workshop", "category": "Workshop", "price": 799, "quantity": 3, "city": "Gorakhpur"},
    {"product": "Python Course", "category": "Online Course", "price": 999, "quantity": 1, "city": "Deoria"},
    {"product": "Data Analytics Course", "category": "Online Course", "price": 1499, "quantity": 2, "city": "Gorakhpur"},
    {"product": "AI Workshop", "category": "Workshop", "price": 799, "quantity": 1, "city": "Lucknow"},
]
#==========================================================>>>
# Question 1: Count Orders
#Print the total number of sales records.
print(f"Total number of sales records: {len(sales)}")
print("="*50)
#=========================================================>>>
# Question 2: Count Units Sold
#Calculate and print the total quantity sold across all records.
sold=0
for item in sales:
    sold+=item["quantity"]
print(f"Total quantity sold across all records: {sold}")
print("="*50)
#========================================================>>>
## Question 3: Calculate Total Revenue
# Calculate and print the total revenue from all sales records.
revenue = 0
for i in sales:
    revenue += i["price"] * i["quantity"]
print("Total revenue:", revenue)
print("="*50)
#========================================================>>>
# Question 4: Filter Sales by City
# Calculate the total revenue for sales where the city is `"Gorakhpur"`.
gkp = 0
for i in sales:
    if i["city"] == "Gorakhpur":
        gkp += i["price"] * i["quantity"]
print("Gorakhpur revenue:", gkp)
print("="*50)
#========================================================>>>
# Question 5: Revenue by Category
#Create a dictionary that stores total revenue for each category and print it.
category = {}
for i in sales:
    category[i["category"]] = category.get(i["category"], 0) + i["price"] * i["quantity"]
print(category)
print("="*50)
#========================================================>>>
#Question 6: Revenue by City
# Create a dictionary that stores total revenue for each city and print it.
city = {}
for i in sales:
    city[i["city"]] = city.get(i["city"], 0) + i["price"] * i["quantity"]
print(city)
print("="*50)
#========================================================>>>
## Question 7: Best-Selling Product by Revenue
# Find the product with the highest total revenue and print its name.
product = {}
for i in sales:
    product[i["product"]] = product.get(i["product"], 0) + i["price"] * i["quantity"]
print("Top product:", max(product, key=product.get))
print("="*50)
#========================================================>>>
## Question 8: High-Volume Products
# Create a list of product names for records where `quantity` is 2 or more. Keep the same order as the original data and print the list.
result = []
for i in sales:
    if i["quantity"] >= 2:
        result.append(i["product"])
print(result)
print("="*50)
