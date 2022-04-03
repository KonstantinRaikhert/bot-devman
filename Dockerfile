FROM python:3.9-slim-bullseye
WORKDIR /code
COPY .  .
COPY requirements/ requirements/
RUN python -m pip install --upgrade pip
RUN pip install -r requirements/dev.txt
CMD python3 main.py
