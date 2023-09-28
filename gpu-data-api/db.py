from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os


user="{os.environ['DB_USER']}"
password="{os.environ['DB_PASSWORD']}"


engine = create_engine(f"mysql+mysqlconnector://{user}:{password}@localhost/gpu_db")
Session = sessionmaker(bind=engine)
session = Session()

Base = declarative_base()