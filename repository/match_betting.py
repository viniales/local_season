from sqlalchemy.orm import Session
import models, schemas
from fastapi import status, HTTPException


def create(post: schemas.MatchBettingCreate, db: Session, current_user):
    new_post = models.MatchBetting(owner_id=current_user.id, **post.dict())
    db.add(new_post)
    db.commit()
    db.refresh(new_post)
    return new_post

#
# def create(request: schemas.MatchBetting, db: Session, user):
#     new_match = models.MatchBetting(prediction_score_team1=request.team1, prediction_score_team2=request.team2,
#                                     match_id=request.match_id, user_id=user)
#     db.add(new_match)
#     db.commit()
#     db.refresh(new_match)
#
#     return new_match
