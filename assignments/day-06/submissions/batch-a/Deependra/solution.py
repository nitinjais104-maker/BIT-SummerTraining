# Use only basic Python lists, dictionaries, loops, conditions, and functions.
#  Do not use Pandas, NumPy, or any external library.

# Use this sales data in your program:

sales = [
    {"product": "Python Course", "category": "Online Course", "price": 999, "quantity": 2, "city": "Gorakhpur"},
    {"product": "Data Analytics Course", "category": "Online Course", "price": 1499, "quantity": 1, "city": "Lucknow"},
    {"product": "AI Workshop", "category": "Workshop", "price": 799, "quantity": 3, "city": "Gorakhpur"},
    {"product": "Python Course", "category": "Online Course", "price": 999, "quantity": 1, "city": "Deoria"},
    {"product": "Data Analytics Course", "category": "Online Course", "price": 1499, "quantity": 2, "city": "Gorakhpur"},
    {"product": "AI Workshop", "category": "Workshop", "price": 799, "quantity": 1, "city": "Lucknow"},
]
# Question 1: Count Orders
# Print the total number of sales records.
# Expected Output:
# Total orders: 6
total_orders = len(sales)
print(" Total orders:", total_orders)

# Question 2: Count Units Sold
# Calculate and print the total quantity sold across all records.
# Expected Output:
# Total units sold: 10
total_units = 0
for sale in sales:
    total_units += sale["quantity"]
print(" Total units sold:", total_units)

# Question 3: Calculate Total Revenue
# Calculate and print the total revenue from all sales records.
# Expected Output:
# Total revenue: 10690
total_revenue = 0

for sale in sales:
    revenue = sale["price"] * sale["quantity"]
    total_revenue += revenue

print(" Total revenue:", total_revenue)

# Question 4: Filter Sales by City
# Calculate the total revenue for sales where the city is "Gorakhpur".
# Expected Output:
# Gorakhpur revenue: 7393
gorakhpur_revenue = 0
for sale in sales:
    if sale["city"] == "Gorakhpur":
        revenue = sale["price"] * sale["quantity"]
        gorakhpur_revenue += revenue

print(" Gorakhpur revenue:", gorakhpur_revenue)

# Question 5: Revenue by Category
# Create a dictionary that stores total revenue for each category and print it.
# Expected Output:
# {'Online Course': 7494, 'Workshop': 3196}
category_revenue = {}

for sale in sales:
    category = sale["category"]
    revenue = sale["price"] * sale["quantity"]

    if category not in category_revenue:
        category_revenue[category] = 0

    category_revenue[category] += revenue

print(" Revenue by category:", category_revenue)

# Question 6: Revenue by City
# Create a dictionary that stores total revenue for each city and print it.
# Expected Output:
# {'Gorakhpur': 7393, 'Lucknow': 2298, 'Deoria': 999}
city_revenue = {}

for sale in sales:
    city = sale["city"]
    revenue = sale["price"] * sale["quantity"]

    if city not in city_revenue:
        city_revenue[city] = 0

    city_revenue[city] += revenue

print(" Revenue by city:", city_revenue)

# Question 7: Best-Selling Product by Revenue
# Find the product with the highest total revenue and print its name.
# Expected Output:
# Top product: Data Analytics Course
product_revenue = {}

for sale in sales:
    product = sale["product"]
    revenue = sale["price"] * sale["quantity"]

    if product not in product_revenue:
        product_revenue[product] = 0

    product_revenue[product] += revenue

top_product = ""
max_revenue = 0

for product in product_revenue:
    if product_revenue[product] > max_revenue:
        max_revenue = product_revenue[product]
        top_product = product

print(" Top product:", top_product)

# Question 8: High-Volume Products
# Create a list of product names for records where quantity is 2 or more.
#    Keep the same order as the original data and print the list.
# Expected Output:
# ['Python Course', 'AI Workshop', 'Data Analytics Course']
high_volume_products = []

for sale in sales:
    if sale["quantity"] >= 2:
        high_volume_products.append(sale["product"])

print(" High-volume products:", high_volume_products)