from datetime import date

from CarModel import Car
from TrackModel import Track
from func import *

"""Исполняемый файл"""

def save_item(car_item):
    cars[car_item.id] = {
        "model": car_item.model,
        "year": car_item.year,
        "engine": car_item.engine,
        "cost": car_item.cost,
        "mileage": car_item.mileage,
        "updated_at": car_item.updated_at
    }


"""Добавление авто или грузовика"""
def add_item():
    ch_1 = input("ВЫ находитесь в меню добавления авто. Введите 1, если хотите добавить авто. Или введите 2, "
                 "если хотите добавить грузовой транспорт: ")
    while ch_1 != '1' and ch_1 != '2':
        ch_1 = input('Введите 1 или 2: ')
    if ch_1 == '1':
        new_id = get_last_id(file_path) + 1
        new_model = add_no_empty('Введите модель автомобиля: ')
        new_year = add_check_int_filed('Введите год выпуска автомобиля : ')
        new_engine = add_check_int_filed('Введите объём двигателя автомобиля в л.: ')
        new_cost = add_check_int_filed('Введите цену автомобиля в $: ')
        new_mileage = add_check_int_filed('Введите пробег автомобиля в км.: ')
        new_updated_at = date.today().isoformat()

        return Car(new_id, new_model, new_year, new_engine, new_cost, new_mileage, new_updated_at)

    elif ch_1 == '2':
        new_id = get_last_id(file_path) + 1
        new_model = add_no_empty('Введите модель грузовика: ')
        new_year = add_check_int_filed('Введите год выпуска грузовика: ')
        new_engine = add_check_int_filed('Введите объём двигателя грузовика л.: ')
        new_cost = add_check_int_filed('Введите цену грузовика в $: ')
        new_mileage = add_check_int_filed('Введите пробег грузовика в км.: ')
        new_updated_at = date.today().isoformat()

        return Track(new_id, new_model, new_year, new_engine, new_cost, new_mileage, new_updated_at)


"""Стартовое меню авторынка"""
cars = {}
ch_2 = 'да'
file_path = 'result/file.txt' # Путь к файлу с результатами (база).
make_dir(file_path)

while ch_2 == 'да':
    print()
    print('Сервис Python-авторынок. Выберите дальнейшее действие:')
    print('1. Добавить авто на рынок')
    print('2. Посмотреть авто загруженные в эту сессию')
    print('3. Выгрузить данные из файла')
    print('4. Очистить данные из файла')
    print('5. Сравнение авто')
    print('6. Завершить работу Python-авторынок')
    a = input('Для выбора действия нажмите нужную цифру: ')
    while a not in '123456' or a == ' ':
        a = input('Введите 1 - 6: ')
    if a == '1':
        save_item(add_item())
        record_file(cars, file_path)
    elif a == '2':
        print(cars)
    elif a == '3':
        read_file(file_path)
    elif a == '4':
        clean_file(file_path)
    elif a == '5':
        item_1 = add_id_for_compare('Введите ID авто из файла целым числом: ')
        item_2 = add_id_for_compare('Введите ID авто из файла целым числом: ')
        compare_car(file_path, item_1, item_2)
    elif a == '6':
        print('Вы закончили работу в Python-авторынок. Удачи на дорогах!')
        break

    print('Хотите продолжить работу в Python-авторынок?')
    ch_2 = input('Нажмите Да/Нет: ').lower()
    while ch_2 != 'да' and ch_2 != 'нет':
        ch_2 = input('Нажмите Да/Нет: ').lower()
    if ch_2 == 'нет':
        print('Вы закончили работу в Python-авторынок. Удачи на дорогах!')
        break

input("\nНажмите Enter, чтобы закрыть программу...")