def select_sorted(sort_columns=None, limit=30, order='asc', filename='dump.csv'):
    # функция сортирует по заданным параметрам
    if sort_columns is None:
        sort_columns = ['high']
    try:
        with open('all_stocks_5yr.csv', encoding='utf-8') as r_file:
            data_high = {}
            data_open_ = {}
            data_low = {}
            data_close = {}
            data_volume = {}
            data_name = {}

            r_file = r_file.readlines()
            text = r_file[1:]  # удаляем первую строку
            for i in text:
                date = i.split(',')[0]  # список по столбцам
                open_ = i.split(',')[1]
                high = i.split(',')[2]
                low = i.split(',')[3]
                close = i.split(',')[4]
                volume = i.split(',')[5]
                name = i.split(',')[6]
                data_high.update({date: high})  # словарь с ключом
                data_open_.update({date: open_})
                data_low.update({date: low})
                data_close.update({date: close})
                data_volume.update({date: volume})
                data_name.update({date: name})

            if sort_columns == ['open_']:   # сортируем
                sorted_values = sorted(data_open_.values())

            if sort_columns == ['high']:
                sorted_values = sorted(data_high.values())

            if sort_columns == ['low']:
                sorted_values = sorted(data_low.values())

            if sort_columns == ['close']:
                sorted_values = sorted(data_close.values())

            if sort_columns == ['volume']:
                sorted_values = sorted(data_volume.values())

            sorted_dict = {}

            for n in sorted_values:  # новый словарь с отсортированными значениями
                for m in data_high.keys():
                    if data_high[m] == n:
                        sorted_dict[m] = data_high[m]
                        break
    except FileNotFoundError:
        print('Невозможно открыть файл')

    keys = list(sorted_dict.keys())  # ключи

    if order == 'desc':   # в обратную сторону
        keys = list(reversed(keys))

    with open(filename, 'a') as file:
        for i in range(limit):
            file.write(
                f'{keys[i]} | {data_open_.get(keys[i])} | {data_high.get(keys[i])} | {data_low.get(keys[i])} | {data_close.get(keys[i])} | {data_volume.get(keys[i])} | {data_name.get(keys[i])}')
    return sorted_dict


print(select_sorted(sort_columns=['open_'], order='desc', limit=10, filename='dump.csv'))
# # создаем объект reader, указываем символ разделитель ","
# file_reader = csv.reader(r_file, delimiter = ",")
# # счетчик для подсчета-количества строк и вывода заголовков столбцов
# count = 0
# # ссчитывание данных из csv файла
# for row in file_reader:
#     if count == 0:
#         # вывод строки, содержащей заголовки для столбцов
#         print(f'файл содержит столбцы: {", ".join(row)}')
#     else:
#         # вывод строк
#         print(f' {row[0]}, {row[1]}, {row[2]}')
#     count +=1
# print(f'Всего в файле {count} строкю')
#
