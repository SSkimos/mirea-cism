from typing import Union
import logging
import time
import sys
from fastapi import FastAPI
from jaeger_client import Config
from opentracing_instrumentation.request_context import get_current_span, span_in_context

app = FastAPI()


@app.get("/")
def get_main():
    return {"Hello": "documents"}


@app.get("/main")
def get_main():
    return {"foo": "hello", "first": "amigo"}


@app.get("/person")
def get_person():
    return {"name": "John Gold", "age": "75"}
