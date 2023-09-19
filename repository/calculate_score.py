from sqlalchemy.orm import Session
import models
from sqlalchemy.orm import sessionmaker

# import schemas
# from fastapi import APIRouter, Depends
# from sqlalchemy import create_engine

# router = APIRouter()


def calculate_score(db: Session):
    match_bettings = db.query(models.MatchBetting).all()

    for match_betting in match_bettings:
        match_id = match_betting.match_id
        user_id = match_betting.owner_id
        user_prediction_team1 = match_betting.prediction_score_team1
        user_prediction_team2 = match_betting.prediction_score_team2
        points_awarded = match_betting.points_awarded

        if not points_awarded:
            match = db.query(models.Match).filter(models.Match.id == match_id).first()
            if match:
                result_team1 = match.result_team1
                result_team2 = match.result_team2

                if result_team1 is not None and result_team2 is not None:
                    correct_prediction = (
                            user_prediction_team1 == result_team1 and user_prediction_team2 == result_team2)

                    if correct_prediction:
                        user = db.query(models.User).filter(models.User.id == user_id).first()
                        if user:
                            user.score += 1
                            match_betting.points_awarded = True

    db.commit()


# def new_creator(db: Session):
#     new_task = db.query(models.MatchBetting).all()
#
#     for element in new_task:
#         user_pred1 = element.prediction_score_team1
#         user_pred2 = element.prediction_score_team2
#         match_id = element.match_id
#
#         elements = db.query(models.Match).first()
#         element_kind = db.query(models.Match).filter(models.Match.id == match.id)
#
#         if not elements_kind:
#             raise
#
# SesionLocal = sessionmaker(autocomit=False)
#
#
# def get_db():
#     db = SesionLocal
#     try:
#         yield db
#     finally:
#         db.close()
#
#
# @router.post('/login', response_model=schemas.UserLogin)
# def read_user(db: Session = Depends(get_db)):
#     pass
#
#
# engine = create_engine(bind=True)
