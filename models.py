from sqlalchemy import Column, Integer, String, ForeignKey
from database import Base
from sqlalchemy.orm import relationship


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    email = Column(String)
    password = Column(String)
    points = Column(Integer, default=0)


class Matches(Base):
    __tablename__ = 'matches'
    id = Column(Integer, primary_key=True, index=True)
