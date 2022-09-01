#Program converts string alternate characters  to uppercase and lowercase each
string = "Hello World!"

#for loop is used to change letters to upper and lower case
for letter in range(0,12):
    if(letter % 2 ==0):
        print(string[letter].upper(), end = "")
        
    else:
        print(string[letter], end = "") #prints lowercase if not divisible by 2

