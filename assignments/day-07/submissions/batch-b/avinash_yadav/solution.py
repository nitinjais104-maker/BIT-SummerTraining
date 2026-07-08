import csv

with open('sales_data.csv', 'r') as f:
    rows = list(csv.DictReader(f))

# Question 1: Total Orders
print(f"Total orders: {len(rows)}")

# Question 2: Total Units Sold
print(f"Total units sold: {sum(int(row['quantity']) for row in rows)}")

# Question 3: Total Revenue
total_revenue = sum(int(row['price']) * int(row['quantity']) for row in rows)
print(f"Total revenue: {total_revenue}")

# Question 4: Average Order Revenue
print(f"Average order revenue: {total_revenue / len(rows):.2f}")

# Question 5: Category Revenue Report
category_revenue = {}
for row in rows:
    category = row['category']
    revenue = int(row['price']) * int(row['quantity'])
    category_revenue[category] = category_revenue.get(category, 0) + revenue
print(category_revenue)

# Question 6: City Revenue Report
city_revenue = {}
for row in rows:
    city = row['city']
    revenue = int(row['price']) * int(row['quantity'])
    city_revenue[city] = city_revenue.get(city, 0) + revenue
print(city_revenue)

# Question 7: Top Product
product_revenue = {}
for row in rows:
    product = row['product']
    revenue = int(row['price']) * int(row['quantity'])
    product_revenue[product] = product_revenue.get(product, 0) + revenue
top_product = max(product_revenue, key=product_revenue.get)
print(f"Top product: {top_product}")

# Question 8: Gorakhpur Orders
gorakhpur_orders = [row['order_id'] for row in rows if row['city'] == 'Gorakhpur']
print(f"Gorakhpur order IDs: {gorakhpur_orders}")
