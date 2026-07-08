# Day 7

import csv

# Question 1: Read the CSV File
# Expected Output:
# Total orders: 6
with open("sales_data.csv", "r") as file:
    reader = csv.DictReader(file)
    sales = list(reader)
print("Total orders:", len(sales))
print()


# Question 2: Total Units Sold
# Expected Output:
# Total units sold: 10
total_units = 0
for record in sales:
    total_units += int(record["quantity"])
print("Total units sold:", total_units)
print()

# Question 3: Total Revenue
# Expected Output:
# Total revenue: 10690
total_revenue = 0
for record in sales:
    revenue = int(record["price"]) * int(record["quantity"])
    total_revenue += revenue
print("Total revenue:", total_revenue)
print()


# Question 4: Average Order Revenue
# Expected Output:
# Average order revenue: 1781.67
average = total_revenue / len(sales)
print("Average order revenue:", round(average, 2))
print()


# Question 5: Category Revenue Report
# Expected Output:
# {'Online Course': 7494, 'Workshop': 3196}
category_revenue = {}
for record in sales:
    category = record["category"]
    revenue = int(record["price"]) * int(record["quantity"])
    if category in category_revenue:
        category_revenue[category] += revenue
    else:
        category_revenue[category] = revenue
print(category_revenue)
print()


# Question 6: City Revenue Report
# Expected Output:
# {'Gorakhpur': 7393, 'Lucknow': 2298, 'Deoria': 999}
city_revenue = {}
for record in sales:
    city = record["city"]
    revenue = int(record["price"]) * int(record["quantity"])
    if city in city_revenue:
        city_revenue[city] += revenue
    else:
        city_revenue[city] = revenue
print(city_revenue)
print()


# Question 7: Top Product
# Expected Output:
# Top product: Data Analytics Course
product_revenue = {}
for record in sales:
    product = record["product"]
    revenue = int(record["price"]) * int(record["quantity"])
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
print()

# Question 8: Gorakhpur Orders
# Expected Output:
# Gorakhpur order IDs: ['ORD-001', 'ORD-003', 'ORD-005']
gorakhpur_orders = []
for record in sales:
    if record["city"] == "Gorakhpur":
        gorakhpur_orders.append(record["order_id"])
print("Gorakhpur order IDs:", gorakhpur_orders)

