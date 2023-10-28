import time

from fastapi import APIRouter, Query, Body, Path, Depends, Response, Header, Cookie, Form
from pydantic import BaseModel
from typing import Optional, List, Dict
from schemas import UserBase, UserDisplay
from db import db_user
from db.database import get_db
from fastapi.responses import HTMLResponse, PlainTextResponse

router = APIRouter(prefix='/product', tags=['product'])
product = ['watch', 'mouse', 'keyboard']

async def test_async():
    time.sleep(10)
    return 'ok'

@router.get('/')
def get_all():
    await test_async()
    data = " ".join(product)
    response = Response(content=data, media_type="text/plain")
    response.headers['myheader']= 'Test !'
    response.set_cookie(key='cookie', value='jsut test')
    return response

@router.post('/create')
def create(data:str=Form(...)):
    product.append(data)
    return product

@router.get('/withheader')
def with_header(custom_header:Optional[List[str]] = Header(None), cookie:str = Cookie(None)):
    print(custom_header)
    return {'data': product, 'header': custom_header, 'cookie': cookie}

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
