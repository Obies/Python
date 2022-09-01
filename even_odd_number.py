#Program checks whether number is even or odd and prints it out
num = int(input("Please enter an integer so we can check it: "))

if (num)%2 == 0:
    print(num)
    print("Even number")

if (num)%2 != 0: #Uses not equal to comparative operator
    print(num)
    print("Odd number")
