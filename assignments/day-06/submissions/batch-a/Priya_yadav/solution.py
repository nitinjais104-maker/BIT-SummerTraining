python_sales = [
    {"product": "Python Course", "category": "Online Course", "price": 999, "quantity": 2, "city": "Gorakhpur"},
    {"product": "Data Analytics Course", "category": "Online Course", "price": 1499, "quantity": 1, "city": "Lucknow"},
    {"product": "AI Workshop", "category": "Workshop", "price": 799, "quantity": 3, "city": "Gorakhpur"},
    {"product": "Python Course", "category": "Online Course", "price": 999, "quantity": 1, "city": "Deoria"},
    {"product": "Data Analytics Course", "category": "Online Course", "price": 1499, "quantity": 2, "city": "Gorakhpur"},
    {"product": "AI Workshop", "category": "Workshop", "price": 799, "quantity": 1, "city": "Lucknow"},
]
print("Total orders:", len(python_sales))
total_units_sold=[]
for item in python_sales:
        total_units_sold.append(item["quantity"])
print("Total units sold :",sum(total_units_sold))
total_Revenue=[]
for item in python_sales:
        total_Revenue.append(item["price"]*item["quantity"])
print("Total revenue:",sum(total_Revenue))        
gkp_revenue=[]
for item in python_sales:
        if item["city"]=="Gorakhpur":
                gkp_revenue.append(item["price"]*item["quantity"])
print("Gorakhpur revenue:",sum(gkp_revenue))
dict1={
        "Online Course":0,
        "Workshop":0
}
for item in python_sales:
        if item["category"]=="Online Course":
                dict1["Online Course"]+=(item["price"]*item["quantity"]) 
        else:
                dict1["Workshop"]+=(item["price"]*item["quantity"]) 
print(dict1)                        
dict2={"Gorakhpur": 0, "Lucknow": 0, "Deoria": 0}
for item in python_sales:
        if item["city"]=="Gorakhpur":
                dict2["Gorakhpur"]+=item["price"]*item["quantity"]  
        elif item["city"]=="Lucknow":
                dict2["Lucknow"]+=item["price"]*item["quantity"] 
        elif item["city"]=="Deoria":
          dict2["Deoria"]+=item["price"]*item["quantity"]
        else:
               pass  
print(dict2)   
highest_revenue=0
product=""
for item in python_sales:
       if item["price"]*item["quantity"]>highest_revenue:
              highest_revenue=item["price"]*item["quantity"]
              product=item["product"]
print("Top product:",product)
list1=[] 
for item in python_sales:
       if item["quantity"]>=2:
              list1.append(item["product"])
print(set(list1))
              