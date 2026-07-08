import csv
import os

rows = []

current_folder = os.path.dirname(__file__)
csv_file = os.path.join(current_folder, "sales_data.csv")

with open(csv_file, "r") as file:
    reader = csv.DictReader(file)

    for row in reader:
        row["price"] = int(row["price"])
        row["quantity"] = int(row["quantity"])
        rows.append(row)

# Question 1: Total Orders
total_orders = len(rows)
print("Total orders:", total_orders)

# Question 2: Total Units Sold
total_units = sum(row["quantity"] for row in rows)
print("Total units sold:", total_units)

# Question 3: Total Revenue
total_revenue = sum(row["price"] * row["quantity"] for row in rows)
print("Total revenue:", total_revenue)

# Question 4: Average Order Revenue
average_revenue = round(total_revenue / total_orders, 2)
print("Average order revenue:", average_revenue)

# Question 5: Category Revenue Report
category_revenue = {}

for row in rows:
    revenue = row["price"] * row["quantity"]
    category = row["category"]

    if category not in category_revenue:
        category_revenue[category] = 0

    category_revenue[category] += revenue

print(category_revenue)

# Question 6: City Revenue Report
city_revenue = {}

for row in rows:
    revenue = row["price"] * row["quantity"]
    city = row["city"]

    if city not in city_revenue:
        city_revenue[city] = 0

    city_revenue[city] += revenue

print(city_revenue)

# Question 7: Top Product
product_revenue = {}

for row in rows:
    revenue = row["price"] * row["quantity"]
    product = row["product"]

    if product not in product_revenue:
        product_revenue[product] = 0

    product_revenue[product] += revenue

top_product = max(product_revenue, key=product_revenue.get)
print("Top product:", top_product)

# Question 8: Gorakhpur Orders
gorakhpur_orders = []

for row in rows:
    if row["city"] == "Gorakhpur":
        gorakhpur_orders.append(row["order_id"])

print("Gorakhpur order IDs:", gorakhpur_orders)