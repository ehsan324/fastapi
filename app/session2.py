from fastapi import FastAPI
from enum import Enum

app = FastAPI()

@app.get("/index")
def index():
    return "hello guys"

class typeBlog(str, Enum):
    mes1 = "mes1"
    mes2 = "mes2"
    mes3 = "mes3"

@app.get("/blog/type/{type}")
def type_blog(type:typeBlog):
    return {"message": f"blog type is {type}"}

@app.get("/blog/all")
def get_blog():
    return {"message": "blogs all"} 

@app.get('/blog/{id}')
def get_blog(id:int):
    return {'message': f"blog {id}"}