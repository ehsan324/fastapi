# please learn about exception handler
#tis session was about errors and response type (json, text and ...)
from fastapi import FastAPI
from router import blog_get
from router import blog_post
from router import user
from router import article
from router import product
from db import models
from db.database import engine

app = FastAPI()
app.include_router(blog_get.router)
app.include_router(blog_post.router)
app.include_router(user.router)
app.include_router(article.router)
app.include_router(product.router)
models.Base.metadata.create_all(engine)

@app.get('/')
def hello():
    return 'hello world'

