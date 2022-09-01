#Program displays different answers based on fixed variables
#Fixed variables
num1 = 12

num2 = 17

num3 = 23


#Different answers based on the specific condition being met
if (num1 > num2):
    print(num1)

else:
    print(num2)

if (num1%2) == 0:
    print("even")

else:
    print("odd")

#Code for conditional statement for sorting from largest to smallest
if num1 > num2:
    num1,num2 = num2,num1
if num1 > num3:
    num1,num3 = num3,num1
if num2 > num3:
    num2,num3 = num3,num2
    
print (num3, num2, num1)
    
        
        

