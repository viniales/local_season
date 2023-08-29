from typing import Optional
from pydantic import BaseModel, EmailStr, conint
from datetime import datetime


class MatchBettingBase(BaseModel):
    match_id: int
    prediction_score_team1: int
    prediction_score_team2: int


class MatchBettingCreate(MatchBettingBase):
    pass


class UserOut(BaseModel):
    id: int
    email: EmailStr
    created_at: datetime

    class Config:  # this class
        orm_mode = True


# Responsible for sending the post out
class MatchBetting(MatchBettingBase):
    betting_id: int
    created_at: datetime
    owner_id: int
    owner: UserOut

    class Config:  # this class
        orm_mode = True


''' This JSON response is formatted by the pydantic Post class above  
    {
        "title": "EDITED changed post",
        "content": "EDIT of changes",
        "published": true,
        "id": 3,
        "created_at": "2022-02-07T22:18:54.765932-08:00",
        "owner_id": 6,
        "owner": {
            "id": 6,
            "email": "admin2@admin.com",
            "created_at": "2022-02-07T22:14:26.196719-08:00"
        }
    }
'''


class MatchBettingOut(BaseModel):
    Post: MatchBetting
    votes: int

    class Config:
        orm_mode = True


class UserCreate(BaseModel):
    email: EmailStr  # using this type ensures email is a valid one, uses "email-validator" library
    password: str


class UserLogin(BaseModel):
    email: EmailStr
    password: str


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    id: Optional[str] = None


class Vote(BaseModel):
    post_id: int
    dir: conint(le=1, ge=0)  # means lessthan 1 and greaterthan 0, aka 0 or 1
    # maybe try validator decorator from pydantic to achieve this too??? not sure

# class Match(BaseModel):
#     team1: str
#     team2: str
#     result_team1: int
#     result_team2: int
#     date: str
