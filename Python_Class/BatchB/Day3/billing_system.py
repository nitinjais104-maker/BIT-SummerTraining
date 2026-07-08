# Total Earning 
# How many orders are above ₹20
# Which customer get free biscuit
#Highest Order Amount
orders = [10, 20, 15, 30, 50]

total = 0
free_biscuit_count = 0
highest_order = 0

for amount in orders:
    total = total + amount 

    if amount >= 20:
        print("Order:", amount, "-Free Biscuit")
        free_biscuit_count = free_biscuit_count + 1
    else:
        print("Order:", amount, "-No Biscuit")
    
    if amount > highest_order:
        highest_order = amount

print("total earning:", total)
print("Free biscuit customers:", free_biscuit_count)
print("Highest order:", highest_order)

# Order: 10 - No biscuit
# Order: 20 - Free biscuit
# Order: 15 - No biscuit
# Order: 30 - Free biscuit
# Order: 50 - Free biscuit
# Total earning: 125
# Free biscuit customers: 3
# Highest order: 50