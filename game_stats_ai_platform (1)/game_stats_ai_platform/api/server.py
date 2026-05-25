
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Game Stats AI API Running"}
