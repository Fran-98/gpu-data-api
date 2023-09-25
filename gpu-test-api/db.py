from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os

engine = create_engine(f"mysql+mysqlconnector://{os.environ['DB_USER']}:{os.environ['DB_PASSWORD']}@localhost/GPU_DB")
Session = sessionmaker(bind=engine)
session = Session()

Base = declarative_base()