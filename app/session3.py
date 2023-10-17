from fastapi import FastAPI


app = FastAPI()

@app.get("/blog/all")
def yourInfo(page:int, pagesize:str):
    return {"messge": f"{page} and {pagesize}"}