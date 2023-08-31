from sqlalchemy.orm import Session
import models


def calculate_score(db: Session):
    match_bettings = db.query(models.MatchBetting).all()

    for match_betting in match_bettings:
        match_id = match_betting.match_id
        user_id = match_betting.owner_id
        user_prediction_team1 = match_betting.prediction_score_team1
        user_prediction_team2 = match_betting.prediction_score_team2

        match = db.query(models.Match).filter(models.Match.id == match_id)
        if match:
            pass