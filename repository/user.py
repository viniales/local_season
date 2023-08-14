from sqlalchemy.orm import Session
import models, schemas
from fastapi import status, HTTPException
from hashing import Hash


def check_exist(request: schemas.User, db: Session):
    return db.query(models.User).filter(models.User.name == request.name).first()


def create(request: schemas.User, db: Session):
    if check_exist(request, db):
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail='The User already exist')

    new_user = models.User(name=request.name, email=request.email, password=Hash.bcrypt(request.password), points=0)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return new_user


def get_one(id, db: Session):
    user = db.query(models.User).filter(models.User.id == id).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'User with the id {id} is not available')
    return user
