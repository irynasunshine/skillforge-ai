from src.database.db import SessionLocal, engine  # Import the session factory and the database engine
from src.core.models import Task  # Import the Task model class to interact with the tasks table
from src.database.db import Base  # Import Base so we can access metadata for table creation

Base.metadata.create_all(bind=engine)  # Create all database tables defined by models if they don't already exist


def save_tasks(tasks):  # Save a list of task dictionaries to the database
    db = SessionLocal()  # Open a new database session (like opening a connection)

    for task in tasks:  # Loop through each task dictionary in the list
        db_task = Task(  # Create a new Task ORM object from the dictionary values
            title=task["title"],  # Set the task's title text
            week=task["week"]  # Set which week this task belongs to
        )

        db.add(db_task)  # Stage the new Task object to be inserted (not written yet)

    db.commit()  # Write all staged tasks to the database in a single transaction
    db.close()  # Close the session to release the database connection


def get_tasks():  # Retrieve all tasks stored in the database
    db = SessionLocal()  # Open a new database session
    tasks = db.query(Task).all()  # Run a SELECT * query on the tasks table and return all rows as Task objects
    db.close()  # Close the session after reading

    return tasks  # Return the list of Task objects to the caller


def complete_task(task_id):  # Mark a specific task as completed based on its ID
    db = SessionLocal()  # Open a new database session

    task = db.query(Task).filter(Task.id == task_id).first()  # Find the task with the matching ID (or None)

    if task:  # Only update if a task with that ID was actually found in the database
        task.completed = True  # Set the completed flag to True
        db.commit()  # Save the change to the database

    db.close()  # Close the session to free resources
