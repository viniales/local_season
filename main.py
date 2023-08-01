from typing import List
from fastapi import FastAPI, Depends, status, Response, HTTPException
import models, schemas
from database import engine, SessionLocal
from sqlalchemy.orm import Session
from hashing import Hash

app = FastAPI()

models.Base.metadata.create_all(engine)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post('/player', status_code=status.HTTP_201_CREATED, tags=['players'])
def create(request: schemas.Player, db: Session = Depends(get_db)):
    new_player = models.Player(name=request.name, surname=request.surname, age=request.age, team=request.team,
                               nationality=request.nationality)
    db.add(new_player)
    db.commit()
    db.refresh(new_player)
    return new_player


@app.delete('/player/{id}', status_code=status.HTTP_204_NO_CONTENT, tags=['players'])
def delete_player(id, db: Session = Depends(get_db)):
    player = db.query(models.Player).filter(models.Player.id == id)
    if not player.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'Player with id {id} not found')
    player.delete(synchronize_session=False)
    db.commit()
    return 'done'


@app.put('/player/{id}', status_code=status.HTTP_202_ACCEPTED, tags=['players'])
def update(id, request: schemas.Player, db: Session = Depends(get_db)):
    player = db.query(models.Player).filter(models.Player.id == id)
    if not player.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'Player with id {id} not found')
    player.update(
        {models.Player.name: request.name, models.Player.surname: request.surname, models.Player.age: request.age,
         models.Player.team: request.team, models.Player.nationality: request.nationality})
    db.commit()
    return 'updated'


@app.get('/player', response_model=List[schemas.ShowPlayer], tags=['players'])
# with response_model we don't display id
def all_players(db: Session = Depends(get_db)):
    players = db.query(models.Player).all()
    return players


@app.get('/player/{id}', status_code=status.HTTP_200_OK, response_model=schemas.ShowPlayer, tags=['players'])
def player(id, db: Session = Depends(get_db)):
    player = db.query(models.Player).filter(models.Player.id == id).first()
    if not player:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'Player with the id {id} is not available')
        # response.status_code = status.HTTP_404_NOT_FOUND
        # return {'detail':f'Player with the id {id} is not available'}
    return player


@app.post('/user', response_model=schemas.ShowUser, tags=['users'])
def create_user(request: schemas.User, db: Session = Depends(get_db)):
    new_user = models.User(name=request.name, email=request.email, password=Hash.bcrypt(request.password))
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user


@app.get('/user/{id}', response_model=schemas.ShowUser, tags=['users'])
def show_user(id: int, db: Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.id == id).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'User with the id {id} is not available')
    return user
