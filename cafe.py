'cafe.py'

"""
1. Initialize a list 'menu' with items.
2. Initialize a dictionary 'stock' with items as keys and their stock numbers as values.
3. Initialize a dictionary 'price' with items as keys and their prices as values.
4. Initialize a variable 'total_stock_worth' to 0.
5. For each item in 'menu', calculate its value by multiplying its stock number by its price.
6. Add this value to 'total_stock_worth'.
7. Print 'total_stock_worth'.
"""

# Initialize the menu list
menu = ["Coffee", "Tea", "Sandwich", "Cake"]

# Initialize the stock dictionary
stock = {"Coffee": 100, "Tea": 200, "Sandwich": 50, "Cake": 30}

# Initialize the price dictionary
price = {"Coffee": 2.5, "Tea": 2.0, "Sandwich": 5.0, "Cake": 3.5}

# Initialize the total stock worth
total_stock_worth = 0

# Calculate the total stock worth
for item in menu:
    item_value = stock[item] * price[item]  # Calculate the value of each item
    total_stock_worth += item_value  # Add the item value to the total stock worth

# Print the total stock worth
print("Total stock worth:", total_stock_worth)
