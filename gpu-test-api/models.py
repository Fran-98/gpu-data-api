import db

from sqlalchemy import Column, Integer, String, Float

class GPU(db.Base):
    __tablename__ = 'GPU'

    #id = Column(Integer, primary_key=True)
    name = Column(String(128), primary_key=True, nullable=False)
    score = Column(Integer, nullable=False)
    price = Column(Float)

    def __init__(self, name, score, price):
        self.name = name
        self.score = score
        self.price = price
    
    def __repr__(self):
        return f'{self.name}, score: {self.score}, price: {self.price}'

    def __str__(self):
        return self.name