from sqlalchemy.orm import Session
import models, schemas
from fastapi import status, HTTPException
from hashing import Hash


# def check_exist(request: schemas.MatchBetting, db: Session):
#     return db.query(models.User).filter(models.User.name == request.name).first()
def create(request: schemas.MatchBetting, db: Session, user):
    # if check_exist(request, db):
    #     raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail='The User already exist')
    new_match = models.MatchBetting(prediction_score_team1=request.team1, prediction_score_team2=request.team2,
                                    match_id=request.match_id, user_id=user)
    db.add(new_match)
    db.commit()
    db.refresh(new_match)

    return new_match
