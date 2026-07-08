# Import the csv module
import csv

# Open the CSV file in read mode
with open("sales_data.csv", "r") as file:
    reader = csv.DictReader(file)

    # Convert all rows into a list so we can use them multiple times
    sales = list(reader)
# Question 1: Read the CSV File
# Read all rows from sales_data.csv and print the total number of orders.
# Expected Output:
# Total orders: 6
total_orders = len(sales) # Count the total number of rows (orders)

print("Total orders:", total_orders)

# Question 2: Total Units Sold
# Calculate and print the total quantity sold.
# Expected Output:
# Total units sold: 10

total_units = 0

for row in sales:
    # Convert quantity to integer
    quantity = int(row["quantity"])
    total_units += quantity

print("Total units sold:", total_units)

# Question 3: Total Revenue
# Calculate and print the total revenue from the CSV data.
# Expected Output:
# Total revenue: 10690
total_revenue = 0

for row in sales:
    # Convert price and quantity to integers
    price = int(row["price"])
    quantity = int(row["quantity"])

    # Calculate revenue for this order
    revenue = price * quantity

    # Add to total revenue
    total_revenue += revenue

print("Total revenue:", total_revenue)

# Question 4: Average Order Revenue
# Calculate total revenue divided by total orders. Round the result to 2 decimal places.
# Expected Output:
# Average order revenue: 1781.67
average_revenue = total_revenue / total_orders

# Round to 2 decimal places
print("Average order revenue:", round(average_revenue, 2))

# Question 5: Category Revenue Report
# Create and print a dictionary of total revenue by category.
 # Expected Output:
# {'Online Course': 7494, 'Workshop': 3196}
category_revenue = {}

for row in sales:
    category = row["category"]
    price = int(row["price"])
    quantity = int(row["quantity"])

    revenue = price * quantity

    # If category already exists, add revenue
    if category in category_revenue:
        category_revenue[category] += revenue
    else:
        category_revenue[category] = revenue

print(category_revenue)

# Question 6: City Revenue Report
# Create and print a dictionary of total revenue by city.
# Expected Output:
# {'Gorakhpur': 7393, 'Lucknow': 2298, 'Deoria': 999}
city_revenue = {}

for row in sales:
    city = row["city"]
    price = int(row["price"])
    quantity = int(row["quantity"])

    revenue = price * quantity

    # If city already exists, add revenue
    if city in city_revenue:
        city_revenue[city] += revenue
    else:
        city_revenue[city] = revenue

print(city_revenue)

# Question 7: Top Product
# Find the product with the highest total revenue and print it.
# Expected Output:
# Top product: Data Analytics Course
product_revenue = {}

for row in sales:
    product = row["product"]
    price = int(row["price"])
    quantity = int(row["quantity"])

    revenue = price * quantity

    # Add revenue for each product
    if product in product_revenue:
        product_revenue[product] += revenue
    else:
        product_revenue[product] = revenue

# Find product with maximum revenue
top_product = max(product_revenue, key=product_revenue.get)

print("Top product:", top_product)

# Question 8: Gorakhpur Orders
# Create a list of order_id values where the city is "Gorakhpur".
# Keep the CSV order and print the list.
# Expected Output:
# Gorakhpur order IDs: ['ORD-001', 'ORD-003', 'ORD-005']
gorakhpur_orders = []

for row in sales:
    if row["city"] == "Gorakhpur":
        gorakhpur_orders.append(row["order_id"])

print("Gorakhpur order IDs:", gorakhpur_orders)
