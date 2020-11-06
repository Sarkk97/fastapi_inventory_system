from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from .config import settings

#create sqlalchemy engine
engine = create_engine(settings.SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})

#create Session class (db session). The class is not yet a db session
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

#create Base class which is a superclass for ORM model classes
Base = declarative_base()