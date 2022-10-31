import csv

import matplotlib.pyplot as plt

filename = 'data/sitka_weather_07-2018_simple.csv'
with open(filename) as f:
    reader = csv.reader(f)  # Створюємо об'єкт-читач і прив'язуємо його до змінної reader
    header_row = next(reader)  # Функція next() 'наступний' повертає наступний рядок у файлі
    # ^ Викликаємо лише один раз, щоб отримати перший рядок файлу, що містить файлові заголовки

    # Отримати високі температури з цього файлу
    highs = []
    for row in reader:  # Об'єкт reader продовжує роботу там, де зупинився останній раз
        # Позаяк ми вже зчитали назви стовпців, то починаємо роботу з їх вмістом
        high = int(row[5])  # Витягаємо данні з індексом [5] -> TMAX == максимальна температура
        highs.append(high)  # Формуємо список з цих даних

# Створити графік високих температур
plt.style.use('seaborn-v0_8')  # Обираємо стиль
fig, ax = plt.subplots()  # Створюємо діаграми
ax.plot(highs, c='red')  # Передаємо список highs, робимо його крапки червоними

# Відформатувати графік
plt.title('Максимальні добові температури, липень 2018', fontsize=24)  # Задаємо назву
plt.xlabel('', fontsize=16)  # Ось Х
plt.ylabel('Температура(F)', fontsize=16)  # Ось У
plt.tick_params(axis='both', which='major', labelsize=16)  # Підписи на розмітці

plt.show()  # Відкрити переглядач
