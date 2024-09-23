# bot/handlers.py

from bot.parser import parse_report
from bot.google_sheets import save_to_google_sheets

def handle_message(message_text, chat_id):
    print(f"Получено сообщение: {message_text}")  # логируем полученное сообщение

    # проверяем наличие тегов #День или #Ночь
    if '#День' in message_text or '#Ночь' in message_text:
        report_data = parse_report(message_text)
        if report_data:
            save_to_google_sheets(report_data)
            print("Отчет успешно сохранен в Google Sheets")
        else:
            print("Не удалось распарсить сообщение.")
    else:
        print("Сообщение не содержит тегов #День или #Ночь.")



