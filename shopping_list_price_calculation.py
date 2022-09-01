#Program requires 3 products, each with their price and performs calculations
product1 = input("Please enter your favourite product first: ")

product2 = input("Please enter your second favourite product: ")

product3 = input("Please enter your third favourite product: ")

product1_price = float(input("Please enter the price of product 1 king: "))

product2_price = float(input("Please enter the price of product 2 champ: "))

product3_price = float(input("Lastly the price of product 3 cool kid: "))

total = product1_price + product2_price + product3_price

average_price = total / 3


#Prints out the different calculations
print(total)

print(round(average_price))

print(f"The Total of {product1}, {product2}, {product3} is R{total} and the average price of the items is R{average_price}.")

