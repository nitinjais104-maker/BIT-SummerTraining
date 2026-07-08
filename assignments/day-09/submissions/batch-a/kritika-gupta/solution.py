import pandas as pd

# Given data
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

# Question 1: Create and Print DataFrame

df = pd.DataFrame(sales_data)

print("Question 1: DataFrame")
print(df)
print()


# Question 2: Inspect the Data

print("Question 2:")
print("Rows:", df.shape[0])
print("Columns:", df.shape[1])
print()


# Question 3: Add Revenue Column

df["revenue"] = df["price"] * df["quantity"]

print("Question 3:")
print(df[["product", "revenue"]])
print()


# Question 4: Total Revenue
total_revenue = df["revenue"].sum()

print("Question 4:")
print("Total revenue:", total_revenue)
print()


# Question 5: Filter Gorakhpur Sales

gorakhpur_sales = df[df["city"] == "Gorakhpur"]

print("Question 5:")
print(gorakhpur_sales[["product", "quantity", "revenue"]])
print()


# Question 6: Revenue by Category

category_revenue = df.groupby("category")["revenue"].sum()

print("Question 6:")
print(category_revenue)
print()


# Question 7: Revenue by City

city_revenue = df.groupby("city")["revenue"].sum()

print("Question 7:")
print(city_revenue)
print()


# Question 8: Top Revenue Product

product_revenue = df.groupby("product")["revenue"].sum()

top_product = product_revenue.idxmax()

print("Question 8:")
print("Top product:", top_product)