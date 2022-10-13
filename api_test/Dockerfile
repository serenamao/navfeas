FROM python:3.9

RUN mkdir /src

COPY ./setup.py /
COPY ./requirements.txt /
COPY ./src/ /src/

RUN pip install --upgrade pip; exit 0
RUN pip install -e .

EXPOSE 8080

CMD [ "uvicorn", "src.api:app", "--reload", "--reload-dir", "/src", "--host", "0.0.0.0", "--port", "8080" ]