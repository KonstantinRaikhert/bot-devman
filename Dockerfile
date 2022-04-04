FROM python:3.9-slim-bullseye
WORKDIR /code
COPY .  .
RUN python -m pip install --upgrade pip
RUN pip install -r requirements.txt
CMD python3 main.py
