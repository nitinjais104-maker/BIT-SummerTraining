import csv
import os

current_folder = os.path.dirname(__file__)
csv_file = os.path.join(current_folder, "sales_data.csv")
with open(csv_file,"r") as file:
    reader = csv.DictReader(file)
    for row in reader:
        print(row)


### Question 1: Read the CSV File
# read all rows from `sales_data.csv` and print the total number of orders.

total_orders = 0
with open(csv_file,"r") as file:
    content = csv.DictReader(file)
    for order in content:
        total_orders += 1
print("Total orders:",total_orders)
 
 
 
###Question 2: Total Units Sold

# Calculate and print the total quantity sold.

quantity = 0
with open(csv_file,"r") as file:
    content = csv.DictReader(file)
    for value in content:
        quantity += int(value["quantity"])
print("Total units sold:",quantity)


### Question 3: Total Revenue
# Calculate and print the total revenue from the CSV data.
revenue = 0
with open(csv_file,"r") as file:
    content = csv.DictReader(file)
    for value in content:
        revenue += int(value["quantity"])*int(value["price"])

print("Total revenue:",revenue)



### Question 4: Average Order Revenue
# Calculate total revenue divided by total orders. Round the result to 2 decimal places.
revenue = 0
order = 0
with open(csv_file,"r") as file:
    content = csv.DictReader(file)
    for value in content:
        revenue += int(value["quantity"])*int(value["price"])
        order += 1
    average_revenue = revenue/order
print("Average total revenue:",round(average_revenue,2))



### Question 5: Category Revenue Report
#Create and print a dictionary of total revenue by category.
category_revenue = {}
with open (csv_file,"r") as file:
    content = csv.DictReader(file)
    for value in content:
        revenue = int(value["quantity"])*int(value["price"])
        category =  value["category"]
        if category in category_revenue:
           category_revenue[category] += revenue
        else:
           category_revenue[category] = revenue
        
print(category_revenue)



### Question 6: City Revenue Report
#Create and print a dictionary of total revenue by city.

city_revenue = {}
with open(csv_file,"r")as file:
    content = csv.DictReader(file)
    for value in content:
        revenue = int(value["quantity"])*int(value["price"])
        city = value["city"]
        if city in city_revenue:
            city_revenue[city] += revenue
        else:
            city_revenue[city] = revenue
print(city_revenue)


### Question 7: Top Product
#Find the product with the highest total revenue and print it.

highest_revenue = 0
with open (csv_file,"r") as file:
    content = csv.DictReader(file)
    
    for value in content:
        revenue = int(value["price"])*int(value["quantity"])
        if highest_revenue < revenue:
            product = value["product"]
            highest_revenue = revenue
        else:
            continue
print("Top product:",product)



### Question 8: Gorakhpur Orders
gorakhpur_order = []
with open(csv_file,'r') as file:
    content = csv.DictReader(file)
    for value in content:
        if value["city"] == "Gorakhpur":
            gorakhpur_order.append(value["order_id"])
        else:
            continue
print("Gorakhpur order IDs:",gorakhpur_order)
