#Program calculates the price of sending a parcel depending on method
#Variable prices stated below are in Rands, even for user input
package_price = float(input("Please enter the package price: "))

total_distance = float(input("Please enter the distance to deliver: "))

air = 0.36

freight = 0.25

full_insurance = 50.00

limited_insurance = 25.00

gift = 15.00

no_gift = 0.00

priority = 100.00

standard_delivery = 20.00

#User selects different options for courier method
opt_air = input("Do you prefer air courier(Yes or No in lower case letters): ").lower()
if (opt_air) == "yes":
    opt_air = air

else:
    opt_air = freight

opt_insurance = input("Do you prefer full insurance(Yes or No in lower case letters): ").lower()
if (opt_insurance) == "yes":
    opt_insurance = full_insurance

else:
    opt_insurance = limited_insurance

opt_gift = input("Do you prefer adding a gift(Yes or No in lower case letters): ").lower()
if (opt_gift) == "yes":
    opt_gift = gift

else:
    opt_gift = no_gift

opt_priority = input("Do you prefer priority delivery(Yes or No in lower case letters): ").lower()
if (opt_priority) == "yes":
    opt_priority = priority

else:
    opt_priority = standard_delivery

#Calculates the total cost
total_cost = package_price + (total_distance * opt_air) + opt_insurance + opt_gift + opt_priority

print(f"Your total is R{total_cost}")
