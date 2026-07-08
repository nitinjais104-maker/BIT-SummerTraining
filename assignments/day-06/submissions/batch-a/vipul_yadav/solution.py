sales = [
    {"product": "Python Course", "category": "Online Course", "price": 999, "quantity": 2, "city": "Gorakhpur"},
    {"product": "Data Analytics Course", "category": "Online Course", "price": 1499, "quantity": 1, "city": "Lucknow"},
    {"product": "AI Workshop", "category": "Workshop", "price": 799, "quantity": 3, "city": "Gorakhpur"},
    {"product": "Python Course", "category": "Online Course", "price": 999, "quantity": 1, "city": "Deoria"},
    {"product": "Data Analytics Course", "category": "Online Course", "price": 1499, "quantity": 2, "city": "Gorakhpur"},
    {"product": "AI Workshop", "category": "Workshop", "price": 799, "quantity": 1, "city": "Lucknow"},
]


### Question 1: Count Orders
orders = len(sales)
print("Total orders:",orders)


### Question 2: Count Units Sold

sold = 0
for sale in sales:
    sold += sale["quantity"]
print ("Total units sold:",sold)


### Question 3: Calculate Total Revenue
revenue = 0
for sale in sales:
    revenue += sale["quantity"] * sale["price"]
print("Total revenue:",revenue)


### Question 4: Filter Sales by City
gkp_revenue = 0
for sale in sales:
    if sale["city"] == "Gorakhpur":
        gkp_revenue += sale["quantity"] * sale["price"]
    else:
        continue
print("Gorakhpur revenue:",gkp_revenue)


### Question 5: Revenue by Category
category_revenue = {}
for sale in sales:
    revenue = sale["quantity"] * sale["price"]
    category = sale["category"]
    if category in category_revenue:
        category_revenue[category] += revenue
    else:
        category_revenue[category] = revenue

print (category_revenue)


### Question 6: Revenue by City
city_revenue = {}
for sale in sales:
    revenue = sale["quantity"] * sale["price"]
    city = sale["city"]
    if city in city_revenue:
        city_revenue [city] += revenue
    else:
        city_revenue[city] = revenue
print(city_revenue)



### Question 7: Best-Selling Product by Revenue

top_product = 0
for sale in sales:
    price = sale["quantity"] * sale["price"]
    
    if top_product < price:
        product = sale["product"]
        top_product = price
    else:
        continue
print("Top product:",product)


### Question 8: High-Volume Products

product_name = []
for sale in sales:
    quantity = sale["quantity"]
    if quantity >= 2:
        product_name.append(sale["product"])
    else:
        continue
print(product_name)