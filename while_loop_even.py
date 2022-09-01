#Program prints even numbers using while loop
number = int(input("Please enter a number: "))

#i is the control variable
i = 1
#while condition to print out even numbers
while i <= number:
    if i % 2 == 0:
        print(i)
    i += 1      
