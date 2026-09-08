from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.database import get_db

from app import schemas,crud


#----------------

router = APIRouter(
    prefix="/users",
    tags=["Users"]
)

# create user (POST
@router.post("/", response_model=schemas.UserResponse, status_code=status.HTTP_201_CREATED)
async def create_user(user:schemas.UserCreate, db:Session=Depends(get_db)):
    db_user = crud.create_user(db=db,user=user)
    return db_user


# get user by id (GET
@router.get("/{user_id}", response_model=schemas.UserResponse)
async def read_user(user_id:int, db:Session=Depends(get_db)):
    db_user = crud.get_user(db=db,user_id=user_id)

    if not db_user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"User with id {user_id} not found"
        )

    return db_user