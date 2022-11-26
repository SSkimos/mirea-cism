FROM python:3.9

WORKDIR /code

COPY ./requirements.txt /code/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

RUN pip install opentracing-instrumentation
RUN pip install --upgrade "setuptools>=29" "pip>=9"
RUN pip install jaeger-client

COPY ./app /code/app

CMD ["uvicorn", "app.documents:app", "--host", "0.0.0.0", "--port", "5001"]
