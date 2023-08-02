from typing import List
from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.orm import Session
import database, schemas, models

router = APIRouter(
    prefix='/user',
    tags=['Players']
)

get_db = database.get_db