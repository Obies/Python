#This program performs calculations for an investment or bond
#we import the math module to help with calculations
import math

#3 messages are printed to be displayed to the user before entering input
print("Choose either 'investment' or 'bond' from the menu  below to proceed:\n")

print("investment      - to calculate the amount of interest you'll earn on investment")
print("bond            - to calculate the amount you'll have to pay on a home loan\n")

#Receive input from the users selection using input method
investment_or_bond = input("Please type your selection from above: ").lower()

#if statement is used to require basic information from the user in terms of option selection
if investment_or_bond == "investment":
    deposit = float(input("\nHow much is your deposit?: "))
    interest_rate = int(input("\nHow much is the interest rate?: "))
    num_of_years = int(input("\nHow many years would you like to invest?: "))
    simple_compound_interest = input("\nDo you prefer simple interest or compound interest?: ").lower()
    
    #Another if statement is used based on the type of interest the user selects
    #Begins with simple interest total calculation
    if simple_compound_interest == "simple":
        simple_total = deposit * (1 + (interest_rate / 100) * num_of_years)
        print("\nYou will receive {} after {} years at an {}% interest rate.".format(simple_total, num_of_years, interest_rate))

    #elif statement is used if the user selects compound interest
    elif simple_compound_interest == "compound":
        compound_total = deposit *(pow((1 + interest_rate / 100), num_of_years))
        print("\nYou will receive {} after {} years at an {}% interest rate.".format(compound_total, num_of_years, interest_rate))

#elif statement is used when the user selects bond from the option selection
#calculation is performed for bond repayment amount
elif investment_or_bond == "bond":
    present_value_house = int(input("\nWhat is the present value of the house?: "))
    bond_int_rate = int(input("\nWhat is the interest rate charged on the bond?: "))
    bond_int_rate = (bond_int_rate / 100) / 12
    number_of_months = int(input("\nOver how many months are you repaying the bond?: "))
    bond_repayment = (bond_int_rate * present_value_house) / (1 - (1 + bond_int_rate)**(-number_of_months))
    print("Your monthly payment is {:.2f}".format(bond_repayment))

#message is printed out when user enters invalid options or typed incorrectly
#using special characters or numbers in input
else:
    print("Please enter the correct option(investment or bond), no numbers or special characters.")

