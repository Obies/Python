#Program requires user enter date of birth and prints a message if condition is met
dob = int(input("Please enter your year of birth: "))

#calculates the age from current year we are in
age = 2021 - dob

#prints out message if condition is met
if age >= 18:
    print("Congrats, you are old enough.")
