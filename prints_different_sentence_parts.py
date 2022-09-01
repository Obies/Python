#Program manipulates a sentence stored in a variable using replace
str_manip = input("Enter your favourite sentence champ: ")

#Prints different statements
print(str_manip)

print(len(str_manip))

print(str_manip.replace("s", "@"))

print(str_manip[-1:-4:-1])

print(str_manip[0:3] + str_manip[-1:-3:-1])

print(str_manip.replace(" ", "\n"))


