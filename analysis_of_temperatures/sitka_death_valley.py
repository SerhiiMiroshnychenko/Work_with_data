import csv
from datetime import datetime

import matplotlib.pyplot as plt

filename_sitka = 'data/sitka_weather_2018_simple.csv'
with open(filename_sitka) as f:
    reader_sitka = csv.reader(f)  # Створюємо об'єкт-читач і прив'язуємо його до змінної reader
    header_row = next(reader_sitka)  # Функція next() 'наступний' повертає наступний рядок у файлі
    # ^ Викликаємо лише один раз, щоб отримати перший рядок файлу, що містить файлові заголовки

    # Отримати дати, високі та низькі температури з цього файлу
    dates_sitka, highs_sitka, lows_sitka = [], [], []
    for row in reader_sitka:  # Об'єкт reader продовжує роботу там, де зупинився останній раз
        # Позаяк ми вже зчитали назви стовпців, то починаємо роботу з їх вмістом
        current_date = datetime.strptime(row[2], '%Y-%m-%d')  # Конвертуємо дані з індексом [2] в datetime об'єкти
        high_sitka = int(row[5])  # Витягаємо данні з індексом [5] -> TMAX == максимальна температура
        low_sitka = int(row[6])  # Витягаємо данні з індексом [6] -> TMIN == максимальна температура
        dates_sitka.append(current_date)  # Формуємо список з дат
        highs_sitka.append(high_sitka)  # Формуємо список з температур
        lows_sitka.append(low_sitka)  # Формуємо список з температур

filename_valley = 'data/death_valley_2018_simple.csv'
with open(filename_valley) as f:
    reader_valley = csv.reader(f)  # Створюємо об'єкт-читач і прив'язуємо його до змінної reader
    header_row = next(reader_valley)  # Функція next() 'наступний' повертає наступний рядок у файлі
    # ^ Викликаємо лише один раз, щоб отримати перший рядок файлу, що містить файлові заголовки

    # Отримати дати, високі та низькі температури з цього файлу
    dates_valley, highs_valley, lows_valley = [], [], []
    for row in reader_valley:  # Об'єкт reader продовжує роботу там, де зупинився останній раз
        # Позаяк ми вже зчитали назви стовпців, то починаємо роботу з їх вмістом
        current_date = datetime.strptime(row[2], '%Y-%m-%d')  # Конвертуємо дані з індексом [2] в datetime об'єкти
        try:
            high_valley = int(row[4])  # Витягаємо данні з індексом [5] -> TMAX == максимальна температура
            low_valley = int(row[5])  # Витягаємо данні з індексом [6] -> TMIN == максимальна температура
        except ValueError:
            print(f"Відсутні данні за {current_date}")
        dates_valley.append(current_date)  # Формуємо список з дат
        highs_valley.append(high_valley)  # Формуємо список з температур
        lows_valley.append(low_valley)  # Формуємо список з температур

# Створити графік високих та низьких температур
plt.style.use('seaborn-v0_8')  # Обираємо стиль
fig, ax = plt.subplots()  # Створюємо діаграми
ax.plot(dates_sitka, highs_sitka, c='blue', alpha=0.5)  # Передаємо список highs, робимо його крапки помаранчевими
# Де alpha=0.5 --> прозорість кольору
ax.plot(dates_sitka, lows_sitka, c='blue', alpha=0.5)  # Передаємо список highs, робимо його крапки червоними
plt.fill_between(dates_sitka, highs_sitka, lows_sitka, facecolor='blue', alpha=0.1)

ax.plot(dates_valley, highs_valley, c='orange', alpha=0.5)  # Передаємо список highs, робимо його крапки помаранчевими
# Де alpha=0.5 --> прозорість кольору
ax.plot(dates_valley, lows_valley, c='orange', alpha=0.5)  # Передаємо список highs, робимо його крапки червоними
plt.fill_between(dates_valley, highs_valley, lows_valley, facecolor='yellow', alpha=0.1)

# Відформатувати графік
plt_title = """Максимальні та мінімальні добові температури, 2018 рік
Жовтим: Долина Смерті, Каліфорнія       Синім: Сітка, Аляска"""
plt.title(plt_title, fontsize=16)  # Задаємо назву
plt.xlabel('', fontsize=16)  # Ось Х
fig.autofmt_xdate()  # Зображає позначки дат діагонально, щоб вони не перетиналися
plt.ylabel('Температура(F)', fontsize=16)  # Ось У
plt.tick_params(axis='both', which='major', labelsize=16)  # Підписи на розмітці

plt.show()  # Відкрити переглядач
