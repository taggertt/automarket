import json
import os
def is_not_int(value):
    if value.replace('.', '', 1).isnumeric() == False:
        return True
    else:
        return False


"""Проверки вводимых значений"""
def add_check_int_filed(intro_phrase):
    text = input(intro_phrase)
    while is_not_int(text):
        text = input('Введите числовое значение вида "1" или "1.0": ')
    if '.' in text:
        text = float(text)
        return text
    else:
        text = int(text)
        return text

def add_id_for_compare(intro_phrase):
    text = input(intro_phrase)
    while is_not_int(text):
        text = input('Введите целое число: ')
    return text

def add_no_empty(intro_phrase):
    text = input(intro_phrase)
    spec_chars = '?><\\/|'
    while any(x in text for x in spec_chars) or text.strip() == '' or len(text) < 3:
        text = input('Поле не может быть пустым, содержать спец символы или состоять из менее 3 символов. Повторите ввод: ')
    return text


"""Работа с файлами (БД)"""

def make_dir(path):
    os.makedirs(os.path.dirname(path), exist_ok=True)

def record_file(data, file):
    if os.path.exists(file) and os.path.getsize(file) > 0: # Проверка существует файл и пустой ли он
        with open(file, 'r', encoding = 'UTF-8') as fr:
            json_data = json.load(fr)                      # Считываются данны из файла в переменную, чтоб туда записать новые данные
    else:
        json_data = {}

    json_data.update(data) # Запись новых данных в переменную

    with open(file, 'w', encoding = 'UTF-8') as fw: # Запись данных в файл
        json.dump(json_data, fw, ensure_ascii = False, indent=4)

def read_file(file):
    if os.path.exists(file) and os.path.getsize(file) > 0:
        with open(file, 'r', encoding = 'UTF-8') as fr:
            export = json.load(fr)
            print(json.dumps(export, ensure_ascii = False, indent = 4)) # Преобразование python-объекта в объект-json
    else:
        print()
        print('Файл авторынка пуст.')
        print('Вы можете добавить авто, используя меню.')
        print()


def compare_car(file, a, b): # Сравнение двух авто
    print()
    if not os.path.exists(file) or os.path.getsize(file) == 0:
        return print('Файл пуст или не существует')
    else:
        a1 = ''
        b1 = ''
        i = 0
        c = 0
        with open(file, 'r', encoding = 'UTF-8') as fr:
            export = json.load(fr)
            if len(export) > 1:
                while a1 == '':
                    a1 = export.get(a, '')
                    if a1 == '':
                        print(f'Введённый ID "{a}" - не существует')
                        a = input('Введите существующий ID: ')
                        i += 1
                    if i > 2:
                        print()
                        return print('Проверьте ID в базе данных файла после чего повторите сравнение авто.')

                while b1 == '':
                    b1 = export.get(b, '')
                    if b1 == '':
                        print(f'Введённый ID "{b}" - не существует')
                        b = input('Введите существующий ID: ')
                        c += 1
                    if c > 2:
                        print()
                        return print('Проверьте ID в базе данных файла после чего повторите сравнение авто.')

            else:
                return print('Нужно больше авто для сравнения. Добавьте авто в базу.')

            print()
            print(f'Авто с ID - {a}')
            for k, v in a1.items():
                print(f'"{k}": "{v}",')

            print()
            print(f'Авто с ID - {b}')
            for k, v in b1.items():
                print(f'"{k}": "{v}",')


def clean_file(file):
    with open(file, 'w') as fclean:
        fclean.write('')


def get_last_id(file): # Проверка последнего ID для работы с базой
    if os.path.exists(file) and os.path.getsize(file) > 0:
        with open(file, 'r') as fr:
            base = json.load(fr)
            return len(base)
    else:
        return 0