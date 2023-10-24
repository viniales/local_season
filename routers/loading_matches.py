from fastapi import Response, status, HTTPException, Depends, APIRouter
from repository import loading_matches
import models, schemas, oauth2
from typing import List, Optional
from sqlalchemy import func
from sqlalchemy.orm import Session
from database import get_db

router = APIRouter(
    prefix='/update_results',
    tags=['Update matches and results']
)


@router.get('/', status_code=status.HTTP_200_OK)
def update_results(db: Session = Depends(get_db)):
    loading_matches.update_or_create_matches_from_file("matches_results.json", db)
    return {"massage": "Results updated"}