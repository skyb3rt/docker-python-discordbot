FROM python:3.10-slim-buster
COPY ./app /app
WORKDIR /app
RUN pip3 install -r requirements.txt

CMD [ "python3", "app.py"]