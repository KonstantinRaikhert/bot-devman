import os

import telegram
from dotenv import load_dotenv

load_dotenv()

TELEGRAM_TOKEN = os.environ.get("TELEGRAM_TOKEN")

bot = telegram.Bot(token=TELEGRAM_TOKEN)


def send_message(text, chat_id):
    """Отправляет сообщение пользователю в телеграм."""
    bot.sendMessage(chat_id=chat_id, text=text)
