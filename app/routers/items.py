from typing import List

from fastapi import APIRouter, Depends, HTTPException

from sqlalchemy.orm import Session

from app import dependencies as deps, schemas, models, crud


router = APIRouter()

@router.get("/", response_model=List[schemas.Item])
def get_items(db: Session = Depends(deps.get_db), skip: int = 0, limit: int = 20):
    return crud.get_items(db, skip=skip, limit=limit)