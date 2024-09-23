# bot/parser.py

import re

def parse_report(message_text):
    date_pattern = r"(?P<date>\d{2}[-\.]\d{2}[-\.]\d{4})"  # Дата
    shift_pattern = r"#(?P<shift>День|Ночь)"  # Смена
    admin_pattern = r"(?<=#(?:День|Ночь)\s+.*?\n)(?P<admin>[A-Za-zА-Яа-яЁё\s\.]+)"  # Имя администратора
    cash_pattern = r"Нал\s*ИП\s*Трутнев[:\s]*(?P<cash>[\d\s]+)"  # Нал
    noncash_pattern = r"Безнал\s*ИП\s*Трутнев[:\s]*(?P<noncash>[\d\s]+)"  # Безнал
    total_pattern = r"Итог[:\s]*(?P<total>[\d\s]+)"  # Итог
    cashbox_pattern = r"Касса[:\s]*(?P<cashbox>[\d\s]+)"  # Касса
    bar_pattern = r"Бар[:\s]*(?P<bar>[\d\s]+)"  # Бар
    reviews_pattern = r"Отзывы[:\s]*(?P<reviews>\d+)"  # Отзывы
    registrations_pattern = r"Регистрации[:\s]*(?P<registrations>\d+)"  # Регистрации
    in_file_pattern = r"[Вв]\s*файле[:\s]*(?P<in_file>\d+)"  # В файле

    # шаг 1: парсим дату
    match_date = re.search(date_pattern, message_text)
    if match_date:
        print(f"Дата найдена: {match_date.group('date')}")
    else:
        print("Не удалось распарсить дату.")
        return None

    # шаг 2: парсим смену
    match_shift = re.search(shift_pattern, message_text)
    if match_shift:
        print(f"Смена найдена: {match_shift.group('shift')}")
    else:
        print("Не удалось распарсить смену.")
        return None

    # шаг 3: парсим имя администратора
    lines = message_text.splitlines()
    if len(lines) > 2:
        admin = lines[2].strip()  # Имя администратора на 3-й строке
        print(f"Администратор найден: {admin}")
    else:
        print("Не удалось распарсить администратора.")
        return None

    # шаг 4: парсим финансовые данные
    match_cash = re.search(cash_pattern, message_text)
    match_noncash = re.search(noncash_pattern, message_text)
    match_total = re.search(total_pattern, message_text)
    match_cashbox = re.search(cashbox_pattern, message_text)
    match_bar = re.search(bar_pattern, message_text)
    match_reviews = re.search(reviews_pattern, message_text)
    match_registrations = re.search(registrations_pattern, message_text)
    match_in_file = re.search(in_file_pattern, message_text)

    # проверка и вывод резов
    if match_cash and match_noncash and match_total and match_cashbox and match_bar and match_reviews and match_registrations and match_in_file:
        print(f"Нал ИП Трутнев: {match_cash.group('cash')}")
        print(f"Безнал ИП Трутнев: {match_noncash.group('noncash')}")
        print(f"Итог: {match_total.group('total')}")
        print(f"Касса: {match_cashbox.group('cashbox')}")
        print(f"Бар: {match_bar.group('bar')}")
        print(f"Отзывы: {match_reviews.group('reviews')}")
        print(f"Регистрации: {match_registrations.group('registrations')}")
        print(f"В файле: {match_in_file.group('in_file')}")
    else:
        print("Не удалось распарсить одно из финансовых полей.")
        return None

    return {
        "date": match_date.group("date"),
        "shift": match_shift.group("shift"),
        "admin": admin,
        "cash": match_cash.group("cash"),
        "noncash": match_noncash.group("noncash"),
        "total": match_total.group("total"),
        "cashbox": match_cashbox.group("cashbox"),
        "bar": match_bar.group("bar"),
        "reviews": match_reviews.group("reviews"),
        "registrations": match_registrations.group("registrations"),
        "in_file": match_in_file.group("in_file")
    }

# пример сообщения для тестирования
message_text = """
22.09.2024
#День
Иволга А.И.
Нал ИП Трутнев: 3380
Безнал ИП Трутнев: 27890
Итог: 31270
Касса: 150
Бар: 2300
Отзывы: 0
Регистрации: 1
В файле: 0
"""

# пример вызова функции парсинга
parsed_data = parse_report(message_text)
if parsed_data:
    print("\nРаспарсенные данные:")
    print(parsed_data)













