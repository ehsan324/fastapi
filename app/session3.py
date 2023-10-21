from fastapi import FastAPI


app = FastAPI()

@app.get("/blog/all")
def yourInfo(page:str, pagesize:int):
    return {"messge": f"{page} and {pagesize}"}