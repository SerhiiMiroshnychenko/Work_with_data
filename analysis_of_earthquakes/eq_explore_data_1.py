import json

# Дослідити структури даних
filename = 'data/eq_data_1_day_m1.json'
with open(filename) as f:
    all_eq_data = json.load(f)  # Конвертуємо вміст файлу в змінну all_eq_data

all_eq_dicts = all_eq_data['features']  # Створюємо список, що містить всі землетруси у вигляді словників
print(len(all_eq_dicts))  # Перевіряємо кількість елементів: 158 словників

mags = []  # Порожній словник для магнітуд
for eq_dict in all_eq_dicts:
    mag = eq_dict['properties']['mag']  # Видобуваємо послідовно кожну магнітуду
    mags.append(mag)  # Додаємо значення у словник mags

print(mags[:10])  # Друк перших 10 значень для перевірки

