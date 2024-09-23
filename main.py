# main.py

import time
import requests
from config import API_TOKEN
from bot.handlers import handle_message

# URL для обращения к Telegram API
TELEGRAM_API_URL = f"https://api.telegram.org/bot{API_TOKEN}/"


# функция для получения обновлений (новых сообщений)
def get_updates(offset=None):
    url = TELEGRAM_API_URL + "getUpdates"
    params = {'timeout': 100,
              'offset': offset}  # offset нужен для того, чтобы не обрабатывать одни и те же сообщения несколько раз
    response = requests.get(url, params=params)
    return response.json()


# бесконечный цикл для долгого опроса
def main():
    offset = None  # начальное значение смещения
    while True:
        updates = get_updates(offset)

        if updates['ok']:
            for update in updates['result']:
                if 'message' in update and 'text' in update['message']:
                    message_text = update['message']['text']
                    chat_id = update['message']['chat']['id']

                    # обрабатываем сообщение
                    handle_message(message_text, chat_id)

                    # обновляем offset, чтобы не получать одно и то же сообщение снова
                    offset = update['update_id'] + 1

        # небольшая задержка, чтобы не перегружать API
        time.sleep(1)


if __name__ == '__main__':
    main()

