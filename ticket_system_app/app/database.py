from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os

SQLALCHEMY_DATABASE_URI = "postgres://rosatom_user:123@localhost/ticket_system" 
# SQLALCHEMY_DATABASE_URI = os.environ['DATABASE_URL'] - for production 

engine = create_engine(
    SQLALCHEMY_DATABASE_URI
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
