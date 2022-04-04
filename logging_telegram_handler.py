import logging
import os

import telegram


class TelegramLogsHandler(logging.StreamHandler):
    def __init__(self):
        super().__init__()
        self.chat_id = os.environ.get("CHAT_ID")
        self.telegram_token = os.environ.get("TELEGRAM_TOKEN")

    @property
    def tg_bot(self):
        return telegram.Bot(token=self.telegram_token)

    def emit(self, record):
        log_entry = self.format(record)
        self.tg_bot.sendMessage(chat_id=self.chat_id, text=log_entry)
