#Program calculates Body Mass Index based on users details and prints a specific message
weight = float(input("How much do you weigh?: ")) #Weight is in kilograms

height = float(input("How tall are you?: ")) #Height is in meters

bmi = weight / ((height)*(height))

print(bmi)

#Message printed out when a specific condition is met from if-elif-else statements
if bmi >= 30:
    print("The user is obese.")

elif bmi >= 25:
    print("The user is overweight.")

elif bmi >=18.5:
    print("The user is normal weight.")

else:
    print("The user is underweight.")
