FROM python:3.10

COPY requirements.txt ./

COPY .env ./

RUN pip install -r requirements.txt

ADD app_api/ /

EXPOSE 8080

CMD [ "python", "app.py" ]