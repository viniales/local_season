from typing import List
from fastapi import APIRouter, Depends, status
import schemas, database, models
from sqlalchemy.orm import Session
from repository import player as play

router = APIRouter(
    prefix='/player',
    tags=['Players']
)
get_db = database.get_db


@router.get("/", response_model=List[schemas.ShowPlayer])
# with response_model show data without id
def all_players(db: Session = Depends(get_db)):
    return play.get_all(db)


@router.post('/', status_code=status.HTTP_201_CREATED)
def create(request: schemas.Player, db: Session = Depends(get_db)):
    return play.create(request, db)


@router.delete('/{id}', status_code=status.HTTP_204_NO_CONTENT)
def delete_player(id: int, db: Session = Depends(get_db)):
    return play.delete(id, db)


@router.put('/{id}', status_code=status.HTTP_202_ACCEPTED)
def update(id: int, request: schemas.Player, db: Session = Depends(get_db)):
    return play.update(id, request, db)


@router.get('/{id}', status_code=status.HTTP_200_OK, response_model=schemas.ShowPlayer)
def player(id: int, db: Session = Depends(get_db)):
    return play.get_one(id, db)
