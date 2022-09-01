#Program gets two numbers from the user and swaps them with each other
num1 = input("Enter a golden number: ")

num2 = input("Enter another golden number: ")

print("Before swap:\n {} \n {}".format(num1, num2))

#swaps the variables with each others values then prints out the swapped values
num1, num2 = num2, num1

print("After swap:\n {} \n {}".format(num1, num2))

