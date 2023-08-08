from pydantic import BaseModel
from typing import List


#
class Points(BaseModel):
    points: int


class Player(BaseModel):
    name: str
    surname: str
    age: int
    team: str
    nationality: str


class User(BaseModel):
    name: str
    email: str
    password: str


class ShowUserInPlayers(BaseModel):
    name: str
    email: str


class ShowUser(BaseModel):
    name: str
    email: str
    players: List[Player] = []
    points: List[Points] = []

    # "players" must be the same variable as in Models.py file


class ShowPlayer(BaseModel):
    name: str
    surname: str
    age: int
    team: str
    nationality: str
    creator: ShowUserInPlayers
    # "creator" must be the same variable as in Models.py file


class Login(BaseModel):
    username: str
    password: str


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    username: str | None = None
