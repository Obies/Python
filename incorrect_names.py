#Program stores incorrect names in a list and ends when correct name "John" is entered
#Empty list is created to store incorrect names
incorrect_names = []

name = ""

#while loop repeats when incorrect name is not entered and appends to the list
while name != "John":
    name = input("Please enter a name: ").title()
    incorrect_names.append(name)

#if statement prints incorrect names when the correct name is entered
#and uses indexing to prevent the correct name being printed with incorrect names
    if name == "John":
        print(f"incorrect_names: {incorrect_names[:-1]}")

