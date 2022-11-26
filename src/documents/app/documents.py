from typing import Union
import logging
import time
import sys
from fastapi import FastAPI
from jaeger_client import Config
from opentracing_instrumentation.request_context import get_current_span, span_in_context

app = FastAPI()


def init_tracer(service):
    logging.getLogger('').handlers = []
    logging.basicConfig(format='%(message)s', level=logging.DEBUG)
    config = Config(
        config={
            'sampler': {
                'type': 'const',
                'param': 1,
            },
            'logging': True,
        },
        service_name=service,
    )
    return config.initialize_tracer()


@app.get("/")
def basic():
    tracer = init_tracer('test')
    with tracer.start_span('test') as span:
        span.set_tag('test', 'aboba')
    # tracer.close()
    return {"Hello": "documents"}


@app.get("/documents/")
def read_root():
    return {"Hello": "documents"}
