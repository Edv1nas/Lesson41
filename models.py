from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship

engine = create_engine('sqlite:///todo.db', echo=True)
Base = declarative_base()

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    username = Column(String, unique=True)
    password = Column(String)
    tasks = relationship('Task', back_populates='user')
    
class Task(Base):
    __tablename__ = 'tasks'
    id = Column(Integer, primary_key=True)
    title = Column(String)
    description = Column(String)
    completed = Column(Integer)
    user_id = Column(Integer, ForeignKey('users.id'))
    user = relationship('User', back_populates='tasks')

if __name__ == "__main__":
    Base.metadata.create_all(engine)