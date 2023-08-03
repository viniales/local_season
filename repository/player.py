from sqlalchemy.orm import Session
import models, schemas
from fastapi import status, HTTPException


def get_all(db: Session):
    players = db.query(models.Player).all()
    return players


def get_one(id: int, db: Session):
    player = db.query(models.Player).filter(models.Player.id == id).first()
    if not player:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'Player with the id {id} is not available')
    return player


def create(request: schemas.Player, db: Session):
    new_player = models.Player(name=request.name, surname=request.surname, age=request.age, team=request.team,
                               nationality=request.nationality, user_id=1)
    db.add(new_player)
    db.commit()
    db.refresh(new_player)
    return new_player


def delete(id: int, db: Session):
    player = db.query(models.Player).filter(models.Player.id == id)
    if not player.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'Player with id {id} not found')
    player.delete(synchronize_session=False)
    db.commit()
    return 'done'


def update(id: int, request: schemas.Player, db: Session):
    player = db.query(models.Player).filter(models.Player.id == id)
    if not player.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'Player with id {id} not found')
    player.update(
        {models.Player.name: request.name, models.Player.surname: request.surname, models.Player.age: request.age,
         models.Player.team: request.team, models.Player.nationality: request.nationality})
    db.commit()
    return 'updated'
