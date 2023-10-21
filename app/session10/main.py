#this sesion is with session 11
from fastapi import FastAPI
from router import blog_post
from router import blog_get

app = FastAPI()
app.include_router(blog_get.router)
app.include_router(blog_post.router)

@app.get('/index')
def init():
    return {"message": "wellcome"}