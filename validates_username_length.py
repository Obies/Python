#Program validates if user entered name and surname according to length
#And prints different messages out according to conditions
name_surname = input("Please enter your name and surname champ: \n")

#prints a specific message if the specific condition is met
if len(name_surname) == 0:
    print("You haven't entered anything. Please input your full name.")

elif len(name_surname) < 4:
    print("You have entered less than 4 characters. Please make sure you have entered your name and surname.")

elif len(name_surname) > 25:
    print("Please make sure that you have only entered your full name.")

elif len(name_surname) > 5:
    print("Thank you for entering your name.")
