import os

from sqlalchemy import create_engine
from sqlalchemy.orm.session import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# To create a database engine
SQLALCHEMY_DATABASE_URL = "sqlite:///chinook.db"  
engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})
# connect_args={"check_same_thread": False} its onyly used for sqlite

# To create a local database session
Session = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# To create an instance of DeclarativeMeta
Base = declarative_base()

# Helper to get a BD Session
def get_db():
    
    db = Session()

    try:
        yield db
    finally:
        db.close()