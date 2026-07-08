# Day 7 Assignment - CSV Data Analytics With Python

import csv

# Read CSV file
with open(r"C:\Users\hp\OneDrive\Desktop\New folder\assignment\BIT-SummerTraining\assignments\day-07\submissions\batch-a\kritika-gupta\sales_data.csv", "r") as file:
    reader = csv.DictReader(file)

    rows = []

    # Convert price and quantity to integers
    for row in reader:
        row["price"] = int(row["price"])
        row["quantity"] = int(row["quantity"])
        rows.append(row)

# Question 1: Total Orders
print("Total orders:", len(rows))


# Question 2: Total Units Sold
total_units = 0

for row in rows:
    total_units += row["quantity"]

print("Total units sold:", total_units)


# Question 3: Total Revenue
total_revenue = 0

for row in rows:
    revenue = row["price"] * row["quantity"]
    total_revenue += revenue

print("Total revenue:", total_revenue)


# Question 4: Average Order Revenue
average_revenue = total_revenue / len(rows)

print("Average order revenue:", round(average_revenue, 2))


# Question 5: Category Revenue Report
category_revenue = {}

for row in rows:
    category = row["category"]
    revenue = row["price"] * row["quantity"]

    if category in category_revenue:
        category_revenue[category] += revenue
    else:
        category_revenue[category] = revenue

print(category_revenue)


# Question 6: City Revenue Report
city_revenue = {}

for row in rows:
    city = row["city"]
    revenue = row["price"] * row["quantity"]

    if city in city_revenue:
        city_revenue[city] += revenue
    else:
        city_revenue[city] = revenue

print(city_revenue)


# Question 7: Top Product
product_revenue = {}

for row in rows:
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

for row in rows:
    if row["city"] == "Gorakhpur":
        gorakhpur_orders.append(row["order_id"])

print("Gorakhpur order IDs:", gorakhpur_orders)