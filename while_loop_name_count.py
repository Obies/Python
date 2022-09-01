#Program counts the number of names entered
#Counter variable is created and initialised with 0
name_count = 0

#While loop executes while True user is typing name and stops when "Stop" is inputted
#name_count is incremented with every name entered
while True:
    name = input("Please enter the full names: ")
    name_count += 1

    if name == "Stop":
        print("The total number of names entered is {}.".format(name_count))
        break  #stops the program from repeating again once Stop is executed


