FROM python:3.8.6-buster

RUN mkdir -p /opt/app
RUN mkdir -p /opt/data
ADD . /opt/app
WORKDIR /opt/app

RUN pip install -r requirements.txt

EXPOSE 8000

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]