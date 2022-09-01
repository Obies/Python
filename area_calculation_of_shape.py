#Program calculates area of a shape based on the users selection
#And given measurements
shape = input("What is the shape you choose: ").lower()

#Conditions executed and calculated based on the user selection and given measurements
if shape == "rectangular":
    length = float(input("Please enter the length: "))
    width = float(input("Please enter the width: "))
    area_of_rectangular = length * width
    print(area_of_rectangular)

if shape == "square":
    length = float(input("Please enter the length: "))
    area_of_square = length * length
    print(area_of_square)

if shape == "round":
    radius = float(input("Please enter the radius: "))
    area_of_circle = 3.14 * (radius * radius)
    print(area_of_circle)
