### Question 1: Read the CSV File
# Read all rows from `sales_data.csv` and print the total number of orders.
# # Expected Output: Total orders: 6
import csv
with open("sales_data.csv", "r") as file:
    f = csv.DictReader(file)
    total_orders = 0
    for row in f:
        total_orders += 1

print("Total orders: ",total_orders)


# ### Question 2: Total Units Sold
# Calculate and print the total quantity sold.
# # Expected Output: Total units sold: 10
with open("sales_data.csv", "r") as file:
    f_reader = csv.DictReader(file)
    total_units = 0
    for row in f_reader:
        quantity = int(row["quantity"])
        total_units += quantity

print("Total units sold: ",total_units)


# ### Question 3: Total Revenue
# Calculate and print the total revenue from the CSV data.
# # Expected Output: Total revenue: 10690
with open("sales_data.csv", "r") as file:
    f_reader = csv.DictReader(file)
    total_revenue = 0
    total_orders = 0
    
    city_revenue = {}
    category_revenue = {}
    product_revenue ={}

    for row in f_reader:
        product = row["product"]
        city = row["city"]
        category = row["category"]
        price = int(row["price"])
        quantity = int(row["quantity"])

        revenue = price * quantity
        total_revenue += revenue

        total_orders += 1                           # for question no : 04

        if category in category_revenue:            #for question no: 05
            category_revenue[category] += revenue
        else:
            category_revenue[category] = revenue

        if city in city_revenue:                     #for question number: 06
             city_revenue[city] += revenue
        else:
            city_revenue[city] = revenue

        if product in product_revenue:               #for question number: 07
            product_revenue[product] += revenue
        else:
            product_revenue[product] = revenue



print("Total revenue:", total_revenue)


### Question 4: Average Order Revenue
# Calculate total revenue divided by total orders. Round the result to 2 decimal places.
# # Expected Output: Average order revenue: 1781.67
average_revenue = round(total_revenue / total_orders, 2)
print("Average order revenue: ", average_revenue)


#### Question 5: Category Revenue Report
# Create and print a dictionary of total revenue by category.
# # Expected Output: {'Online Course': 7494, 'Workshop': 3196}
print(category_revenue)



# ### Question 6: City Revenue Report
# Create and print a dictionary of total revenue by city.
# # Expected Output: {'Gorakhpur': 7393, 'Lucknow': 2298, 'Deoria': 999}
print(city_revenue)



# ### Question 7: Top Product
# Find the product with the highest total revenue and print it.
# # Expected Output: Top product: Data Analytics Course.
top_product = max(product_revenue, key=product_revenue.get)
print(f"Top product: ", top_product)


# ### Question 8: Gorakhpur Orders
# Create a list of `order_id` values where the city is `"Gorakhpur"`. Keep the CSV order and print the list.
# # Expected Output: Gorakhpur order IDs: ['ORD-001', 'ORD-003', 'ORD-005']
with open("sales_data.csv", "r") as file:
    reader = csv.DictReader(file)

    gorakhpur_orders = []

    for row in reader:
        if row["city"] == "Gorakhpur":
            gorakhpur_orders.append(row["order_id"])

print("Gorakhpur order IDs:", gorakhpur_orders)
