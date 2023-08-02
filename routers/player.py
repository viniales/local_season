from typing import List
from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.orm import Session
import database, schemas, models

router = APIRouter(
    prefix='/player',
    tags=['Players']
)

get_db = database.get_db


@router.get('/', response_model=List[schemas.ShowPlayer])
# with response_model we don't display id
def all_players(db: Session = Depends(get_db())):
    players = db.query(models.Player).all()
    return players


@router.post('/', status_code=status.HTTP_201_CREATED)
def create(request: schemas.Player, db: Session = Depends(get_db)):
    new_player = models.Player(name=request.name, surname=request.surname, age=request.age, team=request.team,
                               nationality=request.nationality, user_id=1)
    db.add(new_player)
    db.commit()
    db.refresh(new_player)
    return new_player


@router.delete('/{id}', status_code=status.HTTP_204_NO_CONTENT)
def delete_player(id, db: Session = Depends(get_db)):
    player = db.query(models.Player).filter(models.Player.id == id)
    if not player.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'Player with id {id} not found')
    player.delete(synchronize_session=False)
    db.commit()
    return 'done'


@router.put('/{id}', status_code=status.HTTP_202_ACCEPTED)
def update(id, request: schemas.Player, db: Session = Depends(get_db)):
    player = db.query(models.Player).filter(models.Player.id == id)
    if not player.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'Player with id {id} not found')
    player.update(
        {models.Player.name: request.name, models.Player.surname: request.surname, models.Player.age: request.age,
         models.Player.team: request.team, models.Player.nationality: request.nationality})
    db.commit()
    return 'updated'


@router.get('/{id}', status_code=status.HTTP_200_OK, response_model=schemas.ShowPlayer)
def player(id, db: Session = Depends(get_db)):
    player = db.query(models.Player).filter(models.Player.id == id).first()
    if not player:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'Player with the id {id} is not available')
        # response.status_code = status.HTTP_404_NOT_FOUND
        # return {'detail':f'Player with the id {id} is not available'}
    return player
