# Notes: 
# 1. Use the following username and password to access the admin rights 
# username: admin
# password: password
# 2. Ensure you open the whole folder for this task in VS Code otherwise the 
# program will look in your root directory for the text files.

#=====importing libraries===========
import os
from datetime import datetime, date

DATETIME_STRING_FORMAT = "%Y-%m-%d"
    


# Function to register a new user
def reg_user():
    """
    Register a new user and add them to the user.txt file.
    """
    # - Request input of a new username and ensure username is unique in user.txt
    new_username = ""
    
    while not new_username:
        new_username = input("New Username: ")
        if new_username in username_password:
            print()
            print("Username already exists. Please choose a different username.")
            print("")
            new_username = ""
    
    # - Validate and ensure user enter matching passwords
    while True:
        # - Request input of a new password
        new_password = input("New Password: ")
        confirm_password = input("Confirm Password: ")
        
        if new_password == confirm_password:
            # Register and save new user details
            username_password[new_username] = new_password
            with open("user.txt", "a") as user_file:
                user_file.write(f"\n{new_username};{new_password}")
            print()
            print("New user added successfully.")
            print("")
            break
        else:
            print()
            print("Passwords do not match. User registration failed. Try entering passwords again.")
    # Update the global user data for the program
    
            
    
    


# Function to add a new task
def add_task():
    """
    Add a new task to the tasks.txt file.
    Prompt a user for the following: 
        - A username of the person whom the task is assigned to,
        - A title of a task,
        - A description of the task and 
        - the due date of the task.
    """
    while True:
        task_username = input("Name of person assigned to task: ")
        
        # Ensure the user exists in the user database
        if task_username not in username_password:
            print()
            print("User does not exist. Please enter a valid username.")
        else:
            break

    # Get details of the task
    task_title = input("Title of Task: ")
    task_description = input("Description of Task: ")
    # Ensure the user enters a valid date
    while True:
        try:
            task_due_date = input("Due date of task (YYYY-MM-DD): ")
            due_date_time = datetime.strptime(task_due_date, DATETIME_STRING_FORMAT)
            break
        except ValueError:
            print()
            print("Invalid datetime format. Please use the format specified.")

    # Then get the current date.
    curr_date = date.today()
    new_task = {
        "username": task_username,
        "title": task_title,
        "description": task_description,
        "due_date": due_date_time,
        "assigned_date": curr_date,
        "completed": False
    }

    task_list.append(new_task)
    with open("tasks.txt", "a") as task_file:
        task_file.write(f"\n{task_username};{task_title};{task_description};"
                        f"{due_date_time.strftime(DATETIME_STRING_FORMAT)};"
                        f"{curr_date.strftime(DATETIME_STRING_FORMAT)};No")
    print()
    print("Task successfully added.")
    


# Function to view all tasks
def view_all():
    """
    Read tasks from tasks.txt file and print them to the console in a clear format.
    """
    if curr_user == 'admin':
        if not task_list:
            print("No tasks available.")
        else:
            for task in task_list:
                print()
                print(f"Task: {task['title']}")
                print(f"Assigned to: {task['username']}")
                print(f"Date Assigned: {task['assigned_date'].strftime(DATETIME_STRING_FORMAT)}")
                print(f"Due Date: {task['due_date'].strftime(DATETIME_STRING_FORMAT)}")
                print(f"Task Description:\n{task['description']}")
                print()
    else:
        print()
        print("You do not have permission to perform this action")
        return
    


# Function to view user's tasks
def view_mine():
    """
    Read tasks from tasks.txt file and print user's tasks to the console in a clear format.
    """
    user_tasks = [task for task in task_list if task['username'] == curr_user]
    if not user_tasks:
        print()
        print("No tasks assigned to you.")
    else:
        for task in user_tasks:
            print()
            print(f"Task: {task['title']}")
            print(f"Assigned to: {task['username']}")
            print(f"Date Assigned: {task['assigned_date'].strftime(DATETIME_STRING_FORMAT)}")
            print(f"Due Date: {task['due_date'].strftime(DATETIME_STRING_FORMAT)}")
            print(f"Task Description:\n{task['description']}")
            print()


# Function to display statistics
def display_statistics():
    """
    Display statistics about the number of users and tasks.
    """
    if curr_user == 'admin':
        num_users = len(username_password)
        num_tasks = len(task_list)
        print()
        print("-----------------------------------")
        print(f"Number of users: {num_users}")
        print(f"Number of tasks: {num_tasks}")
        print("-----------------------------------")
    else:
        print()
        print("You do not have permission to perform this action")
        return


# Create tasks.txt if it doesn't exist
if not os.path.exists("tasks.txt"):
    with open("tasks.txt", "w") as default_file:
        pass
# Get tasks from the task list
with open("tasks.txt", 'r') as task_file:
    task_data = task_file.read().split("\n")
    task_data = [task for task in task_data if task != ""]


# Create a list of tasks and store task information there for later use
task_list = []
for task_str in task_data:
    curr_task = {}

    # Split by semicolon and manually add each component
    task_components = task_str.split(";")
    curr_task['username'] = task_components[0]
    curr_task['title'] = task_components[1]
    curr_task['description'] = task_components[2]
    curr_task['due_date'] = datetime.strptime(task_components[3], DATETIME_STRING_FORMAT)
    curr_task['assigned_date'] = datetime.strptime(task_components[4], DATETIME_STRING_FORMAT)
    curr_task['completed'] = True if task_components[5] == "Yes" else False

    task_list.append(curr_task)
    


#====Login Section====
'''
    This code reads usernames and password from the user.txt file to 
    allow a user to login.
'''
# If no user.txt file, write one with a default account
if not os.path.exists("user.txt"):
    with open("user.txt", "w") as default_file:
        default_file.write("admin;password")

# Read in user_data
with open("user.txt", 'r') as user_file:
    user_data = user_file.read().split("\n")

# Convert to a dictionary
username_password = {}
for user in user_data:
    username, password = user.split(';')
    username_password[username] = password

logged_in = False
while not logged_in:

    print("LOGIN")
    curr_user = input("Username: ")
    curr_pass = input("Password: ")
    if curr_user not in username_password:
        print("User does not exist")
        continue
    elif username_password[curr_user] != curr_pass:
        print("Wrong password")
        continue
    else:
        print("Login Successful!")
        logged_in = True


while True:
    # presenting the menu to the user and 
    # making sure that the user input is converted to lower case.
    print()
    menu = input('''Select one of the following Options below:
        r - Registering a user
        a - Adding a task
        va - View all tasks
        vm - View my task
        ds - Display statistics
        e - Exit
        : ''').lower()

    if menu == 'r':
        reg_user()
    elif menu == 'a':
        add_task()
    elif menu == 'va':
        view_all()
    elif menu == 'vm':
        view_mine()
    elif menu == 'ds':
        display_statistics()
    elif menu == 'e':
        print('Goodbye!!!')
        exit()
    else:
        print()
        print("Invalid choice. Please try again.")