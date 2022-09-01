#Program reads data from external file using with open
#And prints them out with the correct format
lines = []
names = []
dobs = []

with open('DOB.txt', 'r+') as file:
    lines = file.readlines()

#strips a newline in external file entries
    entries = [line.strip('\n') for line in lines]

#for loop appends entries to name and dobs list
#f-format is used to specify positions
for position in entries:
    positions = position.split()
    names.append(f"{positions[0][0]} {positions[1]}")
    dobs.append(f"{positions[2]} {positions[3]} {positions[4]}")

#join function is used to give correct output
#by joining names and date of births(dobs) to the list
#and printing out the correct positions
names = '\n'.join(names)
dobs = '\n'.join(dobs)
print(f"Names: \n{names}")
print()
print(f"Birthdays: \n{dobs}")

#References:
#https://www.w3schools.com/python/python_lists.asp
#https://www.w3schools.com/python/ref_string_strip.asp
#https://www.geeksforgeeks.org/python-list-slicing/
