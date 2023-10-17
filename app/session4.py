from fastapi import FastAPI, Response, status


app = FastAPI()

@app.get("/blog/info", status_code= status.HTTP_200_OK)
def info(pagename:str, pagenum:int, response:Response):
    if pagenum > 10 :
        response.status_code = status.HTTP_404_NOT_FOUND
        return {"Error": "the page not found"}
    return {"messgage": f"you are on page {pagename} and page number {pagenum}"}