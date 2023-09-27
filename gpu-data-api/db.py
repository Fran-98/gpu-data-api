from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os

engine = create_engine(f"mysql+mysqlconnector://root:gonza@localhost/gpu_db")
Session = sessionmaker(bind=engine)
session = Session()

Base = declarative_base()