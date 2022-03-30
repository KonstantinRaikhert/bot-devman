LOGGING_CONFIG = {
    "version": 1,
    "disable_existing_loggers": True,
    "formatters": {
        "standard": {"format": "%(asctime)s [%(levelname)s] %(name)s: %(message)s"},
    },
    "handlers": {
        "file": {
            "class": "logging.handlers.RotatingFileHandler",
            "formatter": "standard",
            "filename": "bot_chat.log",
            "maxBytes": 1024,
        }
    },
    "loggers": {
        "__main__": {"handlers": ["file"], "level": "INFO", "propagate": False},
    },
}
