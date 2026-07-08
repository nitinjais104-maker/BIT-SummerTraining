# Day 7 Assignment
#==========================================================>>>
import csv
# Question 1: Read the CSV File
# Read all rows from `sales_data.csv` and print the total number of orders.
with open("sales_data.csv", "r") as file:
    data = list(csv.DictReader(file))
print("Total orders:", len(data))
print("="*50)
#==========================================================>>>
# Question 2: Total Units Sold
# Calculate and print the total quantity sold.
total = 0
with open("sales_data.csv", "r") as file:
    data = csv.DictReader(file)
    for i in data:
        total += int(i["quantity"])
print("Total units sold:", total)
print("="*50)
#==========================================================>>>
## Question 3: Total Revenue
# Calculate and print the total revenue from the CSV data.
revenue = 0
with open("sales_data.csv", "r") as file:
    data = csv.DictReader(file)
    for i in data:
        revenue += int(i["price"]) * int(i["quantity"])
print("Total revenue:", revenue)
print("="*50)
#==========================================================>>>
## Question 4: Average Order Revenue
# Calculate total revenue divided by total orders. Round the result to 2 decimal places.
with open("sales_data.csv", "r") as file:
    data = list(csv.DictReader(file))
print("Average order revenue:", round(revenue / len(data), 2))
print("="*50)
#==========================================================>>>
## Question 5: Category Revenue Report
# Create and print a dictionary of total revenue by category.
with open("sales_data.csv", "r") as file:
    data = csv.DictReader(file)
    category_revenue = {}
    for i in data:
        category = i["category"]
        revenue = int(i["price"]) * int(i["quantity"])
        if category in category_revenue:
            category_revenue[category] += revenue
        else:
            category_revenue[category] = revenue
print("Total revenue by category:", category_revenue)
print("="*50)
#========================================================>>>
# Question 6: City Revenue Report
# Create and print a dictionary of total revenue by city.
with open("sales_data.csv", "r") as file:
    data = csv.DictReader(file)
    city_revenue = {}
    for i in data:
        city = i["city"]
        revenue = int(i["price"]) * int(i["quantity"])
        if city in city_revenue:
            city_revenue[city] += revenue
        else:
            city_revenue[city] = revenue
print("Total revenue by city:", city_revenue)
print("="*50)
#========================================================>>>
# Question 7: Top Product
# Find the product with the highest total revenue and print it.
with open("sales_data.csv", "r") as file:
    data = csv.DictReader(file)
    product_revenue = {}
    for i in data:
        product = i["product"]
        revenue = int(i["price"]) * int(i["quantity"])
        if product in product_revenue:
            product_revenue[product] += revenue
        else:
            product_revenue[product] = revenue
top_product = max(product_revenue, key=product_revenue.get)
print("Top product:", top_product)
print("="*50)
#========================================================>>>
# Question 8: Gorakhpur Orders
# Create a list of `order_id` values where the city is `"Gorakhpur"`. Keep the CSV order and print the list.
with open("sales_data.csv", "r") as file:
    data = csv.DictReader(file)
    gorakhpur_orders = [i["order_id"] for i in data if i["city"] == "Gorakhpur"]
print("Gorakhpur orders id:", gorakhpur_orders)
print("="*50)
#========================================================>>>