# How many rows and columns are present ?
# Which column contains revenue ? 
# Which columns should be dates but are currently text ? 

#.head, .info, .tail, shape


# 1. Show only `Customer Name`, `State`, 
# and `Sales`.
# [["","",""]]
# 2. Show orders from the `East` region.
# ["Region"] == "East"
# 3. Show orders in the `Office Supplies` 
# category.
# ["Category"] == "Office Supplies"
# 4. Show Technology orders from the 
# West region.
# "Category" == "Technology" & "Region" == "West"
# 5. Check missing values and 
# duplicate rows.
# .isNull() and .duplicated()