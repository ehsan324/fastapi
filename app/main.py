from fastapi import FastAPI

app = FastAPI()

@app.get("/get")
def simp():
    return "hello"