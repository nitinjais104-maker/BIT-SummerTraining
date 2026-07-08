#  Day 6 Assignment

# ## Topic: Data Analytics Fundamentals With Python

# Complete all 8 questions in one file named `solution.py`.

# Use only basic Python lists, dictionaries, loops, conditions, and functions. Do not use Pandas, NumPy, or any external library.

# Use this sales data in your program:

# ```python
# sales = [
#     {"product": "Python Course", "category": "Online Course", "price": 999, "quantity": 2, "city": "Gorakhpur"},
#     {"product": "Data Analytics Course", "category": "Online Course", "price": 1499, "quantity": 1, "city": "Lucknow"},
#     {"product": "AI Workshop", "category": "Workshop", "price": 799, "quantity": 3, "city": "Gorakhpur"},
#     {"product": "Python Course", "category": "Online Course", "price": 999, "quantity": 1, "city": "Deoria"},
#     {"product": "Data Analytics Course", "category": "Online Course", "price": 1499, "quantity": 2, "city": "Gorakhpur"},
#     {"product": "AI Workshop", "category": "Workshop", "price": 799, "quantity": 1, "city": "Lucknow"},
# ]
# ```

# For each record, revenue means:

# ```python
# revenue = price * quantity
# ```

# ## Basic Questions

# ### Question 1: Count Orders

# Print the total number of sales records.

# ```python
# # Expected Output:
# # Total orders: 6
# ```
sales = [
    {"product": "Python Course", "category": "Online Course", "price": 999, "quantity": 2, "city": "Gorakhpur"},
    {"product": "Data Analytics Course", "category": "Online Course", "price": 1499, "quantity": 1, "city": "Lucknow"},
    {"product": "AI Workshop", "category": "Workshop", "price": 799, "quantity": 3, "city": "Gorakhpur"},
    {"product": "Python Course", "category": "Online Course", "price": 999, "quantity": 1, "city": "Deoria"},
    {"product": "Data Analytics Course", "category": "Online Course", "price": 1499, "quantity": 2, "city": "Gorakhpur"},
    {"product": "AI Workshop", "category": "Workshop", "price": 799, "quantity": 1, "city": "Lucknow"},
]

print("Total orders:", len(sales))

# ### Question 2: Count Units Sold

# Calculate and print the total quantity sold across all records.

# ```python
# # Expected Output:
# # Total units sold: 10
# ```
total_units = 0

for item in sales:
    total_units += item["quantity"]

print("Total units sold:", total_units)

# ### Question 3: Calculate Total Revenue

# Calculate and print the total revenue from all sales records.

# ```python
# # Expected Output:
# # Total revenue: 10690
# ```
total_revenue = 0

for item in sales:
    total_revenue += item["price"] * item["quantity"]

print("Total revenue:", total_revenue)

# ### Question 4: Filter Sales by City

# Calculate the total revenue for sales where the city is `"Gorakhpur"`.

# ```python
# # Expected Output:
# # Gorakhpur revenue: 7393
# ```
gorakhpur_revenue = 0

for item in sales:
    if item["city"] == "Gorakhpur":
        gorakhpur_revenue += item["price"] * item["quantity"]

print("Gorakhpur revenue:", gorakhpur_revenue)

# ## Medium Questions

# ### Question 5: Revenue by Category

# Create a dictionary that stores total revenue for each category and print it.

# ```python
# # Expected Output:
# # {'Online Course': 7494, 'Workshop': 3196}
# ```
category_revenue = {}

for item in sales:
    category = item["category"]
    revenue = item["price"] * item["quantity"]

    if category in category_revenue:
        category_revenue[category] += revenue
    else:
        category_revenue[category] = revenue

print(category_revenue)

# ### Question 6: Revenue by City

# Create a dictionary that stores total revenue for each city and print it.

# ```python
# # Expected Output:
# # {'Gorakhpur': 7393, 'Lucknow': 2298, 'Deoria': 999}
# ```
city_revenue = {}

for item in sales:
    city = item["city"]
    revenue = item["price"] * item["quantity"]

    if city in city_revenue:
        city_revenue[city] += revenue
    else:
        city_revenue[city] = revenue

print(city_revenue)

# ### Question 7: Best-Selling Product by Revenue

# Find the product with the highest total revenue and print its name.

# ```python
# # Expected Output:
# # Top product: Data Analytics Course
# ```
product_revenue = {}

for item in sales:
    product = item["product"]
    revenue = item["price"] * item["quantity"]

    if product in product_revenue:
        product_revenue[product] += revenue
    else:
        product_revenue[product] = revenue

top_product = ""
max_revenue = 0

for product, revenue in product_revenue.items():
    if revenue > max_revenue:
        max_revenue = revenue
        top_product = product

print("Top product:", top_product)

# ### Question 8: High-Volume Products

# Create a list of product names for records where `quantity` is 2 or more. Keep the same order as the original data and print the list.

# ```python
# # Expected Output:
# # ['Python Course', 'AI Workshop', 'Data Analytics Course']
# ```
high_volume_products = []

for item in sales:
    if item["quantity"] >= 2:
        high_volume_products.append(item["product"])

print(high_volume_products)

