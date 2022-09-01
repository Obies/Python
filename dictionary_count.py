#Program counts number of times a character occurs in a string
#then prints out the results
string = "I've got you too"

#empty dictionary is created to store keys and values from string
dict_count = {}

#get method is used to count each character in the string variable
for keys in string:
    dict_count[keys] = dict_count.get(keys, 0) + 1

#command below prints out the characters from the string according
#to how many times they occur in the string
print(str(dict_count))
