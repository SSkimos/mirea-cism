from typing import Union
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def basic():
    return {"Hello": "printers"}

@app.get("/printers/")
def read_root():
    return {"Hello": "printers"}
