# bot/google_sheets.py

import gspread
from oauth2client.service_account import ServiceAccountCredentials

# файл с учетными данными гугл шитс
GOOGLE_SHEETS_FILE = 'credentials.json'

def get_google_sheets_client():
    scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
    creds = ServiceAccountCredentials.from_json_keyfile_name(GOOGLE_SHEETS_FILE, scope)
    client = gspread.authorize(creds)
    return client

def save_to_google_sheets(report_data):
    # преобразуем числовые значения в целые числа
    def parse_int(value):
        return int(value.replace(' ', '').replace('\xa0', '').strip())

    report_data['cash'] = parse_int(report_data['cash'])
    report_data['noncash'] = parse_int(report_data['noncash'])
    report_data['total'] = parse_int(report_data['total'])
    report_data['cashbox'] = parse_int(report_data['cashbox'])
    report_data['bar'] = parse_int(report_data['bar'])
    report_data['reviews'] = int(report_data['reviews'])
    report_data['registrations'] = int(report_data['registrations'])
    report_data['in_file'] = int(report_data['in_file'])

    # подключаемся к гугл шитс
    client = get_google_sheets_client()
    sheet = client.open('WINSTRIKE REPORTS IIG').sheet1  # Замените на название вашей таблицы

    # записываем данные в таблицу
    row = [
        report_data['date'],
        report_data['shift'],
        report_data['admin'],
        report_data['cash'],
        report_data['noncash'],
        report_data['total'],
        report_data['cashbox'],
        report_data['bar'],
        report_data['reviews'],
        report_data['registrations'],
        report_data['in_file']
    ]

    sheet.append_row(row)  # добавляем новую строку с данными


