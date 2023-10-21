from fastapi import APIRouter, Query, Body, Path, Depends
from pydantic import BaseModel
from typing import Optional, List, Dict
from echemas import UserBase, UserDisplay
from db.database import get_db


router = APIRouter(prefix='/user', tags=['user'])


# create user
@router.post('/', response_model=UserDisplay)
def create_user(user:UserBase, db=Depends(get_db)):
    return create_user(db, user)


# read user


# update user


# delete user