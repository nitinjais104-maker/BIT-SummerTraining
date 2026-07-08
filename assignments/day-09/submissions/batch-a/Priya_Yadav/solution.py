import pandas as pd
sales_data = {
    "product": ["Python Course", "Data Analytics Course", "AI Workshop", "Python Course", "Data Analytics Course", "AI Workshop"],
    "category": ["Online Course", "Online Course", "Workshop", "Online Course", "Online Course", "Workshop"],
    "price": [999, 1499, 799, 999, 1499, 799],
    "quantity": [2, 1, 3, 1, 2, 1],
    "city": ["Gorakhpur", "Lucknow", "Gorakhpur", "Deoria", "Gorakhpur", "Lucknow"]
}
# 1. Create a DataFrame and print it.
df = pd.DataFrame(sales_data)
print("DataFrame:")
print(df)
# 2.Inspect the Data
print("Rows:", df.shape[0])
print("Columns:", df.shape[1])
# 3. Adding Revenue Column
df["revenue"] = df["price"] * df["quantity"]
print(df[["product","revenue"]])
# 4. Total Revenue
total_revenue = df["revenue"].sum()
print("Total revenue:", total_revenue)
# 5. Filtering Gorakhpur Sales
df3= df[df["city"] == "Gorakhpur"]
print(df3[["product","quantity","revenue",]])
# 6.Revenue by category
df4=df.groupby("category")["revenue"].sum().reset_index()
print(df4)
# 7. Revenue by city
df5=df.groupby("city")["revenue"].sum().reset_index()
print(df5)
# 8. Highest product revenue 
product_revenue=df.groupby("product")["revenue"].sum()
top_product=product_revenue.idxmax()
print("Top product:",top_product) 