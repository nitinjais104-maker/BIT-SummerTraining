import pandas as pd

# Data
sales_data = {
    "product": ["Python Course", "Data Analytics Course", "AI Workshop", "Python Course", "Data Analytics Course", "AI Workshop"],
    "category": ["Online Course", "Online Course", "Workshop", "Online Course", "Online Course", "Workshop"],
    "price": [999, 1499, 799, 999, 1499, 799],
    "quantity": [2, 1, 3, 1, 2, 1],
    "city": ["Gorakhpur", "Lucknow", "Gorakhpur", "Deoria", "Gorakhpur", "Lucknow"]
}

# Question 1: Create DataFrame
df = pd.DataFrame(sales_data)
print(df)

# Question 2: Rows and Columns
print("Rows:", df.shape[0])
print("Columns:", df.shape[1])

# Question 3: Add Revenue column
df["revenue"] = df["price"] * df["quantity"]
print(df[["product", "revenue"]])

# Question 4: Total Revenue
total_revenue = df["revenue"].sum()
print("Total revenue:", total_revenue)

# Question 5: Filter Gorakhpur Sales
gorakhpur_df = df[df["city"] == "Gorakhpur"]
print(gorakhpur_df[["product", "quantity", "revenue"]])

# Question 6: Revenue by Category
category_revenue = df.groupby("category")["revenue"].sum()
print(category_revenue)

# Question 7: Revenue by City
city_revenue = df.groupby("city")["revenue"].sum()
print(city_revenue)

# Question 8: Top Revenue Product
product_revenue = df.groupby("product")["revenue"].sum()
top_product = product_revenue.idxmax()
print("Top product:", top_product)