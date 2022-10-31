import csv

filename = 'data/sitka_weather_07-2018_simple.csv'
with open(filename) as f:
    reader = csv.reader(f)  # Створюємо об'єкт-читач і прив'язуємо його до змінної reader
    header_row = next(reader)  # Функція next() 'наступний' повертає наступний рядок у файлі
    # ^ Викликаємо лише один раз, щоб отримати перший рядок файлу, що містить файлові заголовки

    for index, column_header in enumerate(header_row):  # Функція enumerate() повертає
        # індекс кожного елемента та його значення
        print(index, column_header)  # Виводимо індекси стовпців та іх назви

    # Отримати високі температури з цього файлу
    highs = []
    for row in reader:  # Об'єкт reader продовжує роботу там, де зупинився останній раз
        # Позаяк ми вже зчитали назви стовпців, то починаємо роботу з їх вмістом
        high = int(row[5])  # Витягаємо данні з індексом [5] -> TMAX == максимальна температура
        highs.append(high)  # Формуємо список з цих даних

print(highs)
