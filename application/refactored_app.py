from database import SqlDatabase
import getpass

db1 = SqlDatabase()


def choose_login():
    username = input("Username: ")
    password = getpass.getpass(prompt="Password: ")
    return db1.login_to_app(username, password)


def choose_to_register_user():
    username = input("Choose a username: ")
    password = getpass.getpass(prompt="Choose a password: ")
    return db1.create_user(username, password)


def choose_create_new_task(user):
    description = input("Task description: ")
    db1.create_task(user, description)


def chooose_to_update_task(user):
    task_id = input("Task ID: ")
    new_description = input(
        "New description (leave blank to keep current): ")
    mark_done = input(
        "Mark as done (type y for yes/leave blank to keep current): ")
    db1.update_task(user, task_id, new_description, mark_done)


def choose_to_show_user_task(user):
    db1.show_tasks(user)


def choose_to_delete_task(user):
    task_id = input("Task ID: ")
    db1.delete_task(user, task_id)
