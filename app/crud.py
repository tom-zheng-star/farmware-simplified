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


# item template crud
def create_item_template(db:Session, item_template: schemas.ItemTemplateCreate):
    db_item_template = models.ItemTemplate(
        name = item_template.name,
        sku = item_template.sku,
        description = item_template.description,
        unit = item_template.unit
    )
    db.add(db_item_template)
    db.commit()
    # let db return id, etc...
    db.refresh(db_item_template)
    return db_item_template

def get_item_template(db:Session, item_template_id:int):
    return db.query(models.ItemTemplate).filter(models.ItemTemplate.id == item_template_id).first()


# inventory item (inventory) crud
def create_inventory(db:Session, inventory:schemas.InventoryCreate):
    db_inventory = models.Inventory(
        template_id = inventory.template_id,
        quantity = inventory.quantity
    )
    db.add(db_inventory)
    db.commit()
    db.refresh(db_inventory)
    return db_inventory

def get_inventory(db:Session, inventory_id:int):
    return db.query(models.Inventory).filter(models.Inventory.id == inventory_id).first()


# logs crud (r only for read only)
def get_item_template_log(db:Session,log_id:int):
    return db.query(models.TemplateLog).filter(models.TemplateLog.id == log_id).first

def get_inventory_log(db:Session,log_id:int):
    return db.query(models.InventoryLog).filter(models.InventoryLog.id == log_id).first