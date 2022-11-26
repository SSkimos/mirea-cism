from typing import Union
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def get_main():
    return {"Hello": "printers"}


@app.get("/main")
def basic():
    return {"bar": "hola", "second": "world"}

@app.get("/person")
def read_root():
    return {"profession": "Developer", "company": "some"}
