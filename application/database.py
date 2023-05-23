from sqlalchemy.orm import sessionmaker
from models import engine
from models import User, Task


Session = sessionmaker(bind=engine)
session = Session()


class SqlDatabase:

    def create_user(self, username: str, password: str) -> None:
        user = User(username=username, password=password)
        session.add(user)
        session.commit()
        print("User added successfully.")

    def login_to_app(self, username: str, password: str) -> None:
        user = session.query(User).filter_by(
            username=username, password=password).first()
        if user:
            return user
        else:
            print("Invalid username or password.")
            return None

    def create_task(self, user: str, description: str) -> None:
        task = Task(user_id=user.id, description=description)
        session.add(task)
        session.commit()
        print("Task added successfully.")

    def update_task(self, user: str, task_id: int, new_description=None, new_task_done=None) -> None:
        task = session.query(Task).filter_by(
            id=task_id, user_id=user.id).first()
        if not task:
            print("Invalid task ID.")
            return
        if new_description:
            task.description = new_description
        if new_task_done is not None:
            task.task_done = int(new_task_done.lower() == "y")
        session.commit()
        print("Task updated successfully.")

    def show_tasks(self, user: str):
        tasks = session.query(Task).filter_by(user_id=user.id).all()
        if not tasks:
            print("No tasks found.")
        else:
            for task in tasks:
                done = "done" if task.task_done else "not done"
                print(f"{task.id}. {task.description} ({done})")

    def delete_task(self, user: str, task_id: int) -> None:
        task = session.query(Task).filter_by(
            id=task_id, user_id=user.id).first()
        if not task:
            print("Invalid task ID.")
            return
        session.delete(task)
        session.commit()
        print("Task deleted")
