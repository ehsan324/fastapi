# this is contain session 9 either
# all parameter in query are used in path and body, and vice versa
from fastapi import APIRouter, Query, Body
from pydantic import BaseModel
from typing import Optional

router = APIRouter(prefix='/blog', tags=['blog'])

class BlogModel(BaseModel):
    title: str
    content: str
    num_comment: int
    published: Optional[bool]

@router.post('/new/{id}')
def create_blog(blog: BlogModel, id:int,
    comment_id:int = Query(None, #default value
                       title='Title text!!',
                       description="description Text!!",
                       alias="CommntID",
                       deprecated=True),
    comment:str = Body(...,
                       min_length=10,
                       max_length=20,
                       regex='[A-Z].*',
                       )):

    return {"message": blog, "id": id, "comment_id": comment_id}