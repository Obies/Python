#Program determines if a number is divisible by 2, 5.
number = int(input("Please enter a number champ: "))

#Different if conditions printed if condition is met
if (number) % 2 == 0 and (number) % 5 == 0:
    print("Yes")

else:
    print("No")

if (number) %2 == 0 or (number) % 5 == 0:
    print("Yes")

else:
    print("No")

if (number) %2 == 0 or (number) % 5 == 0:
    print("Divisible by 2 or 5.")

else:
    print("Not divisible by 2 or 5.")
