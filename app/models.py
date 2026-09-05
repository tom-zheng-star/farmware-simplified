from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, func
from sqlalchemy.orm import relationship
from datetime import datetime
from .database import Base

class User(Base):

    __tablename__ = "users"  #It is a SQLAlchemy convention.

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True, nullable=False)
    email = Column(String, unique=True, index=True, nullable=False)
    hashed_password = Column(String, nullable=False)
    role = Column(String, default="worker")  # admin, manager, worker
    created_at = Column(DateTime, default=datetime.utcnow)