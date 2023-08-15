from typing import List
from fastapi import APIRouter, Depends, status
import schemas, database, models
import schemas, database, oauth2
from sqlalchemy.orm import Session
from repository import match_betting

get_db = database.get_db

#
# @router.get("/", response_model=List[schemas.ShowPlayer])
# # with response_model show data without id
# def all_players(db: Session = Depends(get_db)):
# def all_players(db: Session = Depends(get_db), current_user: schemas.User = Depends(oauth2.get_current_user)):
#     return play.get_all(db)

router = APIRouter(
    prefix='/betting',
    tags=['Match Betting']
)


@router.post('/', status_code=status.HTTP_201_CREATED)
def create(request: schemas.MatchBetting, db: Session = Depends(get_db),
           current_user: schemas.User = Depends(oauth2.get_current_user)):
    return match_betting.create(request, db)

#
# @router.delete('/{id}', status_code=status.HTTP_204_NO_CONTENT)
# def delete_player(id: int, db: Session = Depends(get_db)):
# def delete_player(id: int, db: Session = Depends(get_db),
#                   current_user: schemas.User = Depends(oauth2.get_current_user)):
#     return play.delete(id, db)
#
#
# @router.put('/{id}', status_code=status.HTTP_202_ACCEPTED)
# def update(id: int, request: schemas.Player, db: Session = Depends(get_db)):
# def update(id: int, request: schemas.Player, db: Session = Depends(get_db),
#            current_user: schemas.User = Depends(oauth2.get_current_user)):
#     return play.update(id, request, db)
#
#
# @router.get('/{id}', status_code=status.HTTP_200_OK, response_model=schemas.ShowPlayer)
# def player(id: int, db: Session = Depends(get_db)):
# def player(id: int, db: Session = Depends(get_db), current_user: schemas.User = Depends(oauth2.get_current_user)):
#     return play.get_one(id, db)