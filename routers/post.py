from fastapi import APIRouter, Depends, UploadFile, File
from routers.schemas import ItemBase, ItemDisplay
from sqlalchemy.orm.session import Session
from database.database import get_db
from database import db_post
import string
import random
import shutil

router = APIRouter(prefix='/post', tags=['post'])

@router.post('')
def create(request: ItemBase, db: Session = Depends(get_db)):
    return db_post.create(db, request)

@router.get('/all')
def posts(db: Session = Depends(get_db)):
    return db_post.get_all(db)

