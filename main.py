from fastapi import FastAPI, Depends
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


@app.post('/player')
def create(request: schemas.Player, db: Session = Depends(get_db)):
    new_player = models.Player(name=request.name, surname=request.surname, age=request.age, team=request.team,
                               nationality=request.nationality)
    db.add(new_player)
    db.commit()
    db.refresh(new_player)
    return new_player
