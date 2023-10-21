#this is contain session7

from fastapi import FastAPI
from router import blog_get
from router import blog_post

app = FastAPI()
app.include_router(blog_get.router)
app.include_router(blog_post.router)


@app.get("/index")
def info():
    return "hello guys"

