#Program uses input to request the user time in minutes
swimming = float(input("How many minutes for your swim time: "))

cycling = float(input("How many minutes for your cycle time: "))

running = float(input("How many minutes for your run time: "))

#Calculates the total time
total_time = swimming + cycling + running

print(total_time)

#Prints a specific message if conditions are met
if total_time <= 100:
    print("Provincial colours.")

if total_time > 100 and total_time < 105:
    print("Provincial Half Colours.")

if total_time > 105 and total_time < 110:
    print("Provincial Scroll.")

if total_time > 110:
    print("No award.")
