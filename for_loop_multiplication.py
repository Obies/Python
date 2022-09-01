#Program prints the multiplication table up to 12
#for the number entered by the user
number = int(input("Please enter a number to multiply: "))

print(f"The {number} times table is: ")
#For statement specifying start and end range to multiply number by
for i in range(1, 13):
    print("{} * {} = {} ".format(number, i,(number*i)))

