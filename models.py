from sqlalchemy import Column, Integer, String, ForeignKey
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
    user_id = Column(Integer, ForeignKey("users.id"))

    creator = relationship("User", back_populates="players")


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    email = Column(String)
    password = Column(String)

    players = relationship("Player", back_populates="creator")

    points = Column(Integer, ForeignKey("user_points.points"))
    creator = relationship("UsersPoints", back_populates="user_points")


class UsersPoints(Base):
    __tablename__ = 'user_points'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    points = Column(Integer)
    #
    user_points = relationship("User", back_populates="creator")
