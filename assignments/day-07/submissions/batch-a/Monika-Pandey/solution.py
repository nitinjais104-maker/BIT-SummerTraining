# # Day 7 Assignment

# ## Topic: CSV Data Analytics With Python

# Complete all 8 questions using a file named `solution.py` and a data file named `sales_data.csv`.

# Use Python's built-in `csv` module and `csv.DictReader`. Do not use Pandas, NumPy, or any external library.

# Create `sales_data.csv` in your own submission folder with this exact content:

# ```csv
# order_id,product,category,price,quantity,city
# ORD-001,Python Course,Online Course,999,2,Gorakhpur
# ORD-002,Data Analytics Course,Online Course,1499,1,Lucknow
# ORD-003,AI Workshop,Workshop,799,3,Gorakhpur
# ORD-004,Python Course,Online Course,999,1,Deoria
# ORD-005,Data Analytics Course,Online Course,1499,2,Gorakhpur
# ORD-006,AI Workshop,Workshop,799,1,Lucknow
# ```

# Convert `price` and `quantity` to integers before calculating revenue.

# ## Basic Questions

# ### Question 1: Read the CSV File

# Read all rows from `sales_data.csv` and print the total number of orders.

# ```python
# # Expected Output:
# # Total orders: 6
# ```
import csv

count = 0

with open("sales_data.csv", "r") as file:
    reader = csv.DictReader(file)

    for row in reader:
        count += 1

print("Total orders:", count)


# ### Question 2: Total Units Sold

# Calculate and print the total quantity sold.

# ```python
# # Expected Output:
# # Total units sold: 10
# ```
import csv

total_units = 0

with open("sales_data.csv", "r") as file:
    reader = csv.DictReader(file)

    for row in reader:
        total_units += int(row["quantity"])

print("Total units sold:", total_units)


# ### Question 3: Total Revenue

# Calculate and print the total revenue from the CSV data.

# ```python
# # Expected Output:
# # Total revenue: 10690
# ```
import csv

total_revenue = 0

with open("sales_data.csv", "r") as file:
    reader = csv.DictReader(file)

    for row in reader:
        revenue = int(row["price"]) * int(row["quantity"])
        total_revenue += revenue

print("Total revenue:", total_revenue)


# ### Question 4: Average Order Revenue

# Calculate total revenue divided by total orders. Round the result to 2 decimal places.

# ```python
# # Expected Output:
# # Average order revenue: 1781.67
# ```
import csv

total_orders = 0
total_revenue = 0

with open("sales_data.csv", "r") as file:
    reader = csv.DictReader(file)

    for row in reader:
        total_orders += 1
        total_revenue += int(row["price"]) * int(row["quantity"])

average = total_revenue / total_orders

print("Average order revenue:", round(average, 2))

# ## Medium Questions

# ### Question 5: Category Revenue Report

# Create and print a dictionary of total revenue by category.

# ```python
# # Expected Output:
# # {'Online Course': 7494, 'Workshop': 3196}
# ```
import csv

category_revenue = {}

with open("sales_data.csv", "r") as file:
    reader = csv.DictReader(file)

    for row in reader:
        category = row["category"]
        revenue = int(row["price"]) * int(row["quantity"])

        if category in category_revenue:
            category_revenue[category] += revenue
        else:
            category_revenue[category] = revenue

print(category_revenue)

# ### Question 6: City Revenue Report

# Create and print a dictionary of total revenue by city.

# ```python
# # Expected Output:
# # {'Gorakhpur': 7393, 'Lucknow': 2298, 'Deoria': 999}
# ```
import csv

city_revenue = {}

with open("sales_data.csv", "r") as file:
    reader = csv.DictReader(file)

    for row in reader:
        city = row["city"]
        revenue = int(row["price"]) * int(row["quantity"])

        if city in city_revenue:
            city_revenue[city] += revenue
        else:
            city_revenue[city] = revenue

print(city_revenue)

# ### Question 7: Top Product

# Find the product with the highest total revenue and print it.

# ```python
# # Expected Output:
# # Top product: Data Analytics Course
# ```
import csv

product_revenue = {}

with open("sales_data.csv", "r") as file:
    reader = csv.DictReader(file)

    for row in reader:
        product = row["product"]
        revenue = int(row["price"]) * int(row["quantity"])

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



# ### Question 8: Gorakhpur Orders

# Create a list of `order_id` values where the city is `"Gorakhpur"`. Keep the CSV order and print the list.

# ```python
# # Expected Output:
# # Gorakhpur order IDs: ['ORD-001', 'ORD-003', 'ORD-005']
# ```
import csv

gorakhpur_orders = []

with open("sales_data.csv", "r") as file:
    reader = csv.DictReader(file)

    for row in reader:
        if row["city"] == "Gorakhpur":
            gorakhpur_orders.append(row["order_id"])

print("Gorakhpur order IDs:", gorakhpur_orders)


