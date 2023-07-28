from sqlalchemy import Column, Integer, String
from database import Base


class Player(Base):
    __tablename__ = 'players_table'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    surname = Column(String)
    age = Column(Integer)
    team = Column(String)
    nationality = Column(String)
