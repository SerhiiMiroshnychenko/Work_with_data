import csv

from plotly.graph_objs import Scattergeo, Layout
from plotly import offline

filename = 'data/world_fires_7_day.csv'
with open(filename) as f:
    reader = csv.reader(f)  # Створюємо об'єкт-читач і прив'язуємо його до змінної reader
    header_row = next(reader)  # Функція next() 'наступний' повертає наступний рядок у файлі
    # ^ Викликаємо лише один раз, щоб отримати перший рядок файлу, що містить файлові заголовки

    # Отримати високі температури з цього файлу
    brights, lons, lats = [], [], []
    for row in reader:  # Об'єкт reader продовжує роботу там, де зупинився останній раз
        # Позаяк ми вже зчитали назви стовпців, то починаємо роботу з їх вмістом
        bright = int(float(row[2]))
        lat = row[0]
        lon = row[1]
        lats.append(lat)
        lons.append(lon)
        brights.append(bright)

data = [{
    'type': 'scattergeo',
    'lon': lons,
    'lat': lats,
    'marker': {
        'size': [bright//50 for bright in brights],  # Задаємо розмір маркера на мапі
        'color': brights,  # Формуємо градуювання забарвлення по списку mags
        'colorscale': 'Reds',  # Задаємо кольорову схему
        'reversescale': True,  # Реверсуємо кольорову шкалу
        'colorbar': {'title': 'Яскравість пожежі'},  # Зображення кольорової шкали збоку мапи + задаємо її назву
    },
}]


my_layout = Layout(title='ГЛОБАЛЬНІ ПОЖЕЖІ')  # Даємо діаграмі ім'я

fig = {'data': data, 'layout': my_layout}  # Словник, що містить дані та компонування
offline.plot(fig, filename='global_fires.html')
