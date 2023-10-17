from fastapi import FastAPI

app = FastAPI()

@app.get("/post")
def simp():
    return "hello"