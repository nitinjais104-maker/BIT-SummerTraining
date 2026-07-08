# Day 9 Assignment
#==========================================================>>>
import pandas as pd
# Use this data to create a DataFrame:
sales_data = {
    "product": ["Python Course", "Data Analytics Course", "AI Workshop", "Python Course", "Data Analytics Course", "AI Workshop"],
    "category": ["Online Course", "Online Course", "Workshop", "Online Course", "Online Course", "Workshop"],
    "price": [999, 1499, 799, 999, 1499, 799],
    "quantity": [2, 1, 3, 1, 2, 1],
    "city": ["Gorakhpur", "Lucknow", "Gorakhpur", "Deoria", "Gorakhpur", "Lucknow"]
}
#==========================================================>>>
# Question 1: Create and Print a DataFrame
# Create a DataFrame named `df` from `sales_data`. Print the DataFrame.
df = pd.DataFrame(sales_data)
print("DataFrame:\n", df)
print("="*50)
#========================================================>>>
# Question 2: Inspect the Data
# Print the number of rows and columns in this format:
print("Number of rows:", df.shape[0])
print("Number of columns:", df.shape[1])
print("="*50)
#========================================================>>>
# Question 3: Add Revenue Column
# Create a `revenue` column using `price * quantity`. Print only the `product` and `revenue` columns.
df['revenue'] = df['price'] * df['quantity']
print("Product and Revenue:\n", df[['product', 'revenue']])
print("="*50)
#========================================================>>>
# Question 4: Total Revenue
# Calculate and print the total revenue.
total_revenue = df['revenue'].sum()
print("Total Revenue:", total_revenue)
print("="*50)
#========================================================>>>
# Question 5: Filter Gorakhpur Sales
# Create a new DataFrame containing rows where the city is `Gorakhpur`. Print its `product`, `quantity`, and `revenue` columns.
gkp_sales = df[df['city'] == 'Gorakhpur']
print("Gorakhpur Sales:\n", gkp_sales[['product', 'quantity', 'revenue']])
print("="*50)
#========================================================>>>
# Question 6: Revenue by Category
# Use `groupby` to calculate and print total revenue by category.
revenue_by_category = df.groupby('category')['revenue'].sum()
print("Revenue by Category:\n", revenue_by_category)
print("="*50)
#========================================================>>>
## Question 7: Revenue by City
# Use `groupby` to calculate and print total revenue by city.
revenue_by_city = df.groupby('city')['revenue'].sum()
print("Revenue by City:\n", revenue_by_city)
print("="*50)
#========================================================>>>
## Question 8: Top Revenue Product
# Group the data by product, find the product with the highest total revenue, and print it.
top_product = df.groupby('product')['revenue'].sum().idxmax()
print("Top Revenue Product:", top_product)
print("="*50)
#========================================================>>>
