import json

# Дослідити структури даних
filename = 'data/eq_data_1_day_m1.json'
with open(filename) as f:
    all_eq_data = json.load(f)  # Конвертуємо вміст файлу в змінну all_eq_data

all_eq_dicts = all_eq_data['features']
print(len(all_eq_dicts))
    