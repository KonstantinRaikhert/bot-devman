import logging
import os
import time
from logging import config

import requests
import telegram
from dotenv import load_dotenv

from logging_config import LOGGING_CONFIG

logger = logging.getLogger(__name__)

ENDPOINT = "https://dvmn.org/api/long_polling/"


def get_status_homework(endpoint, devman_token, telegram_bot, student_name, chat_id):
    """Отправляем статус проверки работы."""
    timestamp = 0
    while True:
        try:
            payload = {"timestamp": timestamp}
            response = requests.get(endpoint, headers={"Authorization": devman_token}, params=payload)
            response.raise_for_status()
            review_info = response.json()
            status = review_info.get("status")
            timestamp = review_info.get("timestamp_to_request")

            if status == "found":
                timestamp = review_info.get("last_attempt_timestamp")
                last_attempt = review_info.get("new_attempts")[0]
                lesson_title = last_attempt["lesson_title"]
                lesson_url = last_attempt["lesson_url"]
                is_negative = "Работа нуждается в доработке." if last_attempt["is_negative"] else "Работа сдана!"
                text = f"{student_name}, урок '{lesson_title}' проверен. {is_negative} Ссылка на урок - {lesson_url}"
                telegram_bot.sendMessage(chat_id=chat_id, text=text)

        except requests.exceptions.HTTPError as http_error:
            logger.error(http_error)
        except requests.exceptions.ReadTimeout as timeout_error:
            logger.error(timeout_error)
        except requests.exceptions.ConnectionError as connection_error:
            logger.error(connection_error)
            time.sleep(60)


def main():
    load_dotenv()

    config.dictConfig(LOGGING_CONFIG)
    logger.info("Запуск приложения.")

    telegram_token = os.environ.get("TELEGRAM_TOKEN")
    devman_token = os.environ.get("DEVMAN_TOKEN")
    telegram_chat_id = os.environ.get("CHAT_ID")
    student_name = os.environ.get("STUDENT_NAME")

    telegram_bot = telegram.Bot(token=telegram_token)

    get_status_homework(
        endpoint=ENDPOINT,
        devman_token=devman_token,
        telegram_bot=telegram_bot,
        student_name=student_name,
        chat_id=telegram_chat_id,
    )


if __name__ == "__main__":
    main()
