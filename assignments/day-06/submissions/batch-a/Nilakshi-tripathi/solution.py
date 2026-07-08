# Day 6 Assignment Solution

sales = [
    {"product": "Python Course", "category": "Online Course", "price": 999, "quantity": 2, "city": "Gorakhpur"},
    {"product": "Data Analytics Course", "category": "Online Course", "price": 1499, "quantity": 1, "city": "Lucknow"},
    {"product": "AI Workshop", "category": "Workshop", "price": 799, "quantity": 3, "city": "Gorakhpur"},
    {"product": "Python Course", "category": "Online Course", "price": 999, "quantity": 1, "city": "Deoria"},
    {"product": "Data Analytics Course", "category": "Online Course", "price": 1499, "quantity": 2, "city": "Gorakhpur"},
    {"product": "AI Workshop", "category": "Workshop", "price": 799, "quantity": 1, "city": "Lucknow"},
]


# Question 1: Count Orders

print("Total orders:", len(sales))


# Question 2: Total Units Sold

total_units = 0
for s in sales:
    total_units += s["quantity"]

print("Total units sold:", total_units)


# Question 3: Total Revenue

total_revenue = 0
for s in sales:
    total_revenue += s["price"] * s["quantity"]

print("Total revenue:", total_revenue)


# Question 4: Gorakhpur Revenue

gorakhpur_revenue = 0
for s in sales:
    if s["city"] == "Gorakhpur":
        gorakhpur_revenue += s["price"] * s["quantity"]

print("Gorakhpur revenue:", gorakhpur_revenue)


# Question 5: Revenue by Category

revenue_by_category = {}

for s in sales:
    revenue = s["price"] * s["quantity"]
    category = s["category"]

    if category in revenue_by_category:
        revenue_by_category[category] += revenue
    else:
        revenue_by_category[category] = revenue

print(revenue_by_category)


# Question 6: Revenue by City

revenue_by_city = {}

for s in sales:
    revenue = s["price"] * s["quantity"]
    city = s["city"]

    if city in revenue_by_city:
        revenue_by_city[city] += revenue
    else:
        revenue_by_city[city] = revenue

print(revenue_by_city)


# Question 7: Best-Selling Product by Revenue

product_revenue = {}

for s in sales:
    revenue = s["price"] * s["quantity"]
    product = s["product"]

    if product in product_revenue:
        product_revenue[product] += revenue
    else:
        product_revenue[product] = revenue


top_product = ""
max_revenue = 0

for product, rev in product_revenue.items():
    if rev > max_revenue:
        max_revenue = rev
        top_product = product

print("Top product:", top_product)


# Question 8: High Volume Products

high_volume_products = []

for s in sales:
    if s["quantity"] >= 2:
        high_volume_products.append(s["product"])

print(high_volume_products)