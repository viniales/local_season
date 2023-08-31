from fastapi import APIRouter, status, Depends
from database import get_db
from sqlalchemy.orm import Session
from repository import calculate_score

router = APIRouter(prefix='calculate_score', tags=['Calculate score'])


@router.get('/', status_code=status.HTTP_200_OK)
def calculate_and_update_scores(db: Session = Depends(get_db)):
    calculate_score.calculate_score(db)
    return {"massage": "Scores updated"}
