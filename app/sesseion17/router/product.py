from fastapi import APIRouter, Query, Body, Path, Depends, Response
from pydantic import BaseModel
from typing import Optional, List, Dict
from schemas import UserBase, UserDisplay
from db import db_user
from db.database import get_db
from fastapi.responses import HTMLResponse, PlainTextResponse

router = APIRouter(prefix='/product', tags=['product'])
product = ['watch', 'mouse', 'keyboard']


@router.get('/')
def get_all():
    data = " ".join(product)
    return Response(content=data, media_type="text/plain")

@router.get('/{id}',responses={
    404:{"content":{"text/plain":{'example': "product not found !"}},"description": "vaghti mahsol peyda bashe"},
    200:{}
})
def get_id(id:int):
    text = 'data not found'
    if id > len(product):
        return PlainTextResponse(status_code=404,content=text, media_type='text/plain')
    data = product[id]
    return HTMLResponse(content=f"<div> {data} <div>", media_type="text/html")
