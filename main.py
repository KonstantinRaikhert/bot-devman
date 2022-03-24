from secrets import TELEGRAM_TOKEN, TOKEN

import requests
import telegram

ENDPOINT = "https://dvmn.org/api/long_polling/"

bot = telegram.Bot(token=TELEGRAM_TOKEN)


timestamp = 0


def get_status_homework(endpoint, student_name, chat_id):
    """Отправляем статус проверки работы."""
    global timestamp
    try:
        payload = {"timestamp_to_request": timestamp}
        response = requests.get(endpoint, headers={"Authorization": TOKEN}, params=payload)
        data = response.json()
        timestamp = data.get("timestamp_to_request")

        if data["status"] == "found":
            lesson_title = data["new_attempts"][0]["lesson_title"]
            is_negative = "Работа нуждается в доработке." if data["new_attempts"][0]["is_negative"] else "Работа сдана!"
            lesson_url = data["new_attempts"][0]["lesson_url"]
            name = student_name
            text = f"{name}, урок '{lesson_title}' проверен. {is_negative} Ссылка на урок - {lesson_url}"
            bot.sendMessage(chat_id=chat_id, text=text)
    except requests.exceptions.ReadTimeout as time_out_error:
        print(time_out_error)
    except requests.exceptions.ConnectionError:
        print("Интернет вырубился")


if __name__ == "__main__":

    student_name = input("Введите Ваше имя: \n")
    chat_id = input("Введите Ваш chat_id: \n")
    while True:
        get_status_homework(
            endpoint=ENDPOINT,
            student_name=student_name,
            chat_id=chat_id,
        )
