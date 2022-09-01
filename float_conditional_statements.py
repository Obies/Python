#Program calculates total of floats entered by user
import math

#create empty list to append numbers too
float_list = []

#variable for maximum numbers to enter 
max_numbers = 10

#for loop requests input and appends to the empty list
for add in range(max_numbers):
    numbers = float(input("Please enter your chosen numbers: "))
    float_list.append(numbers)
    continue

#prints the appended list and sum of the list
print(float_list)
print(sum(float_list))

#shows position of the maximum number in the list
max_index = float_list.index(max(float_list))
print(max_index)

#shows the position of the smallest number in the list
min_index = float_list.index(min(float_list))
print(min_index)

#calculates average of the list and prints out the result
average = sum(float_list) / len(float_list)
print(round(average, 2))

#calculates the median of the list and prints out the result
median = sorted(float_list)[len(float_list) // 2]
print(median)


    
