import json

# Дослідити структури даних
filename = 'data/eq_data_1_day_m1.json'
with open(filename) as f:
    all_eq_data = json.load(f)  # Конвертуємо вміст файлу в змінну all_eq_data

readable_file = 'data/readable_eq_data.json'  # Створюємо читабельний файл
with open(readable_file, 'w') as f:
    json.dump(all_eq_data, f, indent=4)  # indent=4 --> табуляція, що відповідає структурі даних
