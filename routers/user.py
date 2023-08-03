from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
import database, schemas
from repository import user as use

router = APIRouter(
    prefix='/user',
    tags=['User']
)

get_db = database.get_db


@router.post('/', response_model=schemas.ShowUser)
def create_user(request: schemas.User, db: Session = Depends(get_db)):
    return use.create(request, db)


@router.get('/{id}', response_model=schemas.ShowUser)
def show_user(id: int, db: Session = Depends(get_db)):
    return use.get_one(id, db)
