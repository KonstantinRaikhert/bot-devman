![python version](https://img.shields.io/pypi/pyversions/nengo.svg)
![black](https://img.shields.io/badge/code%20style-black-000000.svg)

# Dev-man API telegram bot

Этот телеграм бот для получения статуса о проверке домашних заданий от [DevMan](https://dvmn.org/).

### Как развернуть локально:
В приложении используется инструмент для управления зависимостями [Poetry](https://python-poetry.org/docs/)
Подробнее о плюсах и преимуществах [здесь](https://habr.com/ru/post/593529/).

И можно воспользоваться стандартным **PIP**:
* Рекомендую сначала создать и активировать виртуальное окружение
```
python -m venv /path/to/new/virtual/environment
source /path/to/new/virtual/environment/bin/activate
```
* Установить все зависимости для работы бота с файла *requirements.txt*:
```
pip install -r requirements.txt
```
* Необходимо создать `.env` файл с переменными окружения, где:
```
DEVMAN_TOKEN=<Личный токен с сайта devman>
TELEGRAM_TOKEN=<Токен вашего telegram бота>
CHAT_ID=<id диалога в телеграме>
STUDENT_NAME=<имя студента>
```
* Запустить бота командой:
```
python3 main.py
```

### Как развернуть на сервере:
Предусмотрены два способа: [Heroku](https://devcenter.heroku.com/) и любая виртуальная машина.

С Heroku необходимо ознакомиться с официальной документацией.

На VPS необходимо наличие [Docker](https://www.docker.com/) и [docker-compose](https://docs.docker.com/compose/).
Склонируйте репозиторий и запустите:
```
docker-compose -f compose.yaml up -d
```
