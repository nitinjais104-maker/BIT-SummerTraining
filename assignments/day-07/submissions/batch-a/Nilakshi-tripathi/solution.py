import csv

rows = []

with open("sales_data.csv", "r") as file:
    reader = csv.DictReader(file)

    for row in reader:
        row["price"] = int(row["price"])
        row["quantity"] = int(row["quantity"])
        rows.append(row)

# Question 1
total_orders = len(rows)
print("Total orders:", total_orders)

# Question 2
total_units_sold = sum(row["quantity"] for row in rows)
print("Total units sold:", total_units_sold)

# Question 3
total_revenue = sum(row["price"] * row["quantity"] for row in rows)
print("Total revenue:", total_revenue)

# Question 4
average_order_revenue = round(total_revenue / total_orders, 2)
print("Average order revenue:", average_order_revenue)

# Question 5
category_revenue = {}

for row in rows:
    category = row["category"]
    revenue = row["price"] * row["quantity"]

    if category not in category_revenue:
        category_revenue[category] = 0

    category_revenue[category] += revenue

print(category_revenue)

# Question 6
city_revenue = {}

for row in rows:
    city = row["city"]
    revenue = row["price"] * row["quantity"]

    if city not in city_revenue:
        city_revenue[city] = 0

    city_revenue[city] += revenue

print(city_revenue)

# Question 7
product_revenue = {}

for row in rows:
    product = row["product"]
    revenue = row["price"] * row["quantity"]

    if product not in product_revenue:
        product_revenue[product] = 0

    product_revenue[product] += revenue

top_product = max(product_revenue, key=product_revenue.get)
print("Top product:", top_product)

# Question 8
gorakhpur_orders = []

for row in rows:
    if row["city"] == "Gorakhpur":
        gorakhpur_orders.append(row["order_id"])

print("Gorakhpur order IDs:", gorakhpur_orders)