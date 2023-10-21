#this contain a session11
# all parameter in query are used in path and body, and vice versa
from fastapi import APIRouter, Query, Body, Path
from pydantic import BaseModel
from typing import Optional, List, Dict

router = APIRouter(prefix='/blog', tags=['blog'])

class Image(BaseModel):
    url: str
    alias: str

class BlogModel(BaseModel):
    title: str
    content: str
    num_comment: int
    published: Optional[bool]
    tags: List[str]
    metadata : Dict[str, str] = {'key', 'value'}
    image: Image



@router.post('/new/{id}/comment/{comment_id}')
def create_blog(blog: BlogModel, id:int,
    comment_title:str = Query(None, #default value
                       title='Title text!!',
                       description="description Text!!",
                       alias="CommntTtile",
                       deprecated=True),
    comment:str = Body(...,
                       min_length=10,
                       max_length=20,
                       regex='[A-Z].*',
                       ),
    v:Optional[List[str]]= Query(None),
    comment_id:int = Path(..., gt=5, le=10),
                ):

    return {"message": blog,
            "id": id,
            "comment_title" : comment_title,
            "comment_id": comment_id,
            "vision": v}