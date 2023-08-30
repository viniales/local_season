import json
from sqlalchemy.orm import Session
import models


def update_or_create_matches_from_file(file_path: str, db: Session):
    with open(file_path, 'r') as file:
        data = json.load(file)

    for match_data in data:
        match_id = match_data["match_id"]
        result_team1 = match_data["result_team1"]
        result_team2 = match_data["result_team2"]
        team1 = match_data["team1"]
        team2 = match_data["team2"]
        date = match_data["date"]

        match = db.query(models.Match).filter(models.Match.id == match_id).first()
        if match:
            if match.result_team1 is None or match.result_team2 is None:
                match.result_team1 = result_team1
                match.result_team2 = result_team2
        else:
            new_match = models.Match(id=match_id, team1=team1, team2=team2, result_team1=result_team1,
                                     result_team2=result_team2, date=date)
            db.add(new_match)

    db.commit()
