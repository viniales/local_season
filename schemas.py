from pydantic import BaseModel
from typing import List


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
    # "players" must be the same variable as in Models.py file


class ShowPlayer(BaseModel):
    name: str
    surname: str
    age: int
    team: str
    nationality: str
    creator: ShowUserInPlayers
    # "creator" must be the same variable as in Models.py file
