#Program to classify a password as strong
have_length = False

up_case = False

low_case = False

have_num = False

count = 0 
#Different conditions to meet
#Input variables store value in different variable to alter the original variables if condition is met
have_length_of_6 = input("Is the password length 6 characters and above(Yes or No): ")
if have_length_of_6 == "Yes":
    have_length = True
    print(have_length)

upper_case = input("Does it contain uppercase letters(Yes or No): ")
if upper_case == "Yes":
    up_case = True
    print(up_case)
    
lower_case = input("Does it contain lowercase letters(Yes or No): ")
if lower_case == "Yes":
    low_case = True
    print(low_case)

have_numbers = input("Does it contain numbers(Yes or No): ")
if have_numbers == "Yes":
    have_num = True
    print(have_num)

#count checks if total equals minimum 3 to print message by incrementing count by 1 if condition is met
if have_length == True:
    count +=1

if up_case == True:
    count +=1

if low_case == True:
    count +=1

if have_num == True:
    count +=1

if count == 3:
    print("This is a suitable password.")

    
