import json

from plotly.graph_objs import Scattergeo, Layout
from plotly import offline

# Дослідити структури даних
filename = 'data/eq_data_1_day_m1.json'
with open(filename) as f:
    all_eq_data = json.load(f)  # Конвертуємо вміст файлу в змінну all_eq_data

all_eq_dicts = all_eq_data['features']  # Створюємо список, що містить всі землетруси у вигляді словників

mags, lons, lats = [], [], []  # Порожній словник для магнітуд, довгот та широт
for eq_dict in all_eq_dicts:
    mag = eq_dict['properties']['mag']  # Видобуваємо послідовно кожну магнітуду
    lon = eq_dict['geometry']['coordinates'][0]  # Видобуваємо послідовно кожну довготу
    lat = eq_dict['geometry']['coordinates'][1]  # Видобуваємо послідовно кожну широту
    mags.append(mag)  # Додаємо значення у словник mags
    lons.append(lon)
    lats.append(lat)

# Нанести землетруси на мапу
data = [Scattergeo(lon=lons, lat=lats)]  # data --> список візуалізацій; Scattergeo --> об'єкт-діаграма мапи світу;
# lon=lons --> довготи; lat=lats --> широти.
my_layout = Layout(title='ГЛОБАЛЬНІ ЗЕМЛЕТРУСИ')  # Даємо діаграмі ім'я

fig = {'data': data, 'layout': my_layout}  # Словник, що містить дані та компонування
offline.plot(fig, filename='global_earthquakes.html')  # Передаємо fig та ім'я файлу в функцію plot
