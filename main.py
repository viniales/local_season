from fastapi import FastAPI, Depends, status, Response
import models, schemas
from database import engine, SessionLocal
from sqlalchemy.orm import Session

app = FastAPI()

models.Base.metadata.create_all(engine)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post('/player', status_code=status.HTTP_201_CREATED)
def create(request: schemas.Player, db: Session = Depends(get_db)):
    new_player = models.Player(name=request.name, surname=request.surname, age=request.age, team=request.team,
                               nationality=request.nationality)
    db.add(new_player)
    db.commit()
    db.refresh(new_player)
    return new_player


@app.get('/player')
def all_players(db: Session = Depends(get_db)):
    players = db.query(models.Player).all()
    return players


@app.get('/player/{id}', status_code=status.HTTP_200_OK)
def player(id, response: Response,db: Session = Depends(get_db)):
    player = db.query(models.Player).filter(models.Player.id == id).first()
    if not player:
        response.status_code = status.HTTP_404_NOT_FOUND
        return {'detail':f'Player with the id {id} is not available'}
    return player
