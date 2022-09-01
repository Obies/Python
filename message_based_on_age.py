#Program prints a specific message that meets the specific condition
age = int(input("What is your age patron: "))

#Messages printed out if condition is met
if age >= 18:
    print("You are old enough!")

elif age >= 16:
    print("Almost there.")

else:
    print("You're just too young!")
