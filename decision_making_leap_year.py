#Program determines if a year is a leap year or not
year = int(input("Please enter the year to start from: "))

num_years = int(input("Please enter how many years you would like to check for leap year validity: "))

#for loop checks the range from the start year entered and 
for year in range(year, year + num_years):

#if statement checks if year is divisible by 4 and prints statement    
        if year % 4 == 0:       
                print("{} is a leap year".format(year))

#else statement prints if year is not divisible by 4
        else:
                print ("{} is not a leap year".format(year))
