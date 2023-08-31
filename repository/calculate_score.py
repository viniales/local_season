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
            result_team1 = match.result_team1
            result_team2 = match.result_team2

            if result_team1 is not None and result_team2 is not None:
                correct_prediction = (user_prediction_team1 == result_team1 and user_prediction_team2 == result_team2)

                if correct_prediction:
                    user = db.query(models.User).filter(models.User.id == user_id)
                    if user:
                        user.score += 1

    db.commit()