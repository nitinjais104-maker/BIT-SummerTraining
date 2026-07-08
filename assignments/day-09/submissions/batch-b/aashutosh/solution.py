import pandas as pd

sales_data = {
    "product": ["Python Course", "Data Analytics Course", "AI Workshop", "Python Course", "Data Analytics Course", "AI Workshop"],
    "category": ["Online Course", "Online Course", "Workshop", "Online Course", "Online Course", "Workshop"],
    "price": [999, 1499, 799, 999, 1499, 799],
    "quantity": [2, 1, 3, 1, 2, 1],
    "city": ["Gorakhpur", "Lucknow", "Gorakhpur", "Deoria", "Gorakhpur", "Lucknow"]
}

# -----------------------------------------------------------
# Question 1: Create and Print a DataFrame
# -----------------------------------------------------------
df = pd.DataFrame(sales_data)
print("Question 1:")
print(df)
print()

# -----------------------------------------------------------
# Question 2: Inspect the Data
# -----------------------------------------------------------
rows, columns = df.shape
print("Question 2:")
print("Rows:", rows)
print("Columns:", columns)
print()

# -----------------------------------------------------------
# Question 3: Add Revenue Column
# -----------------------------------------------------------
df["revenue"] = df["price"] * df["quantity"]
print("Question 3:")
print(df[["product", "revenue"]])
print()

# -----------------------------------------------------------
# Question 4: Total Revenue
# -----------------------------------------------------------
total_revenue = df["revenue"].sum()
print("Question 4:")
print("Total revenue:", total_revenue)
print()

# -----------------------------------------------------------
# Question 5: Filter Gorakhpur Sales
# -----------------------------------------------------------
gorakhpur_df = df[df["city"] == "Gorakhpur"]
print("Question 5:")
print(gorakhpur_df[["product", "quantity", "revenue"]])
print()

# -----------------------------------------------------------
# Question 6: Revenue by Category
# -----------------------------------------------------------
revenue_by_category = df.groupby("category")["revenue"].sum()
print("Question 6:")
print(revenue_by_category)
print()

# -----------------------------------------------------------
# Question 7: Revenue by City
# -----------------------------------------------------------
revenue_by_city = df.groupby("city")["revenue"].sum()
print("Question 7:")
print(revenue_by_city)
print()

# -----------------------------------------------------------
# Question 8: Top Revenue Product
# -----------------------------------------------------------
revenue_by_product = df.groupby("product")["revenue"].sum()
top_product = revenue_by_product.idxmax()
print("Question 8:")
print("Top product:", top_product)