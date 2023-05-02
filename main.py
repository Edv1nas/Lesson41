"""Create a TO DO list application that runs in terminal. 
It should allow user to log in. 
Each user should have his own tasks in to do list. 
User should be able to add/ update/ delete tasks. 
User information and task information should be kept in database"""

from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy.ext.declarative import declarative_base
import getpass

Base = declarative_base()
engine = create_engine('sqlite:///todo.db', echo=False)

Session = sessionmaker(bind=engine)
session = Session()

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    username = Column("Username", String, unique=True)
    password = Column("Password", String)
    tasks = relationship('Task', back_populates='user')

class Task(Base):
    __tablename__ = 'tasks'

    id = Column(Integer, primary_key=True)
    description = Column("Description", String)
    is_done = Column(Integer, default=0)
    user_id = Column(Integer, ForeignKey('users.id'))

    user = relationship("User", back_populates="tasks")

Base.metadata.create_all(engine)

def add_user(username, password):

    user = User(username=username, password=password)
    session.add(user)
    session.commit()
    print("User added successfully.")

def login(username, password):

    user = session.query(User).filter_by(username=username, password=password).first()
    if user:
        print(f"Welcome, {username}!")
        return user
    else:
        print("Invalid username or password.")
        return None

def add_task(user, description):
    task = Task(user_id=user.id, description=description)
    session.add(task)
    session.commit()
    print("Task added successfully.")

def update_task(user, task_id, new_description=None, new_is_done=None):
    task = session.query(Task).filter_by(id=task_id, user_id=user.id).first()
    if not task:
        print("Invalid task ID.")
        return
    if new_description:
        task.description = new_description
    if new_is_done is not None:
        task.is_done = int(new_is_done.lower() == "y")
    session.commit()
    print("Task updated successfully.")

def show_tasks(user):
    tasks = session.query(Task).filter_by(user_id=user.id).all()
    if not tasks:
        print("No tasks found.")
    else:
        for task in tasks:
            done = "done" if task.is_done else "not done"
            print(f"{task.id}. {task.description} ({done})")

def delete_task(user, task_id):
    task = session.query(Task).filter_by(id=task_id, user_id=user.id).first()
    if not task:
        print("Invalid task ID.")
        return
    session.delete(task)
    session.commit()
    print("Task deleted")


print("Welcome to your TODO application!")
while True:
    choice = input("Please choose an option from the list:\n1. Log in\n2. Register\n3. Exit\n")
    if choice == "1":
        username = input("Username: ")
        password = getpass.getpass(prompt="Password: ")
        user = login(username, password)
        if user:
            print(f"Welcome, {username}!")
            while True:
                task_choice = input("Please choose an option from the list:\n1. Add task\n2. Update task\n3. Show tasks\n4. Delete task\n5. Log out\n")
                if task_choice == "1":
                    description = input("Task description: ")
                    add_task(user, description)
                elif task_choice == "2":
                    task_id = input("Task ID: ")
                    new_description = input("New description (leave blank to keep current): ")
                    new_is_done = input("Mark as done (y/leave blank to keep current): ")
                    update_task(user, task_id, new_description, new_is_done)
                elif task_choice == "3":
                    show_tasks(user)
                elif task_choice == "4":
                    task_id = input("Task ID: ")
                    delete_task(user, task_id)
                elif task_choice == "5":
                    break
    elif choice == "2":
        username = input("Choose a username: ")
        password = getpass.getpass(prompt="Choose a password: ")
        add_user(username, password)
        print(f"User {username} added successfully.")
    elif choice == "3":
        print("Have a great day!")
        break
    else:
        print("Invalid choice.")