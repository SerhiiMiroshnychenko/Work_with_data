import csv


filename = 'data/world_fires_1_day.csv'
with open(filename) as f:
    reader = csv.reader(f)  # Створюємо об'єкт-читач і прив'язуємо його до змінної reader
    header_row = next(reader)  # Функція next() 'наступний' повертає наступний рядок у файлі
    # ^ Викликаємо лише один раз, щоб отримати перший рядок файлу, що містить файлові заголовки

    for index, column_header in enumerate(header_row):  # Функція enumerate() повертає
        # індекс кожного елемента та його значення
        print(index, column_header)  # Виводимо індекси стовпців та іх назви

"""
0 latitude
1 longitude
2 bright_ti4
3 scan
4 track
5 acq_date
6 acq_time
7 satellite
8 confidence
9 version
10 bright_ti5
11 frp
12 daynight

0 широти
1 довгота
2 яскравий_ti4
3 сканування
4 трек
5 acq_date
6 acq_time
7 супутник
8 впевненість
9 версія
10 яскравий_ti5
11 франків
12 день вночі
"""