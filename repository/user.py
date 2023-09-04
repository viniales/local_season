from sqlalchemy.orm import Session
import models, schemas
from fastapi import status, HTTPException


def check_exist(request: schemas.User, db: Session):
    return db.query(models.User).filter(models.User.name == request.name).first()


def create(request: schemas.User, db: Session):
    if check_exist(request, db):
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail='The User already exist')

    new_user = models.User(name=request.name, email=request.email, password=Hash.bcrypt(request.password))
    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return new_user



