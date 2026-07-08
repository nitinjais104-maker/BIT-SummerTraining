
import pandas as pd

sales_data = {
    "product": ["Python Course", "Data Analytics Course", "AI Workshop", "Python Course", "Data Analytics Course", "AI Workshop"],
    "category": ["Online Course", "Online Course", "Workshop", "Online Course", "Online Course", "Workshop"],
    "price": [999, 1499, 799, 999, 1499, 799],
    "quantity": [2, 1, 3, 1, 2, 1],
    "city": ["Gorakhpur", "Lucknow", "Gorakhpur", "Deoria", "Gorakhpur", "Lucknow"]
}


### Question 1: Create and Print a DataFrame
df = pd.DataFrame(sales_data)
print(df)

### Question 2: Inspect the Data
print("Rows:",df.shape[0])
print("Columns:",df.shape[1])

### Question 3: Add Revenue Column

df["revenue"] = df["price"]*df["quantity"]
print(df[["revenue","product"]])

### Question 4: Total Revenue

total_revenue = df["revenue"].sum()
print("Total revenue:",total_revenue)


### Question 5: Filter Gorakhpur Sales

gorakhpur_sales = df[df["city"] == "Gorakhpur"]
print(gorakhpur_sales[["product","quantity","revenue"]])


### Question 6: Revenue by Category
revenue = df.groupby("category")["revenue"].sum()
for category, total in revenue.items():
    print(category,":", total)


### Question 7: Revenue by City

revenue = df.groupby("city")["revenue"].sum()
for city, total in revenue.items():
    print(city,":", total)


### Question 8: Top Revenue Product
high_revenue = 0
revenue = df.groupby("product")["revenue"].sum()
for product, total in revenue.items():
    if high_revenue < total:
        top_product = product
        high_revenue = total 
print("Top product:",top_product)