from datetime import datetime

first_date = datetime.strptime('2018-07-01', '%Y-%m-%d')
print(first_date)

"""
%A -- Назва дня тижня англійською, наприклад 'Monday'
%B -- Назва місяця англійською, наприклад 'January'
%m -- Номер місяця від 01 до 12
%d -- День місяця числом від 01 до 31
%Y -- Рік, чотири цифри, наприклад 2022
%y -- Рік, дві цифри, наприклад 22
%H -- Година в 24-годинному форматі (від 00 до 23)
%I -- Година в 12-годинному форматі (від 01 до 12)
%p -- 'am' (ранку) чи 'pm' (вечора)
%M -- Хвилини (від 00 до 59)
%S -- Секунди (від 00 до 59)
"""