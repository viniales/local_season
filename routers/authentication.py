from fastapi import APIRouter, Depends, HTTPException, status
import schemas, database, models
from sqlalchemy.orm import Session
from hashing import Hash, pwd_context

router = APIRouter(
    tags=['Authentication']
)

get_db = database.get_db


@router.post('/login')
def login(request: schemas.Login, db: Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.email == request.username).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Invalid user')
    if not Hash.verify(request.password, user.password):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Incorrect password')
    # return user
    # now we paste from fastapi OAuth2 documentation
