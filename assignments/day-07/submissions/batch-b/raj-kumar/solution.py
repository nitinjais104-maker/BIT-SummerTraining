
import csv
import os

rows = []

file_path = os.path.join(os.path.dirname(__file__), "sales_data.csv")

with open(file_path, "r", newline="") as file:
    reader = csv.DictReader(file)

    for row in reader:
        row["price"] = int(row["price"])
        row["quantity"] = int(row["quantity"])
        rows.append(row)

# Question 1
print("Total orders:", len(rows))

# Question 2
total_units = 0
for row in rows:
    total_units += row["quantity"]
print("Total units sold:", total_units)

# Question 3
total_revenue = 0
for row in rows:
    total_revenue += row["price"] * row["quantity"]
print("Total revenue:", total_revenue)

# Question 4
average_revenue = total_revenue / len(rows)
print("Average order revenue:", round(average_revenue, 2))

# Question 5
category_revenue = {}
for row in rows:
    revenue = row["price"] * row["quantity"]
    category = row["category"]
    if category in category_revenue:
        category_revenue[category] += revenue
    else:
        category_revenue[category] = revenue
print(category_revenue)

# Question 6
city_revenue = {}
for row in rows:
    revenue = row["price"] * row["quantity"]
    city = row["city"]
    if city in city_revenue:
        city_revenue[city] += revenue
    else:
        city_revenue[city] = revenue
print(city_revenue)

# Question 7
product_revenue = {}
for row in rows:
    revenue = row["price"] * row["quantity"]
    product = row["product"]
    if product in product_revenue:
        product_revenue[product] += revenue
    else:
        product_revenue[product] = revenue

top_product = ""
max_revenue = 0
for product in product_revenue:
    if product_revenue[product] > max_revenue:
        max_revenue = product_revenue[product]
        top_product = product

print("Top product:", top_product)

# Question 8
gorakhpur_orders = []
for row in rows:
    if row["city"] == "Gorakhpur":
        gorakhpur_orders.append(row["order_id"])

print("Gorakhpur order IDs:", gorakhpur_orders)

