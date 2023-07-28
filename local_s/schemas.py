from pydantic import BaseModel


class Player(BaseModel):
    name: str
    surname: str
    age: int
    team: str
    nationality: str
