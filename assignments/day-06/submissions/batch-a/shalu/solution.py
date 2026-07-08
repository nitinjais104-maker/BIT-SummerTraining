# Use this sales data in your program:

sales = [
    {"product": "Python Course", "category": "Online Course", "price": 999, "quantity": 2, "city": "Gorakhpur"},
    {"product": "Data Analytics Course", "category": "Online Course", "price": 1499, "quantity": 1, "city": "Lucknow"},
    {"product": "AI Workshop", "category": "Workshop", "price": 799, "quantity": 3, "city": "Gorakhpur"},
    {"product": "Python Course", "category": "Online Course", "price": 999, "quantity": 1, "city": "Deoria"},
    {"product": "Data Analytics Course", "category": "Online Course", "price": 1499, "quantity": 2, "city": "Gorakhpur"},
    {"product": "AI Workshop", "category": "Workshop", "price": 799, "quantity": 1, "city": "Lucknow"},
]
### Question 1: Count Orders
# Print the total number of sales records.
# Expected Output:
# Total orders: 6
print("Total orders:",len(sales))

### Question 2: Count Units Sold

# Calculate and print the total quantity sold across all records.

# Expected Output:
# Total units sold: 10
sold=0
for item in sales:
    sold+=item["quantity"]
print("Total units sold:",sold)

### Question 3: Calculate Total Revenue

# Calculate and print the total revenue from all sales records.

# Expected Output:
# Total revenue: 10690
# revenue = price * quantity
revenue=0
for item in sales:
    revenue+=item["quantity"]*item["price"]
print("Total revenue:",revenue)

### Question 4: Filter Sales by City

# Calculate the total revenue for sales where the city is `"Gorakhpur"`.

# Expected Output:
# Gorakhpur revenue: 7393
revenue=0
for item in sales:
    if item["city"]=="Gorakhpur":
        revenue+=item["price"]*item["quantity"]
print("Gorakhpur revenue:",revenue)

### Question 5: Revenue by Category

# Create a dictionary that stores total revenue for each category and print it.

# Expected Output:
# {'Online Course': 7494, 'Workshop': 3196}

revenue_category = {}
for item in sales:
    category = item["category"]
    revenue = item["price"]*item["quantity"]

    if category in revenue_category:
        revenue_category[category] += revenue
    else:
        revenue_category[category] = revenue

print(revenue_category)

### Question 6: Revenue by City

#Create a dictionary that stores total revenue for each city and print it.

# Expected Output:
# {'Gorakhpur': 7393, 'Lucknow': 2298, 'Deoria': 999}

revenue_city={}
for item in sales:
    city=item["city"]
    revenue=item["price"]*item["quantity"]

    if city in revenue_city:
        revenue_city[city] += revenue
    else:
        revenue_city[city] = revenue
print(revenue_city)

### Question 7: Best-Selling Product by Revenue

# Find the product with the highest total revenue and print its name.

# Expected Output:
# Top product: Data Analytics Course
product_revenue = {}
for item in sales:
    product = item["product"]
    revenue = item["price"]*item["quantity"]
    product_revenue[product] = product_revenue.get(product, 0) + revenue
top_product = max(product_revenue, key=product_revenue.get)
print("Top product:", top_product)

### Question 8: High-Volume Products

# Create a list of product names for records where `quantity` is 2 or more. Keep the same order as the original data and print the list.

# Expected Output:
# ['Python Course', 'AI Workshop', 'Data Analytics Course']
list1 =[]
for item in sales:
    if item["quantity"]>=2:
        if item["product"] not in list1:
            list1.append(item["product"])
print(list1)
