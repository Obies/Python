#Program asks for number of learners and requests ID using input
#Then saves the received input to a created file
no_of_students = int(input("How many students are registering: "))

student = input("Please enter your ID number: ")

#Most efficient open method with is used
#file is stored as a string to created file
with open('reg_form.txt', 'w') as file:
    file.write(str(no_of_students)+"\n")

#for loop executes according to number of entered students and minus 1 as computer
#counts from 0
#student identity is saved up to the range specified in no_of_students
    for index in range(no_of_students - 1):
        student = input("Please enter your ID number: ")
        file.write(student + "\n")
    

