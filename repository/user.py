from fastapi import status, HTTPException, Depends, APIRouter
import models, schemas, utils
from sqlalchemy.orm import Session
from database import get_db


def create(user: schemas.UserCreate, db: Session):
    # hash the password - user.password
    hashed_password = utils.hash(user.password)
    user.password = hashed_password
    new_user = models.User(**user.dict())
    new_user.score = 0
    db.add(new_user)  # add to database
    db.commit()  # then commit it
    db.refresh(new_user)

    return new_user


def get_user(id: int, db: Session):
    user = db.query(models.User).filter(models.User.id == id).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"User with id: {id}")

    return user
