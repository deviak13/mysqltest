from fastapi import HTTPException, status
from routers.schemas import ItemBase
from sqlalchemy.orm.session import Session
from database.models import DbItem
import datetime

def create(db: Session, request: ItemBase):
    new_item = DbItem(
        title = request.title,
        timestamp = datetime.datetime.now()
    )
    db.add(new_item)
    db.commit()
    db.refresh(new_item)
    return new_item

def get_all(db: Session):
    return db.query(DbItem).all()

