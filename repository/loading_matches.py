import json
from sqlalchemy.orm import Session
import models


def update_or_create_matches_from_file(file_path: str, db: Session):
    with open("../matches_results.json", 'r') as file:
        data = json.load(file)

    for match_data in data:
        match_id = match_data["match_id"]
        team1 = match_data["team1"]
        team2 = match_data["team2"]
        result_team1 = match_data["result_team1"]
        result_team2 = match_data["result_team2"]
        date = match_data["date"]

    match = db.query(models.Matches).filter(models.Matches.id == match_id)
    if match:
        if match.result_team1 is None or match.result_team2 is None:
            match.result_team1 = result_team1
            match.result_team2 = result_team2
    else:
        new_match = models.Matches(id=match_id, team1=team1, team2=team2,date=date, result_team1=result_team1,result_team2=result_team2)