#Program manages tasks for admin and normal users
import os

SEPARATOR = ', '

#logic for checking username and password to give permission to login
login_success = False
while not login_success:
    entered_username = input('Please enter your username: ')
    entered_password = input('Please enter your password: ')

    with open('user.txt', 'r+') as users:
        for line in users:
            username, password = line.strip().split(SEPARATOR)
            if username == entered_username:
                if password == entered_password:
                    login_success = True
                else:
                    print('Incorrect password!')
                break
        else:
            print('No such user!')

#While logic for admin user to display a special menu
while login_success == True:
    if username=='admin':
        selection = input('''
        Please select one of the following options:
            r - register a new user
            a - add task
            va - view all tasks
            vm - view my tasks
            vs - view total count of tasks and users
            e - exit
        ? ''').lower()

#logic for a normal user logged in
    elif login_success == True:
        selection = input('''
    Please select one of the following options:
        r - register a new user
        a - add task
        va - view all tasks
        vm - view my tasks
        e - exit
    ? ''').lower()

#code for different menu option execution after user is logged in
#and only allowing the admin user to register users
    if selection == 'r' and username != 'admin':
        print("Only admin may register users!")
    if selection == 'r' and username =="admin":
        new_username = input("Please enter a new username: ")
        new_password = input("Please enter new password: ")
        confirm_password = input("Please confirm the password entered: ")
        if confirm_password == new_password:
            with open('user.txt', 'a') as register_user:
                register_user.write(f"\n{new_username}, {new_password}")
        else:
            print("The passwords do not match!")

#for adding task as a user
    elif (selection == "a"):
        with open('tasks.txt', 'a') as register_task:
            task_complete = "No"
            
            name = input("Please enter your fullname: ")
            
            task_title = input("Please enter the title task: ")
            
            task_descript = input("Please give a task description: ")
            
            date_assigned = input("Please enter the current date(e.g 1 November 2021): ").title()
            
            date_due = input("Please enter the due date(e.g 1 November 2021): ").title()

            register_task.write(f"{name}, {task_title}, {task_descript}, {date_assigned}, {date_due}, {task_complete}\n")
            
            print(f"\nTask: {task_title} \nAssigned to: {name} \nDate assigned: {date_assigned} \nDue date: {date_due} \nTask Complete?: {task_complete} \nTask description:\n {task_descript}\n")

#for viewing all tasks of all users  
    elif (selection=="va"):
        file = open('tasks.txt', 'r') 
        lines = file.readlines()
        for line in lines:
            task = line.split(", ")
            print("Task:             {}".format(task[1]))
            print("Assigned to:      {}".format(task[0]))
            print("Date assigned:    {}".format(task[3]))
            print("Due date:         {}".format(task[4]))
            print("Task Completed?   {}".format(task[5]))
            print("Task description: {}".format(task[2]))

#for viewing logged in user tasks
    elif (selection=="vm"):
        file = open('tasks.txt', 'r') 
        lines = file.readlines()
        for line in lines:
            task = line.split(", ")
            if (entered_username == task[0]):
                print("Task:             {}".format(task[1]))
                print("Assigned to:      {}".format(task[0]))
                print("Date assigned:    {}".format(task[3]))
                print("Due date:         {}".format(task[4]))
                print("Task Completed?   {}".format(task[5]))
                print("Task description: {}".format(task[2]))
                print("\n")

#for viewing statistic only for the admin user
    elif selection == 'vs' and username == 'admin':
        with open('tasks.txt', 'r') as total_tasks, open('user.txt', 'r') as total_users:
            file1 = total_tasks.readlines()
            file2 = total_users.readlines()
            print("The total number of tasks is: {}".format(len(file1)))
            print("The total number of users is: {}".format(len(file2)))

#for exiting program
    elif(selection=="e"):
        quit()
else:
    print("Invalid Option")

