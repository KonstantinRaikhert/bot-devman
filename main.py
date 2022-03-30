import logging
import time
from logging import config
from secrets import CHAT_ID, STUDENT_NAME, TELEGRAM_TOKEN, TOKEN

import requests
import telegram

from logging_config import LOGGING_CONFIG

config.dictConfig(LOGGING_CONFIG)

logger = logging.getLogger(__name__)

ENDPOINT = "https://dvmn.org/api/long_polling/"

bot = telegram.Bot(token=TELEGRAM_TOKEN)


def get_status_homework(endpoint, student_name, chat_id):
    """Отправляем статус проверки работы."""
    timestamp = 0
    while True:
        try:
            payload = {"timestamp": timestamp}
            response = requests.get(endpoint, headers={"Authorization": TOKEN}, params=payload)
            response.raise_for_status()
            decoded_response = response.json()
            status = decoded_response.get("status")
            timestamp = decoded_response.get("timestamp_to_request")

            if "error" in decoded_response:
                raise requests.exceptions.HTTPError(decoded_response["error"])

            if status == "found":
                timestamp = decoded_response.get("last_attempt_timestamp")
                last_attempt = decoded_response.get("new_attempts")[0]
                lesson_title = last_attempt["lesson_title"]
                lesson_url = last_attempt["lesson_url"]
                is_negative = "Работа нуждается в доработке." if last_attempt["is_negative"] else "Работа сдана!"
                text = f"{student_name}, урок '{lesson_title}' проверен. {is_negative} Ссылка на урок - {lesson_url}"
                bot.sendMessage(chat_id=chat_id, text=text)

        except requests.exceptions.HTTPError as err:
            logger.error(err)


def main():
    try:
        get_status_homework(
            endpoint=ENDPOINT,
            student_name=STUDENT_NAME,
            chat_id=CHAT_ID,
        )
    except requests.exceptions.ConnectionError as connection_error:
        logger.error(connection_error)
        time.sleep(60)


if __name__ == "__main__":
    logger.info("Запуск приложения.")
    main()
