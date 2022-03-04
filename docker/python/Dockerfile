FROM python:3.10-slim-buster
COPY ./app /app
WORKDIR /app
RUN python -m pip install --upgrade pip
RUN pip3 install -r requirements.txt

CMD [ "python3", "app.py"]