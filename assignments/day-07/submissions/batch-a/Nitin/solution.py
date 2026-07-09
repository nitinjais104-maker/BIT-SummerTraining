import csv

sales = []

with open("sales_data.csv", "r") as file:
    reader = csv.DictReader(file)

    for row in reader:
        row["price"] = int(row["price"])
        row["quantity"] = int(row["quantity"])
        sales.append(row)

# =========================
# Question 1
# =========================

print("Total orders:", len(sales))

# =========================
# Question 2
# =========================

total_units = 0

for item in sales:
    total_units += item["quantity"]

print("Total units sold:", total_units)

# =========================
# Question 3
# =========================

total_revenue = 0

for item in sales:
    revenue = item["price"] * item["quantity"]
    total_revenue += revenue

print("Total revenue:", total_revenue)

# =========================
# Question 4
# =========================

average = round(total_revenue / len(sales), 2)

print("Average order revenue:", average)

# =========================
# Question 5
# =========================

category_revenue = {}

for item in sales:
    revenue = item["price"] * item["quantity"]
    category = item["category"]

    if category in category_revenue:
        category_revenue[category] += revenue
    else:
        category_revenue[category] = revenue

print(category_revenue)

# =========================
# Question 6
# =========================

city_revenue = {}

for item in sales:
    revenue = item["price"] * item["quantity"]
    city = item["city"]

    if city in city_revenue:
        city_revenue[city] += revenue
    else:
        city_revenue[city] = revenue

print(city_revenue)

# =========================
# Question 7
# =========================

product_revenue = {}

for item in sales:
    revenue = item["price"] * item["quantity"]
    product = item["product"]

    if product in product_revenue:
        product_revenue[product] += revenue
    else:
        product_revenue[product] = revenue

top_product = max(product_revenue, key=product_revenue.get)

print("Top product:", top_product)

# =========================
# Question 8
# =========================

gorakhpur_orders = []

for item in sales:
    if item["city"] == "Gorakhpur":
        gorakhpur_orders.append(item["order_id"])

print("Gorakhpur order IDs:", gorakhpur_orders)