LOGGING_CONFIG = {
    "version": 1,
    "disable_existing_loggers": True,
    "formatters": {
        "standard": {"format": "%(asctime)s [%(levelname)s] %(name)s: %(message)s"},
        "tg_formatter": {"format": "[%(levelname)s] %(name)s: %(message)s"},
    },
    "handlers": {
        "file": {
            "class": "logging.handlers.RotatingFileHandler",
            "formatter": "standard",
            "filename": "bot_chat.log",
            "maxBytes": 1024,
        },
        "telegram": {
            "class": "logging_telegram_handler.TelegramLogsHandler",
            "formatter": "tg_formatter",
        },
        "console": {
            "class": "logging.StreamHandler",
            "formatter": "standard",
        },
    },
    "loggers": {
        "__main__": {"handlers": ["file", "console", "telegram"], "level": "INFO", "propagate": False},
    },
}
