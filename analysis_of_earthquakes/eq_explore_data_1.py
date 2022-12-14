import json

# Дослідити структури даних
filename = 'data/eq_data_1_day_m1.json'
with open(filename) as f:
    all_eq_data = json.load(f)  # Конвертуємо вміст файлу в змінну all_eq_data

all_eq_dicts = all_eq_data['features']  # Створюємо список, що містить всі землетруси у вигляді словників
print(len(all_eq_dicts))  # Перевіряємо кількість елементів: 158 словників

mags, longs, lats = [], [], []  # Порожній словник для магнітуд, довгот та широт
for eq_dict in all_eq_dicts:
    mag = eq_dict['properties']['mag']  # Видобуваємо послідовно кожну магнітуду
    long = eq_dict['geometry']['coordinates'][0]  # Видобуваємо послідовно кожну довготу
    lat = eq_dict['geometry']['coordinates'][1]  # Видобуваємо послідовно кожну широту
    mags.append(mag)  # Додаємо значення у словник mags
    longs.append(long)
    lats.append(lat)

print(mags[:10])  # Друк перших 10 значень для перевірки
print(longs[:5])
print(lats[:5])
