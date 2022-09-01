#Program replaces characters using the replace function
string = "The!quick!brown!fox!jumps!over!the!lazy!dog!.\n"

#sentence is printed out in different ways
print(string.replace("!", " "))

print(string.upper().replace("!", " "), end= ' ')

print(string[::-1].replace("!", " "))
