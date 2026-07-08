"""
Day 6 Assignment - Data Analytics Fundamentals With Python
Only basic Python (lists, dicts, loops, conditions, functions) is used.
No Pandas / NumPy / external libraries.
"""

sales = [
    {"product": "Python Course", "category": "Online Course", "price": 999, "quantity": 2, "city": "Gorakhpur"},
    {"product": "Data Analytics Course", "category": "Online Course", "price": 1499, "quantity": 1, "city": "Lucknow"},
    {"product": "AI Workshop", "category": "Workshop", "price": 799, "quantity": 3, "city": "Gorakhpur"},
    {"product": "Python Course", "category": "Online Course", "price": 999, "quantity": 1, "city": "Deoria"},
    {"product": "Data Analytics Course", "category": "Online Course", "price": 1499, "quantity": 2, "city": "Gorakhpur"},
    {"product": "AI Workshop", "category": "Workshop", "price": 799, "quantity": 1, "city": "Lucknow"},
]


def get_revenue(record):
    """Return revenue (price * quantity) for a single sales record."""
    return record["price"] * record["quantity"]


# ---------------------------------------------------------------------
# Question 1: Count Orders
# ---------------------------------------------------------------------
def count_orders(data):
    return len(data)


total_orders = count_orders(sales)
print("Total orders:", total_orders)


# ---------------------------------------------------------------------
# Question 2: Count Units Sold
# ---------------------------------------------------------------------
def total_units_sold(data):
    total = 0
    for record in data:
        total += record["quantity"]
    return total


units_sold = total_units_sold(sales)
print("Total units sold:", units_sold)


# ---------------------------------------------------------------------
# Question 3: Calculate Total Revenue
# ---------------------------------------------------------------------
def total_revenue(data):
    total = 0
    for record in data:
        total += get_revenue(record)
    return total


overall_revenue = total_revenue(sales)
print("Total revenue:", overall_revenue)


# ---------------------------------------------------------------------
# Question 4: Filter Sales by City
# ---------------------------------------------------------------------
def revenue_by_city_filter(data, city_name):
    total = 0
    for record in data:
        if record["city"] == city_name:
            total += get_revenue(record)
    return total


gorakhpur_revenue = revenue_by_city_filter(sales, "Gorakhpur")
print("Gorakhpur revenue:", gorakhpur_revenue)


# ---------------------------------------------------------------------
# Question 5: Revenue by Category
# ---------------------------------------------------------------------
def revenue_by_category(data):
    result = {}
    for record in data:
        category = record["category"]
        result[category] = result.get(category, 0) + get_revenue(record)
    return result


category_revenue = revenue_by_category(sales)
print(category_revenue)


# ---------------------------------------------------------------------
# Question 6: Revenue by City
# ---------------------------------------------------------------------
def revenue_by_city(data):
    result = {}
    for record in data:
        city = record["city"]
        result[city] = result.get(city, 0) + get_revenue(record)
    return result


city_revenue = revenue_by_city(sales)
print(city_revenue)


# ---------------------------------------------------------------------
# Question 7: Best-Selling Product by Revenue
# ---------------------------------------------------------------------
def revenue_by_product(data):
    result = {}
    for record in data:
        product = record["product"]
        result[product] = result.get(product, 0) + get_revenue(record)
    return result


def best_selling_product(data):
    product_revenue = revenue_by_product(data)
    top_product = None
    top_revenue = -1
    for product, revenue in product_revenue.items():
        if revenue > top_revenue:
            top_revenue = revenue
            top_product = product
    return top_product


top_product = best_selling_product(sales)
print("Top product:", top_product)


# ---------------------------------------------------------------------
# Question 8: High-Volume Products
# ---------------------------------------------------------------------
def high_volume_products(data, min_quantity=2):
    result = []
    for record in data:
        if record["quantity"] >= min_quantity:
            result.append(record["product"])
    return result


high_volume = high_volume_products(sales)
print(high_volume)