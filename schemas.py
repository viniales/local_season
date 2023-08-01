from pydantic import BaseModel


class Player(BaseModel):
    name: str
    surname: str
    age: int
    team: str
    nationality: str


class ShowPlayer(Player):
    # with it and response_model we don't display id
    class Config():
        orm_mode = True


class User(BaseModel):
    name: str
    email: str
    password: str


class ShowUser(BaseModel):
    name: str
    email: str

    class Config():
        orm_mode = True
