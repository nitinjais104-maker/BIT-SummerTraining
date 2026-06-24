## Topic: Pandas Data Analysis
import pandas as pd
# (Ques 1) Create a DataFrame from the given sales data
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

df = pd.DataFrame(sales_data)
print(df)

print("=" * 45)

# (Ques 2) Inspect the DataFrame to find the number of rows and columns
print("Rows:", df.shape[0])
print("Columns:", df.shape[1])

print("=" * 45)

# (Ques 3) Calculate revenue for each sale
df["revenue"] = df["price"] * df["quantity"]
print(df[["product", "revenue"]])

print("=" * 45)

# (Ques 4) Calculate the total revenue generated from all sales
total_revenue = df["revenue"].sum()
print("Total revenue:", total_revenue)

print("=" * 45)


# (Ques 5) Filter sales data for a specific city
gorakhpur_sales = df[df["city"] == "Gorakhpur"]
print(gorakhpur_sales[["product", "quantity", "revenue"]])

print("=" * 45)

# (Ques 6) Calculate revenue by category
category_revenue = df.groupby("category")["revenue"].sum()
for category, revenue in category_revenue.items():
    print(f"{category}: {revenue}")

print("=" * 45)

# (Ques 7) Calculate revenue by city
city_revenue = df.groupby("city")["revenue"].sum()
for city, revenue in city_revenue.items():
    print(f"{city}: {revenue}")

print("=" * 45)

# (Ques 8) Find the product with the highest revenue
product_revenue = df.groupby("product")["revenue"].sum()
top_product = product_revenue.idxmax()
print("Top product:", top_product)

print("=" * 45)