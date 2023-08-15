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

    match_betting = relationship("MatchBetting", back_populates="user")


class Match(Base):
    __tablename__ = 'matches'
    id = Column(Integer, primary_key=True, index=True)
    team1 = Column(String)
    team2 = Column(String)
    result_team1 = Column(Integer)
    result_team2 = Column(Integer)
    date = Column(String)

    match_betting = relationship("MatchBetting", back_populates="match")


class MatchBetting(Base):
    __tablename__ = 'match_batting'
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    match_id = Column(Integer, ForeignKey("matches.id"))
    prediction_score_team1 = Column(Integer)
    prediction_score_team2 = Column(Integer)

    user = relationship("User", back_populates='match_betting')
    match = relationship("Match", back_populates='match_betting')