#Program receives input from one file and performs calculations that are saved to another file
#function for printing the minimum number in the list
def minimum(lst):
    arr = lst.append(line.split(","))
    return min(arr)

#function for printing the maximum number in the list
def maximum(lst):
    arr = lst.append(line.split(","))
    return max(arr)

#function for printing the average of all numbers in the list
def average(lst):
    arr = lst.split(",")
    integer_map = map(int, arr)             #converts strings to integers. Otherwise SUM will not work
    integer_list = list(integer_map)
    average = sum(integer_list)/len(integer_list)
    return average

#Opens input file where data is received from
with open('input.txt', 'r') as input:
    lines = input.readlines()
    print(lines)

#opens file where new data values will be stored
output = open('output.txt', 'w')

#for loop for iterating through the lines in the file and executing the different functions
for line in lines:
    line = line.replace('\r\n', '')         #cleans out the garbage of the lines data
    line = line.replace('\xef\xbb\xbf', '')
    print(line)                             #so now it supposed to be clean. Let's check by printing a line

    if(line[0:4] == "min:"):                #this helps get rid of the text and detect the integers
        line = line.replace('min:', '')
        result = minimum(line)
        print(result)
        output.write(f"The min of {line} is {result}.")
        
    elif(line[0:4] == "max:"):
        line = line.replace('max:', '')
        result = maximum(line)
        print(result)
        output.write(f"The max of {line} is " + str(result) + ".")
        
    elif(line[0:4] == "avg:"):
        line = line.replace('avg:', '')
        print(line)
        result = average(line)
        output.write(f"The avg of {line} is " + str(result) + ".")
        

output.close()
