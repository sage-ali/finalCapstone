# Task Manager

A simple task manager application that allows users to register, add tasks, view tasks, and display statistics. Users can register their accounts with a unique username and password. Once logged in, they can add tasks, view all tasks, view their own tasks, and see statistics about the number of users and tasks.

## Table of Contents
- [Installation](#installation)
- [Usage](#usage)
- [Credits](#credits)

## Installation
1. Clone the repository to your local machine.
2. Ensure you have Python 3 installed.
3. Open the project folder in your preferred text editor.
4. Run the command `python task_manager.py` in your terminal to start the application.

## Usage
1. Register a new user:
   - Enter a new username and password when prompted.
   - Usernames must be unique.
   - Passwords must be entered correctly to complete registration.

2. Add a task:
   - Enter the name of the person assigned to the task, task title, description, and due date when prompted.
   - Due date must be in the format "YYYY-MM-DD".
   
3. View all tasks:
   - Only the admin user can view all tasks.
   - The task list will be displayed, showing the task title, assigned username, assigned date, due date, and task description.

4. View my tasks:
   - Each user can view their own tasks.
   - The user's tasks will be displayed, showing the task title, assigned username, assigned date, due date, and task description.

5. Display statistics:
   - Only the admin user can display statistics.
   - The number of users and tasks will be shown.

## Credits
- Created by [Ali Agboola](https://github.com/sage-ali)
