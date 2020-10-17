FROM python:3.8.6-buster

RUN pip install --upgrade pip
RUN pip install --upgrade setuptools
RUN pip install flake8 
RUN pip install autopep8

RUN pip install fastapi
RUN pip install uvicorn

RUN pip install databases
RUN pip install sqlalchemy
RUN pip install aiosqlite
