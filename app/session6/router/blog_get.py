from fastapi import APIRouter, Response, status
from enum import Enum

router = APIRouter(prefix='/blog', tags=['blog'])

class typeBlog(str, Enum):
    mes1 = "mes1"
    mes2 = "mes2"
    mes3 = "mes3"


@router.get("/{id}/comments/{comment_id}", tags=['comment'])
def get_comment(id:int, comment_id:int, valid:bool = True, username: str = None):
    return {"message": f"blog id {id} comment id {comment_id} {valid=} {username}"}


@router.get("/all",summary="recieve imformation")
def get_blogs(page:int = None, page_size:str = None):
    # this is for typing the description
    """
    **id** this api is for recieving the data

    """
    return {"message": f"{page=} -- {page_size}"}



@router.get("/info", status_code=status.HTTP_200_OK)
def info(pagename: str, pagenum: int, response: Response):
    if pagenum > 10:
        response.status_code = status.HTTP_404_NOT_FOUND
        return {"Error": "the page not found"}
    return {"messgage": f"you are on page {pagename} and page number {pagenum}"}