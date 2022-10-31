import csv
from datetime import datetime

import matplotlib.pyplot as plt

filename = 'data/sitka_weather_2018_simple.csv'
with open(filename) as f:
    reader = csv.reader(f)  # Створюємо об'єкт-читач і прив'язуємо його до змінної reader
    header_row = next(reader)  # Функція next() 'наступний' повертає наступний рядок у файлі
    # ^ Викликаємо лише один раз, щоб отримати перший рядок файлу, що містить файлові заголовки

    # Отримати дати, високі та низькі температури з цього файлу
    dates, highs, lows = [], [], []
    for row in reader:  # Об'єкт reader продовжує роботу там, де зупинився останній раз
        # Позаяк ми вже зчитали назви стовпців, то починаємо роботу з їх вмістом
        current_date = datetime.strptime(row[2], '%Y-%m-%d')  # Конвертуємо дані з індексом [2] в datetime об'єкти
        high = int(row[5])  # Витягаємо данні з індексом [5] -> TMAX == максимальна температура
        low = int(row[6])  # Витягаємо данні з індексом [6] -> TMIN == максимальна температура
        dates.append(current_date)  # Формуємо список з дат
        highs.append(high)  # Формуємо список з температур
        lows.append(low)  # Формуємо список з температур

# Створити графік високих та низьких температур
plt.style.use('seaborn-v0_8')  # Обираємо стиль
fig, ax = plt.subplots()  # Створюємо діаграми
ax.plot(dates, highs, c='orange', alpha=0.5)  # Передаємо список highs, робимо його крапки помаранчевими
# Де alpha=0.5 --> прозорість кольору
ax.plot(dates, lows, c='blue', alpha=0.5)  # Передаємо список highs, робимо його крапки червоними
plt.fill_between(dates, highs, lows, facecolor='yellow', alpha=0.1)

# Відформатувати графік
plt.title('Максимальні та мінімальні добові температури, 2018 рік', fontsize=24)  # Задаємо назву
plt.xlabel('', fontsize=16)  # Ось Х
fig.autofmt_xdate()  # Зображає позначки дат діагонально, щоб вони не перетиналися
plt.ylabel('Температура(F)', fontsize=16)  # Ось У
plt.tick_params(axis='both', which='major', labelsize=16)  # Підписи на розмітці

plt.show()  # Відкрити переглядач
