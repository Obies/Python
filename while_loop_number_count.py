#Program calculates the average of numbers entered above -1
#Using the while loop
number = int(input("Please enter the numbers you wish to calculate: "))

counter = 0

sum = 0

#While loop executes the calculation
#sum adds the integers together from the numbers entered
while number > -1:
    counter += 1
    sum += number
    number = int(input("Please enter the numbers you wish to calculate: "))

#This prevents error of not being able to divide by 0
if counter == 0:
    counter = 1
print(sum / counter)
    
