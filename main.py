import os

import requests
from dotenv import load_dotenv

load_dotenv()

url = "https://dvmn.org/api/long_polling/"
# url ='https://dvmn.org/api/user_reviews/'
token = os.environ.get("DEVMAN_TOKEN")

timestamp = 0


def get(url):
    """Что делает этот метод."""
    try:
        global timestamp
        print(timestamp)
        payload = {"timestamp_to_request": timestamp}
        response = requests.get(url, headers={"Authorization": token}, params=payload)
        timestamp = response.json()["timestamp_to_request"]
        print(response.json())
    except requests.exceptions.ReadTimeout as time_out_error:
        print(time_out_error)
    except requests.exceptions.ConnectionError:
        print("Интеренет вырубился")


if __name__ == "__main__":
    while True:
        get(url)
