from typing import List, Optional

from sqlalchemy.orm import Session

from . import models, schemas, security

'''
*** READ *******
- read single user by id and email
- read multiple users
- read all items
'''
def get_user(db: Session, user_id: int) -> Optional[models.User]:
    return db.query(models.User).filter(models.User.id == user_id).first()

def get_user_by_email(db: Session, email: str) -> Optional[models.User]:
    return db.query(models.User).filter(models.User.email == email).first()

def get_users(db: Session, skip: int = 0, limit: int = 100) -> List[models.User]:
    return db.query(models.User).offset(skip).limit(limit).all()

def get_items(db: Session, skip: int = 0, limit: int = 100) -> List[models.Item]:
    return db.query(models.Item).offset(skip).limit(limit).all()

'''
**** CREATE ******
- create new user
- create new item
Steps:
1. Create SqlAlchemy Model instance with data
2. add data to db session
3. commit changes to db
4. refresh instance data from db 
'''
def create_user(db: Session, user: schemas.UserCreate) -> models.User:
    hashed_password = security.hash_password(user.password)
    db_user = models.User(email=user.email, password=hashed_password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def create_user_item(db: Session, item: schemas.ItemCreate, user_id: int) -> models.Item:
    db_item = models.Item(**item.dict(), owner_id=user_id)
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item