import csv
from idlelib.multicall import r
from turtle import pd
import pandas as pd
from distlib.compat import raw_input


def cache(f):    # декоратор для запоминания
    cache = {}

    def wrapper(*args, **kwargs):
        key = tuple(f'{f}, {args}, {kwargs}')
        if key not in cache:
            cache[key] = f(*args, **kwargs)
        return cache[key]

    return wrapper


@cache
def select_sorted():  # сортировка
    sorted_collection = raw_input("open(1), close(2), high(3), low(4), volume(5):") or "high"
    if sorted_collection == '1':
        sorted_collection = 'open'
    elif sorted_collection == '2':
        sorted_collection = 'close'
    elif sorted_collection == '3':
        sorted_collection = 'high'
    elif sorted_collection == '4':
        sorted_collection = 'low'
    elif sorted_collection == '5':
        sorted_collection = 'volume'

    order = raw_input('по возрастанию [1] / по убыванию [2]: ') or 'asc'
    if order == '1':
        order = 'asc'
    elif order == '2':
        order = 'desc'

    limit = raw_input('до [10]: ') or '10'
    filename = raw_input('сохранить данные в [dump.csv]: ') or 'dump.csv'

    return select_sorted_func(sorted_collection, order, limit, filename)


@cache
def select_sorted_func(sorted_collection='high', order='asc', limit=10, filename='dump.csv'):  # функция для сортировки
    with open('all_stocks_5yr.csv', 'w') as file:
        reader = list(csv.DictReader(file))  # читаем файл
    df = pd.DataFrame(reader)

    if order == 'desc':  # проверка, в каком прядке написано
        sort_d = df.sort_values(sorted_collection, ascending=False)
    else:
        sort_d = df.sort_values(sorted_collection)

    a = sort_d.to_dict('records')

    with open(filename, 'a') as file:
        file.write('date, open, high, low, close, volume, name\n') # запись в файл
        for i in range(int(limit)):
            file.write(
                f'{r[i]["date"]}, {r[i]["open"]}, {r[i]["high"]}, {r[i]["low"]}, {r[i]["close"]}, {r[i]["volume"]}, {r[i]["name"]}\n')

    return sort_d


def get_by_date():  #для выбора пользователя
    date = raw_input('date [date]: ') or 'date'
    name = raw_input('ticker [date]: ') or 'date'
    filename = raw_input('file [dump2.csv]: ') or 'dump2.csv'

    get_by_date_func(date, name, filename)


def get_by_date_func(date="2017-08-08", name="PCLN", filename="dump2.csv"):  # функцтя для выбора
    with open("dump.csv", "w") as file:
        reader = list(csv.DictReader(file))

    new = []
    for i in reader:
        if i.get('name') == name and i.get('date') == date:
            new.append(i)

    for i in reader:
        if date != 'date' and name != 'date' and i.get('name') == name and i.get('date') == date:
            new.append(i)
        elif date == 'date' and name == 'date':
            new.append(i)
        elif date == 'date' and name != 'date' and i.get('name') == name:
            new.append(i)
    with open(filename, 'a') as file:
        file.write(f'{new} \n')


get_by_date_func(date='2017-08-08', name='PCLN', filename='dump2.csv')
