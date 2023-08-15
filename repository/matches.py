from sqlalchemy.orm import Session
import models, schemas
from fastapi import status, HTTPException
from hashing import Hash


# def check_exist(request: schemas.MatchBetting, db: Session):
#     return db.query(models.User).filter(models.User.name == request.name).first()
def create(request: schemas.Match, db: Session):
    # if check_exist(request, db):
    #     raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail='The User already exist')

    new_match = models.Match(team1=request.team1, team2=request.team2, result_team1=request.result_team1,
                             result_team2=request.result_team2, date=request.date)
    db.add(new_match)
    db.commit()
    db.refresh(new_match)

    return new_match
