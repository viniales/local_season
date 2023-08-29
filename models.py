from sqlalchemy import Column, Integer, String, Boolean, DATETIME
from sqlalchemy.orm import relationship
from sqlalchemy.sql.schema import ForeignKey
from database import Base
import datetime


class MatchBetting(Base):
    __tablename__ = "posts"
    betting_id = Column(Integer, primary_key=True, nullable=False)
    match_id = Column(Integer)
    owner_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"), nullable=False)
    prediction_score_team1 = Column(Integer)
    prediction_score_team2 = Column(Integer)
    created_at = Column(DATETIME, default=datetime.datetime.utcnow())
    owner = relationship("User")
    '''relationship automatically creates another property for File, so when we retrieve 
    File it will return an 'owner' property too, and it will figure out the relationship to   
    User. Basically, will fetch the User based of the owner id and return that for us
    Example of data response with relationship:
    {
        "id": 12,
        "file": "",
        "file_title": "dfasdf",
        "patient_id": 3434,
        "user_id": 4545,
        "owner": {
            "id": 223,
            "email": "john@hotmail.com",
            "password": "fadfaf",
            "created_at": "2022"
        }
    }
    Use pydantic models in path operations to limit the data. For example changing the data
    format to only id and email, excluding the password and created_at properties.
    '''


class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, nullable=False)
    email = Column(String, nullable=False, unique=True)
    password = Column(String, nullable=False)
    created_at = Column(DATETIME, default=datetime.datetime.utcnow())
    phone_number = Column(String)

# class Match(Base):
#     __tablename__ = 'matches'
#     id = Column(Integer, primary_key=True, index=True)
#     team1 = Column(String)
#     team2 = Column(String)
#     result_team1 = Column(Integer)
#     result_team2 = Column(Integer)
#     date = Column(String)
#
#     match_betting = relationship("MatchBetting", back_populates="match")
