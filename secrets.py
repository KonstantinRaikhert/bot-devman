import os

from dotenv import load_dotenv

load_dotenv()

TELEGRAM_TOKEN = os.environ.get("TELEGRAM_TOKEN")
TOKEN = os.environ.get("DEVMAN_TOKEN")
CHAT_ID = os.environ.get("CHAT_ID")
STUDENT_NAME = os.environ.get("STUDENT_NAME")
