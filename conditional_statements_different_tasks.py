#Programs perform different functions according to task
#Program 1 performs countdown from 20 to 0
num = 20

while num > -1:
    print(num)
    num -= 1
print("\n")

#Program 2 prints all even numbers between 1 and 20
for i in range (1, 20):
    if i % 2 == 0:
        print(i)
print("\n")

#Program 3 prints specific stars
for i in range(0 ,6):
        print("* " * i)
print("\n")

#Program 4 computes the highest common factor of two positive integers.
first_num = int(input(" Please Enter the First Value a: "))

second_num = int(input(" Please Enter the Second Value b: "))

i = 1 #is the control variable

#While loop checks condition for numbers that i does not exceed entered integers
#If statement checks for the greatest number able to divide by entered integers
while(i <= first_num and i <= second_num):
    if(first_num % i == 0 and second_num % i == 0):
        highest_common_factor = i
    i += 1
    
print("\n The highest common factor of {} and {} is {}".format(first_num, second_num, highest_common_factor))
