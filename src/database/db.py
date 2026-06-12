from sqlalchemy import create_engine  # create_engine sets up the connection to the database
from sqlalchemy.orm import sessionmaker  # sessionmaker creates factory objects that produce database sessions
from sqlalchemy.orm import declarative_base  # declarative_base provides the base class for all ORM model classes

DATABASE_URL = "sqlite:///skillforge.db"  # Path to the SQLite database file; SQLite stores everything in one file

engine = create_engine(DATABASE_URL)  # Create the database engine that manages the actual connection to the file
SessionLocal = sessionmaker(bind=engine)  # Create a session factory; calling SessionLocal() opens a new DB session
Base = declarative_base()  # Create the base class that all database model classes (like Task) must inherit from
