import pandas as pd

# =========================
# Sales Data
# =========================

sales_data = {
    "product": [
        "Python Course",
        "Data Analytics Course",
        "AI Workshop",
        "Python Course",
        "Data Analytics Course",
        "AI Workshop"
    ],
    "category": [
        "Online Course",
        "Online Course",
        "Workshop",
        "Online Course",
        "Online Course",
        "Workshop"
    ],
    "price": [999, 1499, 799, 999, 1499, 799],
    "quantity": [2, 1, 3, 1, 2, 1],
    "city": [
        "Gorakhpur",
        "Lucknow",
        "Gorakhpur",
        "Deoria",
        "Gorakhpur",
        "Lucknow"
    ]
}

# =========================
# Question 1: Create DataFrame
# =========================

df = pd.DataFrame(sales_data)

print("Question 1")
print(df)

# =========================
# Question 2: Inspect Data
# =========================

print("\nQuestion 2")
print("Rows:", df.shape[0])
print("Columns:", df.shape[1])

# =========================
# Question 3: Add Revenue Column
# =========================

df["revenue"] = df["price"] * df["quantity"]

print("\nQuestion 3")
print(df[["product", "revenue"]])

# =========================
# Question 4: Total Revenue
# =========================

print("\nQuestion 4")
print("Total revenue:", df["revenue"].sum())

# =========================
# Question 5: Filter Gorakhpur Sales
# =========================

gorakhpur = df[df["city"] == "Gorakhpur"]

print("\nQuestion 5")
print(gorakhpur[["product", "quantity", "revenue"]])

# =========================
# Question 6: Revenue by Category
# =========================

print("\nQuestion 6")
print(df.groupby("category")["revenue"].sum())

# =========================
# Question 7: Revenue by City
# =========================

print("\nQuestion 7")
print(df.groupby("city")["revenue"].sum())

# =========================
# Question 8: Top Revenue Product
# =========================

product_revenue = df.groupby("product")["revenue"].sum()

top_product = product_revenue.idxmax()

print("\nQuestion 8")
print("Top product:", top_product)