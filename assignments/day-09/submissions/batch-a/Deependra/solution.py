# Use this data to create a DataFrame:

sales_data = {
    "product": ["Python Course", "Data Analytics Course", "AI Workshop", "Python Course", "Data Analytics Course", "AI Workshop"],
    "category": ["Online Course", "Online Course", "Workshop", "Online Course", "Online Course", "Workshop"],
    "price": [999, 1499, 799, 999, 1499, 799],
    "quantity": [2, 1, 3, 1, 2, 1],
    "city": ["Gorakhpur", "Lucknow", "Gorakhpur", "Deoria", "Gorakhpur", "Lucknow"]
}
# Question 1: Create and Print a DataFrame
# Create a DataFrame named df from sales_data. Print the DataFrame.
import pandas as pd
df = pd.DataFrame(sales_data)
# Print the DataFrame
print(df)

# Question 2: Inspect the Data
# Print the number of rows and columns in this format:
# Expected Output:
# Rows: 6
# Columns: 5

# Get the number of rows and columns
rows, columns = df.shape
print("\nRows:", rows)
print("Columns:", columns)

# Question 3: Add Revenue Column
# Create a revenue column using price * quantity. Print only the product and revenue columns.

# Create a new column named 'revenue'
df["revenue"] = df["price"] * df["quantity"]
print(df[["product", "revenue"]])

# Question 4: Total Revenue
# Calculate and print the total revenue.
# Expected Output:
# Total revenue: 10690
# Find the total revenue
total_revenue = df["revenue"].sum()
print("\nTotal revenue:", total_revenue)

# Question 5: Filter Gorakhpur Sales
# Create a new DataFrame containing rows where the city is Gorakhpur. 
# Print its product, quantity, and revenue columns.

# Select only rows where city is Gorakhpur
gorakhpur_sales = df[df["city"] == "Gorakhpur"]
print('\n')
print(gorakhpur_sales[["product", "quantity", "revenue"]])

# Question 6: Revenue by Category
# Use groupby to calculate and print total revenue by category.
# Expected Values:
# Online Course: 7494
# Workshop: 3196

# Group data by category and calculate total revenue
category_revenue = df.groupby("category")["revenue"].sum()
print('\n',category_revenue)

# Question 7: Revenue by City
# Use groupby to calculate and print total revenue by city.
# Expected Values:
# Deoria: 999
# Gorakhpur: 7393
# Lucknow: 2298
# Group data by city and calculate total revenue
city_revenue = df.groupby("city")["revenue"].sum()

print('\n',city_revenue)

# Question 8: Top Revenue Product
# Group the data by product, find the product with the highest total revenue, and print it.
# Expected Output:
# Top product: Data Analytics Course
# Calculate total revenue for each product
product_revenue = df.groupby("product")["revenue"].sum()

# Find the product with the highest revenue
top_product = product_revenue.idxmax()
print("\nTop product:", top_product)