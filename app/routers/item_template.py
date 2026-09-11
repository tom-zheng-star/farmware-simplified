
from fastapi import APIRouter,Depends,HTTPException,status
from sqlalchemy.orm import Session
from app.database import get_db
from app import schemas,crud



router = APIRouter(
    prefix="/item_templates",
    tags=["ItemTemplates"]
)

# create item template (POST)
@router.post("/",response_model=schemas.ItemTemplateResponse,status_code=status.HTTP_201_CREATED)
async def create_item_template(item_template:schemas.ItemTemplateCreate,db:Session=Depends(get_db)):
    db_item_template = crud.create_item_template(db=db,item_template=item_template)
    return db_item_template

# get item template by id (GET)
@router.get("/{item_template_id}",response_model=schemas.ItemTemplateResponse)
async def read_item_template(item_template_id:int, db:Session=Depends(get_db)):
    db_item_template = crud.get_item_template(item_template_id=item_template_id,db=db)
    if not db_item_template:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"template with id {item_template_id} not found."
        )
    return db_item_template
