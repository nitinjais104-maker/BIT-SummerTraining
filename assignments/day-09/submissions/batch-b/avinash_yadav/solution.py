import pandas as pd

sales_data = {
    "product": ["Python Course", "Data Analytics Course", "AI Workshop", "Python Course", "Data Analytics Course", "AI Workshop"],
    "category": ["Online Course", "Online Course", "Workshop", "Online Course", "Online Course", "Workshop"],
    "price": [999, 1499, 799, 999, 1499, 799],
    "quantity": [2, 1, 3, 1, 2, 1],
    "city": ["Gorakhpur", "Lucknow", "Gorakhpur", "Deoria", "Gorakhpur", "Lucknow"]
}

# Question 1: Create and Print a DataFrame
df = pd.DataFrame(sales_data)
print(df)

# Question 2: Inspect the Data
print(f"Rows: {df.shape[0]}")
print(f"Columns: {df.shape[1]}")

# Question 3: Add Revenue Column
df['revenue'] = df['price'] * df['quantity']
print(df[['product', 'revenue']])

# Question 4: Total Revenue
print(f"Total revenue: {df['revenue'].sum()}")

# Question 5: Filter Gorakhpur Sales
gorakhpur_df = df[df['city'] == 'Gorakhpur']
print(gorakhpur_df[['product', 'quantity', 'revenue']])

# Question 6: Revenue by Category
print(df.groupby('category')['revenue'].sum())

# Question 7: Revenue by City
print(df.groupby('city')['revenue'].sum())

# Question 8: Top Revenue Product
top_product = df.groupby('product')['revenue'].sum().idxmax()
print(f"Top product: {top_product}")
