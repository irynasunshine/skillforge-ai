from sqlalchemy import Column, Integer, String, Boolean  # Import column types used to define database fields
from src.database.db import Base  # Base is the parent class all database model classes must inherit from


class Task(Base):  # Define the Task model; each instance of this class represents one row in the database table
    __tablename__ = "tasks"  # The name SQLAlchemy uses for the table in the SQLite database file

    id = Column(Integer, primary_key=True)  # Unique numeric ID for each task; auto-incremented by the database
    title = Column(String)  # The text description of the learning task
    completed = Column(Boolean, default=False)  # Whether the task is done; starts as False (not completed) by default
    week = Column(Integer)  # Which week of the learning plan this task belongs to
