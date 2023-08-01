from sqlalchemy import Column, Integer, String
from database import Base
from sqlalchemy.orm import relationship

class Player(Base):
    __tablename__ = 'players_table'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    surname = Column(String)
    age = Column(Integer)
    team = Column(String)
    nationality = Column(String)

    creator = relationship('User', back_populates="ite,s")

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    email = Column(String)
    password = Column(String)
