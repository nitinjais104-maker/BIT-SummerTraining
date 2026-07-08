# Day 7 Assignment - CSV Data Analytics With Python

import csv
import os

sales = []

current_folder = os.path.dirname(__file__)
csv_file = os.path.join(current_folder, "sales_data.csv")

with open(csv_file, "r") as file:
    reader = csv.DictReader(file)

    for row in reader:
        row["price"] = int(row["price"])
        row["quantity"] = int(row["quantity"])
        sales.append(row)


# Question 1: Read the CSV File
print("Total orders:", len(sales))


# Question 2: Total Units Sold
total_units = 0

for row in sales:
    total_units += row["quantity"]

print("Total units sold:", total_units)


# Question 3: Total Revenue
total_revenue = 0

for row in sales:
    total_revenue += row["price"] * row["quantity"]

print("Total revenue:", total_revenue)


# Question 4: Average Order Revenue
average_revenue = round(total_revenue / len(sales), 2)

print("Average order revenue:", average_revenue)


# Question 5: Category Revenue Report
category_revenue = {}

for row in sales:
    category = row["category"]
    revenue = row["price"] * row["quantity"]

    if category in category_revenue:
        category_revenue[category] += revenue
    else:
        category_revenue[category] = revenue

print(category_revenue)


# Question 6: City Revenue Report
city_revenue = {}

for row in sales:
    city = row["city"]
    revenue = row["price"] * row["quantity"]

    if city in city_revenue:
        city_revenue[city] += revenue
    else:
        city_revenue[city] = revenue

print(city_revenue)


# Question 7: Top Product
product_revenue = {}

for row in sales:
    product = row["product"]
    revenue = row["price"] * row["quantity"]

    if product in product_revenue:
        product_revenue[product] += revenue
    else:
        product_revenue[product] = revenue

top_product = max(product_revenue, key=product_revenue.get)

print("Top product:", top_product)


# Question 8: Gorakhpur Orders
gorakhpur_orders = []

for row in sales:
    if row["city"] == "Gorakhpur":
        gorakhpur_orders.append(row["order_id"])

print("Gorakhpur order IDs:", gorakhpur_orders)