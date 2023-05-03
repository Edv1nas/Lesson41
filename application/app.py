

from database import SqlDatabase
import getpass

db1 = SqlDatabase()

print("Welcome to your TODO application!")
while True:
    choice = input("Please choose an option from the list:\n1. Log in\n2. Register\n3. Exit\n")
    if choice == "1":
        username = input("Username: ")
        password = getpass.getpass(prompt="Password: ")
        user = db1.login_to_app(username, password)
        if user:
            print(f"Welcome, {username}!")
            while True:
                task_choice = input("Please choose an option from the list:\n1. Add task\n2. Update task\n3. Show tasks\n4. Delete task\n5. Log out\n")
                if task_choice == "1":
                    description = input("Task description: ")
                    db1.create_task(user, description)
                elif task_choice == "2":
                    task_id = input("Task ID: ")
                    new_description = input("New description (leave blank to keep current): ")
                    new_is_done = input("Mark as done (y/leave blank to keep current): ")
                    db1.update_task(user, task_id, new_description, new_is_done)
                elif task_choice == "3":
                    db1.show_tasks(user)
                elif task_choice == "4":
                    task_id = input("Task ID: ")
                    db1.delete_task(user, task_id)
                elif task_choice == "5":
                    break
    elif choice == "2":
        username = input("Choose a username: ")
        password = getpass.getpass(prompt="Choose a password: ")
        db1.create_user(username, password=password)
        print(f"User {username} added successfully.")
    elif choice == "3":
        print("Have a great day!")
        break
    else:
        print("Invalid choice.")