from pydantic import BaseModel
from typing import List


#
class Points(BaseModel):
    points: int


class User(BaseModel):
    name: str
    email: str
    password: str


class ShowUser(BaseModel):
    name: str
    email: str
    points: int

    # "players" must be the same variable as in Models.py file


class Login(BaseModel):
    username: str
    password: str


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    username: str | None = None


class MatchBetting(BaseModel):
    team1: int
    team2: int


class Match(BaseModel):
    team1: str
    team2: str
    result_team1: int
    result_team2: int
    date: str
