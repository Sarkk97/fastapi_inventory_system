from typing import List

from fastapi import APIRouter, Depends, HTTPException

from sqlalchemy.orm import Session

from app import dependencies as deps, schemas, models, crud

router = APIRouter()

@router.post("/users/", response_model=schemas.UserInDB, tags=["user"])
def create_user(user: schemas.UserCreate, db: Session = Depends(deps.get_db)):
    #check if user has not been created
    db_user = crud.get_user_by_email(db, email=user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    return crud.create_user(db, user)

@router.get("/users/", response_model=List[schemas.User], tags=["user"])
def get_users(db: Session = Depends(deps.get_db), skip: int = 0, limit: int = 20):
    return crud.get_users(db, skip=skip, limit=limit)

@router.get("/users/{user_id}", response_model=schemas.User, tags=["user"])
def get_user(user_id: int, db: Session = Depends(deps.get_db)):
    #try to get user
    db_user = crud.get_user(db, user_id)
    if db_user is None:
        raise HTTPException(404, detail="User not found")
    return db_user

@router.post(
    "/users/items/",
    response_model=schemas.Item,
    tags=["user"])
def create_user_item(
    item: schemas.ItemCreate,
    db: Session = Depends(deps.get_db),
    user: schemas.User = Depends(deps.get_current_active_user)):

    return crud.create_user_item(db, item, user.id)