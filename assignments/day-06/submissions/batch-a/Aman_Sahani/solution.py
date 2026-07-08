# # Day 6 Assignment

# ## Topic: Data Analytics Fundamentals With Python

# Complete all 8 questions in one file named `solution.py`.

# Use only basic Python lists, dictionaries, loops, conditions, and functions. Do not use Pandas, NumPy, or any external library.

# Use this sales data in your program:

# ```python
sales = [
    {"product": "Python Course", "category": "Online Course", "price": 999, "quantity": 2, "city": "Gorakhpur"},
    {"product": "Data Analytics Course", "category": "Online Course", "price": 1499, "quantity": 1, "city": "Lucknow"},
    {"product": "AI Workshop", "category": "Workshop", "price": 799, "quantity": 3, "city": "Gorakhpur"},
    {"product": "Python Course", "category": "Online Course", "price": 999, "quantity": 1, "city": "Deoria"},
    {"product": "Data Analytics Course", "category": "Online Course", "price": 1499, "quantity": 2, "city": "Gorakhpur"},
    {"product": "AI Workshop", "category": "Workshop", "price": 799, "quantity": 1, "city": "Lucknow"},
]


# ### Question 1: Count Orders

# Print the total number of sales records.

print("Total order:", len(sales))

# ### Question 2: Count Units Sold

# Calculate and print the total quantity sold across all records.

sold = 0
for item in sales:
    sold += item["quantity"]
print("Total units sold:", sold)

# ### Question 3: Calculate Total Revenue

# Calculate and print the total revenue from all sales records.

for item in sales:
    revenue = item["price"]*item["quantity"]
print("Total revenue:", revenue)


# ### Question 4: Filter Sales by City

# Calculate the total revenue for sales where the city is `"Gorakhpur"`.

revenue=0
for item in sales:
    if item["city"]=="Gorakhpur":
        revenue += item["price"]*item["quantity"]
print("Revenue for Gorakhpur:", revenue)

# ## Medium Questions

# ### Question 5: Revenue by Category

# Create a dictionary that stores total revenue for each category and print it.

revenue_category = {}
for item in sales:
    category = item["category"]
    revenue = item["price"]*item["quantity"]

    if category in revenue_category:
        revenue_category[category] += revenue
    else:
        revenue_category[category] = revenue
print(revenue_category)

# ### Question 6: Revenue by City

# Create a dictionary that stores total revenue for each city and print it.

revenue_city={}
for item in sales:
    city = item["city"]
    revenue = item["price"]*item["quantity"]
    if city in revenue_city:
        revenue_city[city]+= revenue
    else:
        revenue_city[city] = revenue
print(revenue_city)

# ### Question 7: Best-Selling Product by Revenue

# Find the product with the highest total revenue and print its name.

product_revenue = {}
for item in sales:
    product = item["product"]
    revenue = item["price"]*item["quantity"]
    product_revenue[product] = product_revenue.get(product, 0) + revenue
top_product = max(product_revenue, key=product_revenue.get)
print("Top product:", top_product)


# ### Question 8: High-Volume Products

# Create a list of product names for records where `quantity` is 2 or more. Keep the same order as the original data and print the list.

list1 = []
for item in sales:
    if item["quantity"]>=2:
        if item["product"] not in list1:
            list1.append(item["product"])
print(list1)
