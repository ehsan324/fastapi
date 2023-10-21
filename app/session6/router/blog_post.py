from fastapi import APIRouter
from pydantic import BaseModel
from typing import Optional

router = APIRouter(prefix='/blog', tags=['blog'])

class BlogModel(BaseModel):
    title: str
    content: str
    num_connets: int
    published: Optional[bool]

@router.post('/new')
def create_blog(blog:BlogModel):
    print(blog.title)
    return {"message": "Ok",
            "data": blog}