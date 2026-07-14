import pandas as pd

sales_data = {
    "product": ["Python Course", "Data Analytics Course", "AI Workshop", "Python Course", "Data Analytics Course", "AI Workshop"],
    "category": ["Online Course", "Online Course", "Workshop", "Online Course", "Online Course", "Workshop"],
    "price": [999, 1499, 799, 999, 1499, 799],
    "quantity": [2, 1, 3, 1, 2, 1],
    "city": ["Gorakhpur", "Lucknow", "Gorakhpur", "Deoria", "Gorakhpur", "Lucknow"]
}

df = pd.DataFrame(sales_data)
print(df)

# Question 2: Inspect the data
print(f"Rows: {df.shape[0]}")
print(f"Columns: {df.shape[1]}")

# Question 3: Add revenue column
df["revenue"] = df["price"] * df["quantity"]
print(df[["product", "revenue"]])

# Question 4: Total revenue
print(f"Total revenue: {df['revenue'].sum()}")

# Question 5: Filter Gorakhpur sales
gorakhpur_df = df[df["city"] == "Gorakhpur"]
print(gorakhpur_df[["product", "quantity", "revenue"]])

# Question 6: Revenue by category
category_revenue = df.groupby("category")["revenue"].sum().to_dict()
print(category_revenue)

# Question 7: Revenue by city
city_revenue = df.groupby("city")["revenue"].sum().to_dict()
print(city_revenue)

# Question 8: Top revenue product
top_product = df.groupby("product")["revenue"].sum().idxmax()
print(f"Top product: {top_product}")
