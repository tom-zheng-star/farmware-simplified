from sqlalchemy.orm import Session
from app import models,schemas

# user crud operations
def create_user(db: Session, user: schemas.UserCreate):
    # create sqlAlchemy object , from the schema template to db model
    db_user = models.User(
        username = user.username,
        email = user.email,
        password = user.password
    )
    # add object to session
    db.add(db_user)
    # write to real db
    db.commit()
    # refresh object, let db return id and so on to python
    db.refresh(db_user)
    # get the db object (fastapi will use pydantic to turns obj to json)
    return db_user

    # get user by id
def get_user(db:Session,user_id:int):
    # using sqlalchemy  query grammar
    return db.query(models.User).filter(models.User.id == user_id).first()
