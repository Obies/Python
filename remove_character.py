#Program requests a sentence then removes the specified characters by the user
sentence = input("Tell me what you wish to type: ")

remove = input("What characters would you like to remove: ")

#for loop is used with replace function to replace chosen letters with empty space
for letter in remove:
    sentence = sentence.replace(letter, "")
    
print(sentence)

