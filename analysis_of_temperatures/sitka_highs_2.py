import csv
from datetime import datetime

import matplotlib.pyplot as plt

filename = 'data/sitka_weather_07-2018_simple.csv'
with open(filename) as f:
    reader = csv.reader(f)  # Створюємо об'єкт-читач і прив'язуємо його до змінної reader
    header_row = next(reader)  # Функція next() 'наступний' повертає наступний рядок у файлі
    # ^ Викликаємо лише один раз, щоб отримати перший рядок файлу, що містить файлові заголовки

    # Отримати високі температури з цього файлу
    dates, highs = [], []
    for row in reader:  # Об'єкт reader продовжує роботу там, де зупинився останній раз
        # Позаяк ми вже зчитали назви стовпців, то починаємо роботу з їх вмістом
        current_date = datetime.strptime(row[2], '%Y-%m-%d')  # Конвертуємо дані з індексом [2] в datetime об'єкти
        high = int(row[5])  # Витягаємо данні з індексом [5] -> TMAX == максимальна температура
        dates.append(current_date)  # Формуємо список з дат
        highs.append(high)  # Формуємо список з температур

# Створити графік високих температур
plt.style.use('seaborn-v0_8')  # Обираємо стиль
fig, ax = plt.subplots()  # Створюємо діаграми
ax.plot(dates, highs, c='red')  # Передаємо список highs, робимо його крапки червоними

# Відформатувати графік
plt.title('Максимальні добові температури, липень 2018', fontsize=24)  # Задаємо назву
plt.xlabel('', fontsize=16)  # Ось Х
fig.autofmt_xdate()  # Зображає позначки дат діагонально, щоб вони не перетиналися
plt.ylabel('Температура(F)', fontsize=16)  # Ось У
plt.tick_params(axis='both', which='major', labelsize=16)  # Підписи на розмітці

plt.show()  # Відкрити переглядач
