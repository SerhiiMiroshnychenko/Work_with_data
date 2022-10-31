import csv

filename = 'data/sitka_weather_07-2018_simple.csv'
with open(filename) as f:
    reader = csv.reader(f)  # Створюємо об'єкт-читач і прив'язуємо його до змінної reader
    header_row = next(reader)  # Функція next() 'наступний' повертає наступний рядок у файлі
    # ^ Викликаємо лише один раз, щоб отримати перший рядок файлу, що містить файлові заголовки
    print(header_row)
