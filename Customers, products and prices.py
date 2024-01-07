products = ["Sankofa Foods", "Jamestown Coffee", "Bioko Chocolate", "Blue Skies Ice Cream", "Fair Afric Chocolate", "Kawa Moka Coffee", "Aphro Spirit", "Mensado Bissap", "Voltic"]

prices = [30, 25, 40, 20, 20, 35, 45, 50, 35]

last_week = [2, 3, 5, 8, 4, 4, 6, 2, 9]

import statistics
import numpy as np 

# The total price average for the products
print("The price average for the products is:", statistics.mean(prices))

# Create a new price list that reduces the old prices by 5
new_price = np.array([30, 25, 40, 20, 20, 35, 45, 50, 35])
new_price = new_price - 5

print(new_price)

 # Calculate total revenue generated from the products
import numpy as np
revenue = np.multiply (prices, last_week)
print(revenue)

Tot_revenue = sum(revenue)
print (Tot_revenue)
   

# Average daily revenue
Average_rev = statistics.mean(revenue)
print(Average_rev)

########### Which products are less than 30
max_price = 30

# Filter products based on the maximum price
filtered_products = [product for product, price in zip(products, new_price) if price < max_price]

# Display the filtered products
print("Products with prices less than $", max_price, ":")
for product in filtered_products:
    print(product)