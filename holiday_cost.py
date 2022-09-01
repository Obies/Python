##Program calculates cost for a holiday
#function for the hotel cost
def hotel_cost(nights):
    return nights * 980

#function for the cost of the plane ticket to the destination
def plane_cost(destination):
    if destination == 1:
        return 1555

    elif destination == 2:
        return 450

    elif destination == 3:
        return 3571

    else:
        print('You have selected an invalid option') #this is a string to print out for any option not above
        return False
    

#function for the cost of renting a car
def car_rental(days):
    return days * 327

#function to calculate the total of all costs for the holiday
#calls the different functions and stores their values in the variable names
def holiday_cost(nights, destination, days):
    nights = hotel_cost(nights)
    destination = plane_cost(destination)
    days = car_rental(days)
    return nights + destination + days

#information received from the user to calculate cost using user input
destination = int(input('What is your destination?\n1. Gqeberha\n2. Durban\n3. Mpumalanga\n ')) #only an integer can be entered here and its supposed to print an error message for an invalid optiom but doesnt
while(plane_cost(destination) == False): 
    destination = int(input('What is your destination?\n1. Gqeberha\n2. Durban\n3. Mpumalanga\n ')) #only an integer can be entered here and its supposed to print an error message for an invalid optiom but doesnt
nights = int(input('How many nights will you be staying? '))
days = int(input('How many days will you need a car for?: '))
total = holiday_cost(nights, destination, days)
print(f"The amount for your getaway is {total}")

#References
#https://www.w3schools.com/python/python_while_loops.asp
#https://www.w3schools.com/python/python_functions.asp
