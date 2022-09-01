#Program calculates the total stock worth of the cafe
#from 2 dictionaries

menu = ['Pizza', 'Burger', 'Salad', 'Lasagne']

stock = {'Pizza': 30.00, 'Burger': 50.00, 'Salad': 40.00, 'Lasagne': 76.00}

price = {'Pizza': 120.00, 'Burger': 60.00, 'Salad': 70.00, 'Lasagne': 88.00}

total = 0
#for loop calculates the values from the dictionaries keys provided
for key in price:
    amount = price[key] * stock[key]
    total += amount
    #once the total for all stock items are calculated it continues
    continue
#and prints out only the final total stock worth combined
print(f"The total stock worth is {total}")


