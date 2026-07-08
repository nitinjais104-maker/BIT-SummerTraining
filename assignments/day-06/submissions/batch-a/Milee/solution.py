# Sales Data
sales = [
    {"product": "Python Course", "category": "Online Course", "price": 999, "quantity": 2, "city": "Gorakhpur"},
    {"product": "Data Analytics Course", "category": "Online Course", "price": 1499, "quantity": 1, "city": "Lucknow"},
    {"product": "AI Workshop", "category": "Workshop", "price": 799, "quantity": 3, "city": "Gorakhpur"},
    {"product": "Python Course", "category": "Online Course", "price": 999, "quantity": 1, "city": "Deoria"},
    {"product": "Data Analytics Course", "category": "Online Course", "price": 1499, "quantity": 2, "city": "Gorakhpur"},
    {"product": "AI Workshop", "category": "Workshop", "price": 799, "quantity": 1, "city": "Lucknow"}
]

# Question 1: Count Orders
print("Total orders:", len(sales))

# Question 2: Count Units Sold
total_units = 0

for item in sales:
    total_units += item["quantity"]

print("Total units sold:", total_units)

# Question 3: Calculate Total Revenue
total_revenue = 0

for item in sales:
    revenue = item["price"] * item["quantity"]
    total_revenue += revenue

print("Total revenue:", total_revenue)

# Question 4: Revenue from Gorakhpur
gorakhpur_revenue = 0

for item in sales:
    if item["city"] == "Gorakhpur":
        gorakhpur_revenue += item["price"] * item["quantity"]

print("Gorakhpur revenue:", gorakhpur_revenue)

# Question 5: Revenue by Category
category_revenue = {}

for item in sales:
    category = item["category"]
    revenue = item["price"] * item["quantity"]

    if category in category_revenue:
        category_revenue[category] += revenue
    else:
        category_revenue[category] = revenue

print(category_revenue)

# Question 6: Revenue by City
city_revenue = {}

for item in sales:
    city = item["city"]
    revenue = item["price"] * item["quantity"]

    if city in city_revenue:
        city_revenue[city] += revenue
    else:
        city_revenue[city] = revenue

print(city_revenue)

# Question 7: Best-Selling Product by Revenue
product_revenue = {}

for item in sales:
    product = item["product"]
    revenue = item["price"] * item["quantity"]

    if product in product_revenue:
        product_revenue[product] += revenue
    else:
        product_revenue[product] = revenue

max_revenue = 0
top_product = ""

for product in product_revenue:
    if product_revenue[product] > max_revenue:
        max_revenue = product_revenue[product]
        top_product = product

print("Top product:", top_product)

# Question 8: High-Volume Products
high_volume_products = []

for item in sales:
    if item["quantity"] >= 2:
        high_volume_products.append(item["product"])

print(high_volume_products)