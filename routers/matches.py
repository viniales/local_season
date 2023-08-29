# from typing import List
# from fastapi import APIRouter, Depends, status
# import schemas, database, models
# import schemas, database, oauth2
# from sqlalchemy.orm import Session
# from repository import matches
#
# get_db = database.get_db
#
# router = APIRouter(
#     prefix='/matches',
#     tags=['Matches']
# )
#
#
# @router.post('/', status_code=status.HTTP_201_CREATED)
# def create(request: schemas.Match, db: Session = Depends(get_db)):
#     return matches.create(request, db)
