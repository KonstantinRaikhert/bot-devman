import logging


class TelegramLogsHandler(logging.StreamHandler):
    def __init__(self, telegram_chat_id, telegram_bot):
        super().__init__()
        self.chat_id = telegram_chat_id
        self.telegram_bot = telegram_bot

    def emit(self, record):
        log_entry = self.format(record)
        self.telegram_bot.sendMessage(chat_id=self.chat_id, text=log_entry)
